"""
prepare_ridgecrest_data.py
==========================
Download two Sentinel-2 Level-2A scenes (Band 8, NIR, 10 m) covering the
2019 Ridgecrest earthquake sequence, clip them to a common AOI centred on
the M7.1 surface rupture, and write two Cloud-Optimized GeoTIFFs ready for
the EPS 166 Lab 4 pixel-tracking notebook.

Run this script ONCE on your own machine, then commit the two output files
to the course GitHub repository at:

    datasets/ridgecrest_pre_B08.tif
    datasets/ridgecrest_post_B08.tif

Requirements
------------
    pip install rasterio shapely sentinelsat tqdm

Copernicus account
------------------
Register (free) at https://dataspace.copernicus.eu/ and set your credentials
as environment variables before running:

    export CDSE_USER="your@email.com"
    export CDSE_PASSWORD="yourpassword"

Or hard-code them in the CREDENTIALS block below (never commit credentials
to the repo).

Scene selection
---------------
Pre-event  : S2B_MSIL2A_20190624  (2019-06-24, cloud cover < 1 %)
Post-event : S2A_MSIL2A_20190714  (2019-07-14, cloud cover < 2 %)

Both are from the same Sentinel-2 tile: T11SLT (UTM zone 11N).

The M7.1 mainshock occurred on 2019-07-05. The post-event scene was acquired
nine days later; the surface rupture is clearly visible.

AOI
---
A 52 × 52 km window centred on the rupture zone:
    lon: -117.95 to -117.35
    lat:  35.55  to  36.02

Output
------
Two single-band GeoTIFFs in UTM zone 11N (EPSG:32611), ~5000 × 5000 pixels,
~50 MB each uncompressed / ~10 MB each as LZW-compressed COG.
"""

import os
import sys
import zipfile
import tempfile
import pathlib
import rasterio
from rasterio.crs import CRS
from rasterio.warp import transform_bounds
from rasterio.windows import from_bounds
from rasterio.enums import Resampling
import rasterio.shutil as rio_shutil

# ---------------------------------------------------------------------------
# Configuration — edit these if needed
# ---------------------------------------------------------------------------

# Copernicus Data Space credentials (or set env vars CDSE_USER / CDSE_PASSWORD)
CDSE_USER     = os.environ.get("CDSE_USER",     "")
CDSE_PASSWORD = os.environ.get("CDSE_PASSWORD", "")

# AOI in geographic coordinates (WGS-84)
AOI_LON_MIN = -117.95
AOI_LON_MAX = -117.35
AOI_LAT_MIN =  35.55
AOI_LAT_MAX =  36.02

# Sentinel-2 tile and product names
TILE = "T11SLT"

PRODUCTS = {
    "pre": {
        "name":    "S2B_MSIL2A_20190624T180919_N0500_R041_T11SLT_20230322T145520",
        "date":    "2019-06-24",
        "outfile": "datasets/ridgecrest_pre_B08.tif",
    },
    "post": {
        "name":    "S2A_MSIL2A_20190714T180921_N0500_R041_T11SLT_20230305T211504",
        "date":    "2019-07-14",
        "outfile": "datasets/ridgecrest_post_B08.tif",
    },
}

# Band to extract (Band 8 = NIR, 10 m)
BAND_SUFFIX = "B08.jp2"

# LZW compression for the output COGs
CREATION_OPTIONS = {
    "driver":       "GTiff",
    "dtype":        "uint16",
    "compress":     "lzw",
    "predictor":    2,
    "tiled":        True,
    "blockxsize":   512,
    "blockysize":   512,
    "interleave":   "band",
}

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_access_token(user, password):
    """Obtain a short-lived OAuth2 token from the Copernicus Identity Service."""
    import urllib.request
    import urllib.parse
    import json

    url  = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
    data = urllib.parse.urlencode({
        "grant_type": "password",
        "username":   user,
        "password":   password,
        "client_id":  "cdse-public",
    }).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)["access_token"]


def search_product(product_name, token):
    """Return the product UUID from the Copernicus OData catalogue."""
    import urllib.request
    import urllib.parse
    import json

    base = "https://catalogue.dataspace.copernicus.eu/odata/v1/Products"
    filt = f"Name eq '{product_name}'"
    url  = base + "?" + urllib.parse.urlencode({"$filter": filt, "$top": 1})
    req  = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    items = data.get("value", [])
    if not items:
        raise RuntimeError(f"Product not found in catalogue: {product_name}")
    return items[0]["Id"]


def download_product(product_id, token, dest_dir):
    """
    Download a Sentinel-2 product ZIP from the Copernicus Data Space.

    Parameters
    ----------
    product_id : str  UUID returned by search_product()
    token      : str  OAuth2 access token
    dest_dir   : str  Directory to save the ZIP

    Returns
    -------
    str  Path to the downloaded ZIP file
    """
    import urllib.request

    url     = f"https://catalogue.dataspace.copernicus.eu/odata/v1/Products({product_id})/$value"
    zip_path = os.path.join(dest_dir, f"{product_id}.zip")

    print(f"  Downloading {url[:80]}...")
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}"},
    )
    # Stream download with progress
    with urllib.request.urlopen(req, timeout=120) as response, \
         open(zip_path, "wb") as out:
        total = int(response.headers.get("Content-Length", 0))
        downloaded = 0
        chunk = 1 << 20  # 1 MB
        while True:
            buf = response.read(chunk)
            if not buf:
                break
            out.write(buf)
            downloaded += len(buf)
            if total:
                pct = 100 * downloaded / total
                print(f"\r  {downloaded/1e6:.0f} / {total/1e6:.0f} MB  ({pct:.0f}%)",
                      end="", flush=True)
    print()
    return zip_path


