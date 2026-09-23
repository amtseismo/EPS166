# Optical Satellite Imagery

## Purpose

Optical satellites have observed Earth's surface continuously since 1972. By comparing images acquired before and after a geological event, or by tracking the motion of surface features through time, we can measure deformation that other methods cannot easily see.

In this lecture, we will:

- describe how optical satellites acquire multispectral images
- explain the difference between line-scanning and push-broom instruments
- distinguish free and commercial satellite missions and their trade-offs
- interpret false-color imagery and spectral indices
- understand why sun-synchronous orbits matter for time-series analysis
- identify how optical imagery is used to measure crustal deformation

---

# Imaging Earth From Space

## The Landsat Record

The Landsat mission is the longest-running civilian Earth observation program. It began in 1972 with the launch of ERTS-1, later renamed Landsat 1, and has continued uninterrupted through Landsat 9 (launched 2021).

This continuity is scientifically invaluable. A 50-year archive of the same locations, acquired with consistent geometry and calibration, allows us to detect slow changes in land cover, glacier extent, river migration—and fault creep.

Key milestones:

| Satellites | Instrument | Years active | Key capability |
|---|---|---|---|
| Landsat 1–3 | MSS | 1972–1983 | 4 bands (VIS + NIR), 80 m |
| Landsat 4–5 | TM | 1982–2013 | 7 bands, 30 m; Landsat 5 lasted 29 years |
| Landsat 7 | ETM+ | 1999–present | Added 15 m panchromatic |
| Landsat 8–9 | OLI + TIRS | 2013–present | 11 bands, push-broom, 30 m / 15 m pan |

```{figure} ../figures/07_landsat_timeline.png
---
width: 800px
alt: Timeline of Landsat missions from 1972 to present showing instrument generations and overlap periods.
---
The Landsat mission timeline. Overlapping launches ensured continuity of the archive. Landsat 5 vastly exceeded its design life, operating for 29 years.
```

---

## How Do Optical Satellites Acquire Images?

### Line Scanning

Early Landsats (1–7) used a **line-scanning** approach: a rotating mirror sweeps reflected light from the ground across a set of detectors. The mirror scans perpendicular to the flight direction while the satellite moves forward, building up an image one line at a time.

The size of each detector controls spatial resolution. Larger detectors collect more photons but blur fine detail; smaller detectors improve resolution but require more light or a narrower spectral band. This trade-off is why Landsat 7's thermal band (band 6) has 60 m pixels while its panchromatic band (band 8) achieves 15 m.

### Push Broom

Modern satellites—including Landsat 8/9, Sentinel-2, SPOT 6/7, and Pleiades—use a **push-broom** design. A linear array of detectors, oriented perpendicular to the flight track, images an entire row of pixels simultaneously as the satellite moves forward. There are no moving mirrors.

Push-broom instruments are more reliable (fewer mechanical parts), more sensitive (each detector stares at the ground longer), and better suited to very high resolution.

```{figure} ../figures/07_line_scan_pushbroom.png
---
width: 760px
alt: Schematic comparison of line-scanning and push-broom imaging modes.
---
Line scanning (left) uses a rotating mirror to sweep across the swath. Push broom (right) images the full swath width simultaneously with a linear detector array.
```

---

# Spectral Bands

## What Do the Bands Measure?

Multispectral satellites record reflected electromagnetic radiation across several wavelength ranges simultaneously. Each band is sensitive to a different physical property of the surface.

For Landsat 8's OLI instrument:

| Band | Name | Wavelength | Spatial res. | Primary use |
|---|---|---|---|---|
| 1 | Deep blue (coastal) | 0.43–0.45 µm | 30 m | Aerosols, coastal water |
| 2 | Blue | 0.45–0.51 µm | 30 m | Water depth, atmosphere |
| 3 | Green | 0.53–0.59 µm | 30 m | Vegetation, water |
| 4 | Red | 0.64–0.67 µm | 30 m | Vegetation discrimination |
| 5 | Near infrared (NIR) | 0.85–0.88 µm | 30 m | Vegetation, biomass |
| 6 | SWIR-1 | 1.57–1.65 µm | 30 m | Soil moisture, geology |
| 7 | SWIR-2 | 2.11–2.29 µm | 30 m | Clay minerals, geology |
| 8 | Panchromatic | 0.50–0.68 µm | **15 m** | High-resolution detail |
| 9 | Cirrus | 1.36–1.38 µm | 30 m | High cloud detection |
| 10–11 | Thermal (TIRS) | 10.6–12.5 µm | 100 m | Surface temperature |

---

## False-Color Imagery

Our eyes see only three colors—red, green, and blue. By assigning satellite bands to these display colors, we can visualize wavelengths that are invisible to us.

A common combination for geology and vegetation is **bands 5-4-2** (NIR→red display, red→green display, green→blue display):

- **Vegetation** appears bright green because plants strongly reflect NIR (band 5 → red channel) and visible green (band 2 → blue channel), producing a combined yellow-green.
- **Water** appears very dark—it absorbs strongly at NIR wavelengths.
- **Built-up areas** appear purplish, reflecting broadly across the visible but less in NIR.
- **Bare rock and soil** varies with mineralogy.

> What color would fresh lava appear in a 5-4-2 image, and why?

```{figure} ../figures/07_false_color_comparison.png
---
width: 820px
alt: Three panels showing the same scene in true color (3-2-1), false color (5-4-2), and NDVI.
---
The same scene shown in natural color (bands 3-2-1), false color (bands 5-4-2), and NDVI. Vegetation is dark green in natural color, bright green in false color, and bright (high NDVI) in the index image.
```

---

## The Normalized Difference Vegetation Index (NDVI)

Vegetation has a characteristic spectral signature: it absorbs red light strongly (for photosynthesis) and scatters near-infrared light strongly (from leaf cell structure). This contrast is the basis of the **NDVI**:

$$
\text{NDVI} = \frac{\rho_{\text{NIR}} - \rho_{\text{red}}}{\rho_{\text{NIR}} + \rho_{\text{red}}}
$$

where $\rho$ denotes surface reflectance.

- Dense green vegetation: NDVI → 1
- Bare rock, concrete, soil: NDVI → 0
- Water: NDVI < 0

NDVI is useful in geology wherever vegetation follows geological boundaries—fault traces damming groundwater, soil chemistry controlling plant communities, or volcanic heat stimulating anomalous growth before an eruption.

> **Example:** The San Andreas Fault near the Coachella Valley supports a line of oases where the fault gauge dams subsurface groundwater flow. This line of vegetation is detectable in NDVI imagery even where there is no topographic expression.

```{figure} ../figures/07_ndvi_fault.png
---
width: 760px
alt: NDVI image of a fault zone showing a linear vegetation anomaly coinciding with the fault trace.
---
NDVI can reveal fault traces through their control on groundwater and soil properties, even in arid environments where no topographic scarp is visible.
```

---

# Satellite Missions

## Sentinel-2

Sentinel-2 is a two-satellite constellation operated by the European Space Agency. The two satellites (2A and 2B) are phased six days apart in the same orbit, providing combined revisit times of five days at the equator and more frequently at higher latitudes.

Key specifications:
- **13 spectral bands** from visible through SWIR
- **10 m** resolution in visible and NIR bands (better than Landsat)
- **290 km swath** (wider than Landsat or SPOT)
- **Freely available** through the Copernicus Data Space

Sentinel-2 does not carry a thermal band, but its higher spatial resolution and more frequent revisit make it particularly useful for tracking surface changes and pixel-tracking deformation.

```{figure} ../figures/07_sentinel2_landsat_comparison.png
---
width: 800px
alt: Spectral band comparison between Sentinel-2 MSI and Landsat 8 OLI showing band positions and widths.
---
Sentinel-2 and Landsat 8 spectral band comparison. Sentinel-2 adds several narrow red-edge bands for vegetation discrimination and a water vapor band, and achieves 10 m resolution in its visible and NIR bands.
```

---

## SPOT