def find_band_jp2(zip_path, band_suffix):
    """
    Locate the Band 8 JP2 file inside a Sentinel-2 SAFE ZIP.

    Sentinel-2 L2A ZIPs contain JP2 files under
    GRANULE/<id>/IMG_DATA/R10m/<tile>_<date>_B08_10m.jp2

    Parameters
    ----------
    zip_path    : str  Path to the product ZIP
    band_suffix : str  e.g. "B08.jp2" (matches end of path)

    Returns
    -------
    str  The matching path *inside* the ZIP
    """
    with zipfile.ZipFile(zip_path) as zf:
        candidates = [
            n for n in zf.namelist()
            if n.endswith(band_suffix) and "R10m" in n
        ]
    if not candidates:
        raise RuntimeError(
            f"No file matching *R10m*{band_suffix} found in {zip_path}.\n"
            f"Available JP2s: {[n for n in candidates]}"
        )
    if len(candidates) > 1:
        print(f"  Multiple matches found; using first: {candidates[0]}")
    return candidates[0]


def clip_and_write_cog(zip_path, jp2_internal_path, aoi_bounds_geo, out_path):
    """
    Extract a JP2 from a ZIP, clip to the AOI, and write a COG GeoTIFF.

    Parameters
    ----------
    zip_path           : str  Path to the product ZIP
    jp2_internal_path  : str  Path inside the ZIP (from find_band_jp2)
    aoi_bounds_geo     : tuple (lon_min, lat_min, lon_max, lat_max) in WGS-84
    out_path           : str  Destination GeoTIFF path
    """
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)

    with tempfile.TemporaryDirectory() as tmp:
        # Extract just the one JP2 file
        with zipfile.ZipFile(zip_path) as zf:
            zf.extract(jp2_internal_path, tmp)

        jp2_path = os.path.join(tmp, jp2_internal_path)

        with rasterio.open(jp2_path) as src:
            img_crs = src.crs

            # Reproject the AOI bounding box into the image CRS
            aoi_utm = transform_bounds(
                CRS.from_epsg(4326),
                img_crs,
                *aoi_bounds_geo,
            )

            window = from_bounds(*aoi_utm, transform=src.transform)
            data   = src.read(1, window=window)
            transform_clipped = src.window_transform(window)

            print(f"  Clipped size : {data.shape[0]} rows × {data.shape[1]} cols")
            print(f"  Value range  : {data.min()} – {data.max()}")

            # Write temporary GeoTIFF, then copy as COG
            tmp_tif = os.path.join(tmp, "clipped.tif")
            with rasterio.open(
                tmp_tif,
                "w",
                **{
                    **CREATION_OPTIONS,
                    "width":     data.shape[1],
                    "height":    data.shape[0],
                    "count":     1,
                    "crs":       img_crs,
                    "transform": transform_clipped,
                },
            ) as dst:
                dst.write(data, 1)

            # Copy as Cloud-Optimized GeoTIFF
            rio_shutil.copy(tmp_tif, out_path, copy_src_overwrite=True,
                            driver="GTiff", compress="lzw", predictor=2,
                            tiled=True, blockxsize=512, blockysize=512)

    size_mb = os.path.getsize(out_path) / 1e6
    print(f"  Written: {out_path}  ({size_mb:.1f} MB)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not CDSE_USER or not CDSE_PASSWORD:
        print(
            "ERROR: Copernicus credentials not set.\n"
            "Export CDSE_USER and CDSE_PASSWORD as environment variables,\n"
            "or edit the CREDENTIALS block at the top of this script.\n"
            "Register (free) at https://dataspace.copernicus.eu/"
        )
        sys.exit(1)

    aoi_bounds_geo = (AOI_LON_MIN, AOI_LAT_MIN, AOI_LON_MAX, AOI_LAT_MAX)

    print("=" * 60)
    print("Ridgecrest Sentinel-2 data preparation for EPS 166 Lab 4")
    print("=" * 60)

    print("\n[1/4] Obtaining access token...")
    token = get_access_token(CDSE_USER, CDSE_PASSWORD)
    print("  Token obtained.")

    with tempfile.TemporaryDirectory() as tmp:
        for key, product in PRODUCTS.items():
            print(f"\n[{key.upper()} scene — {product['date']}]")

            if os.path.exists(product["outfile"]):
                print(f"  Output already exists: {product['outfile']} — skipping.")
                continue

            print(f"  Searching catalogue for {product['name'][:50]}...")
            product_id = search_product(product["name"], token)
            print(f"  Found product UUID: {product_id}")

            zip_path = download_product(product_id, token, tmp)

            print(f"  Locating {BAND_SUFFIX} inside ZIP...")
            jp2_path = find_band_jp2(zip_path, BAND_SUFFIX)
            print(f"  Found: {jp2_path}")

            print(f"  Clipping to AOI and writing COG...")
            clip_and_write_cog(
                zip_path, jp2_path, aoi_bounds_geo, product["outfile"]
            )

    print("\n[4/4] All done.")
    print("\nNext steps:")
    print("  git add datasets/ridgecrest_pre_B08.tif datasets/ridgecrest_post_B08.tif")
    print("  git commit -m 'Add Ridgecrest Sentinel-2 Band 8 clips for Lab 4'")
    print("  git push")


if __name__ == "__main__":
    main()