The SPOT (Satellite Pour l'Observation de la Terre) series is a French constellation now operating on its sixth and seventh satellites. A key capability that distinguishes SPOT from Landsat and Sentinel-2 is its **steerable cameras**: the instrument can be tilted up to 30° either side of nadir. This allows:

- **Rapid revisit** of a specific target without waiting for the satellite's ground track to pass overhead
- **Along-track and across-track stereo** for generating digital elevation models

SPOT's spectral coverage is more limited than Landsat (green, red, NIR, and panchromatic), but its spatial resolution has improved steadily, reaching **6 m** for multispectral and **1.5 m** for panchromatic on SPOT 6/7. Swath width is 60 km—smaller than Landsat or Sentinel-2.

---

## Very High Resolution: WorldView and Pleiades

Commercial satellites from Maxar (WorldView series) and Airbus (Pleiades) achieve sub-meter panchromatic resolution:

| Mission | Pan resolution | MS resolution | Swath | Operator |
|---|---:|---:|---:|---|
| WorldView-3 | 0.31 m | 1.24 m | 13.1 km | Maxar |
| Pleiades 1A/1B | 0.50 m | 2.0 m | 20 km | Airbus |

At these resolutions, individual buildings, vehicles, and surface rupture features become visible. Pleiades can acquire **tri-stereo** imagery in both along-track and across-track directions, enabling elevation models even in deep canyons and between buildings.

> These data are not freely available. Access typically requires a purchase or research agreement.

```{figure} ../figures/07_vhr_kokoxili.png
---
width: 800px
alt: IKONOS imagery of the Kokoxili earthquake rupture showing offset stream channels and a pull-apart structure.
---
IKONOS imagery of the 2001 Kokoxili earthquake rupture on the Kunlun fault, Tibet (Klinger et al., 2005). At 1 m resolution, individual offset stream channels and a pull-apart extensional structure are visible. Sliding the pre- and post-earthquake images to align offset features yields slip estimates along the rupture.
```

---

## Planet

Planet Labs operates a large constellation of CubeSats (**PlanetScope**), currently numbering over 130 satellites. Though individually modest (~3–5 m resolution, 4 visible/NIR bands), the constellation's size provides **daily global coverage** at moderate resolution.

Planet imagery played a critical role in the 2019 Ridgecrest, California earthquake sequence: images were acquired between the M6.4 and M7.1 mainshocks, allowing scientists to separate the surface ruptures produced by each event—something no other satellite could have provided at that moment.

---

# Satellite Orbits

## Orbital Mechanics

Satellites orbit Earth on elliptical paths. For imaging satellites the orbits are nearly circular, at altitudes of roughly 500–800 km. The orbital period follows from Newton's laws:

$$
T = 2\pi\sqrt{\frac{r^3}{GM_\oplus}}
$$

where $r$ is the orbital radius, $G$ is the gravitational constant, and $M_\oplus$ is Earth's mass. At 700 km altitude, the period is approximately 100 minutes—about 14 orbits per day.

A special case: at ~36,000 km the period equals 24 hours. A satellite in this **geostationary** orbit hovers over the same point on the equator indefinitely. This is impractical for high-resolution imaging but ideal for weather satellites and communications.

---

## Sun-Synchronous Orbits

For time-series analysis of surface change, consistent illumination is essential. If a satellite imaged the same location at different times of day throughout the year, shadowing from topography would change with solar angle, making it impossible to distinguish real surface change from illumination effects.

The solution is a **sun-synchronous orbit**: the orbital plane precesses at the same rate Earth orbits the Sun (~1°/day), so the satellite crosses every latitude at the same local solar time on every pass.

This precession is achieved by choosing orbital altitude and inclination carefully to exploit the torque exerted by Earth's equatorial bulge on an inclined polar orbit.

For Landsat, the result is:
- **16-day repeat cycle** (233 orbits)
- **~10:00–10:30 AM** local acquisition time at all latitudes
- Consistent illumination geometry across the entire 50-year archive

> Sun-synchronicity is why you can meaningfully compare a Landsat image from 1990 to one from today: the illumination angle is nearly identical.

```{figure} ../figures/07_sun_synchronous_orbit.png
---
width: 760px
alt: Diagram of a sun-synchronous polar orbit showing the orbital plane rotating to keep pace with Earth's motion around the Sun.
---
A sun-synchronous orbit precesses at 360°/year, matching Earth's orbital motion around the Sun. The satellite always crosses a given latitude at the same local solar time, keeping illumination consistent throughout the year.
```

---

# Optical Imagery and Crustal Deformation

## What Can Optical Imagery Measure?

Optical imagery measures **position of surface features**. If the same feature can be identified in two images acquired at different times, its displacement between images can be estimated.

Two main approaches:

**1. Visual mapping**
At very high resolution, co-seismic surface ruptures, offsets of stream channels, displaced fence lines, and landslide scarps can be identified and measured directly.

**2. Pixel tracking (sub-pixel correlation)**
Cross-correlating two images at the sub-pixel level yields a displacement field across the entire scene. This works best when:
- the surface has stable texture (rocks, bare ground, crops in a consistent state)
- the two images are taken with similar viewing geometry and illumination
- deformation signals are larger than the noise floor (~1/10 pixel)

For Sentinel-2 at 10 m resolution, this corresponds to sensitivity of roughly **1 m** of surface displacement.

---

## Why Optical Complements InSAR for Strike-Slip Faults

InSAR measures displacement in the **satellite line-of-sight (LOS)** direction—a mix of vertical and horizontal motion projected onto the look vector. For Sentinel-1, the look direction is roughly 35–40° from vertical and nearly perpendicular to the along-track direction.

For a **strike-slip fault** oriented parallel to the satellite track (such as the Hayward or San Andreas fault), fault-parallel horizontal motion is nearly **perpendicular to the LOS**. InSAR is largely blind to it.

Optical pixel tracking measures displacement in **both the range and azimuth directions** of the image. The azimuth direction is approximately along-track—and therefore **parallel to a NW-trending fault**. This is precisely the component InSAR misses.

$$
\text{InSAR sensitivity to strike-slip} \approx \sin(\delta)\sin(\alpha - \phi)
$$

where $\delta$ is the dip of the look vector, $\alpha$ is the look azimuth, and $\phi$ is the fault strike. When $\alpha \approx \phi$, the sensitivity approaches zero.

> This is why optical pixel tracking is the tool of choice for measuring Hayward fault creep from space.

```{figure} ../figures/07_insar_vs_optical_geometry.png
---
width: 820px
alt: Diagram comparing InSAR line-of-sight sensitivity and optical azimuth sensitivity for a strike-slip fault.
---
InSAR LOS is nearly perpendicular to fault-parallel motion on a NW-trending strike-slip fault. Optical pixel tracking in the image azimuth direction is sensitive to exactly this component.
```

---

# Summary

- Optical satellites record reflected radiation across multiple spectral bands at spatial resolutions from 30 m (Landsat, Sentinel-2) to less than 1 m (WorldView, Pleiades).
- Line-scanning instruments sweep a mirror; push-broom instruments image a full row of pixels simultaneously. Most modern satellites use push broom.
- False-color composites and indices like NDVI make non-visible information interpretable and can reveal geological features.
- Sun-synchronous orbits provide consistent illumination across a multi-decade archive, essential for time-series analysis.
- Pixel tracking—sub-pixel cross-correlation of image pairs—extends optical imagery to the measurement of surface displacement.
- For NW-trending strike-slip faults, optical azimuth offsets are sensitive to fault-parallel motion that InSAR cannot measure.

> In the next lecture, we turn to InSAR—a fundamentally different way of measuring displacement from space, and a natural complement to what optical imagery can and cannot see.

---

# Laboratory

Students will use Sentinel-2 imagery to measure surface deformation associated with creep on the Hayward fault near Fremont, California:

- download pre- and post-event Sentinel-2 scenes from the Copernicus Data Space API
- apply sub-pixel cross-correlation to estimate azimuth and range offsets
- interpret the spatial pattern of displacement relative to the fault trace
- compare optical azimuth offsets to any available GNSS or InSAR observations
- discuss why InSAR is insensitive to this signal

---

# Additional Resources

> **Paper:** Klinger, Y., et al. (2005). Coseismic surface rupture and basin-forming faulting along the El Asnam fault during the 1980 Ms = 7.3 earthquake: a re-analysis from satellite imagery. *BSSA*.

> **Tool:** [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)  
> Free access to the complete Sentinel-1 and Sentinel-2 archives. Registration required.

> **Tool:** [USGS EarthExplorer](https://earthexplorer.usgs.gov/)  
> Download the full Landsat archive. Search by location, date, and cloud cover.

> **Paper:** Leprince, S., et al. (2007). Automatic and precise orthorectification, coregistration, and subpixel correlation of satellite images, application to ground deformation measurements. *IEEE TGRS*, 45(6), 1529–1558.  
> The foundational paper for the COSI-Corr pixel-tracking method.
