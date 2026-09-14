# Reading Earthquakes in the Landscape: DEMs, Photogrammetry, and Lidar

## Purpose

The landscape is a long-term archive of fault activity. Fault scarps, offset stream channels, pressure ridges, and sag ponds record not just the most recent earthquake but the cumulative history of repeated ruptures over thousands of years. To read this archive we need high-resolution topographic data — and in the last two decades the tools available for measuring topography have been revolutionized.

In this lecture we will:

- define digital elevation models (DEMs) and describe their uses in active tectonics
- explain how stereophotogrammetry uses image distortion to reconstruct topography from satellite imagery
- describe how airborne lidar generates dense point clouds and how vegetation filtering reveals the bare earth
- show how pre- and post-earthquake point clouds can be differenced and matched to recover 3D coseismic displacements
- introduce structure from motion (SfM) as an inexpensive alternative that brings these capabilities to drones and consumer cameras

This lecture draws heavily on material provided by Ed Nissen (University of Victoria) and Barry Parsons (University of Oxford), with thanks to both.

---

# Digital Elevation Models

---

## What Is a DEM?

A **digital elevation model (DEM)** is a digital dataset representing the elevation of the Earth's surface, sampled at regular horizontal spacing and georeferenced to known coordinates. It is simply a grid of numbers — elevation values at each pixel — that can be visualized, analyzed, and compared.

DEMs go by several names depending on context:
- **DEM** — digital elevation model (generic)
- **DTM** — digital terrain model (often implies bare-earth, vegetation removed)
- **DSM** — digital surface model (includes vegetation and buildings)

The distinction between DTM and DSM matters enormously for active tectonic applications, as we will see when we discuss lidar.

---

## Uses in Active Tectonics

### Geomorphic mapping of fault zones

The most direct application of DEMs in active tectonics is mapping the geomorphic expression of faults — the features in the landscape that record repeated earthquake rupture.

```{figure} ../figures/07_tibet_dem_fault.png
---
width: 720px
alt: Shaded relief DEM of the Mani fault zone in Tibet showing a fault scarp, pressure ridge, and offset ridges from the 1997 earthquake.
---
Shaded relief DEM of the fault zone associated with the 1997 Mani earthquake in Tibet. From the topography alone it is possible to identify a clear fault scarp (formed by repeated earthquakes), a pressure ridge (caused by transpression — compression added to the dominant strike-slip motion), and offset ridges that were once continuous alluvial fan surfaces now separated by right-lateral slip. After Funning (GEO 147 lecture notes).
```

Characteristic landforms that record fault activity:

| Feature | Fault type | What it records |
|---------|-----------|----------------|
| Fault scarp | Any | Repeated dip-slip or oblique displacement; height accumulates over many earthquakes |
| Offset channel / stream | Strike-slip | Cumulative lateral slip; offsets can be measured and linked to earthquake history |
| Pressure ridge | Transpressional | Compressional restraining bend in a strike-slip fault |
| Sag pond | Strike-slip / normal | Depression at releasing bend or along fault trace; often preserves sedimentary record |
| Triangular facet | Normal | Repeatedly refreshed fault scarp face; angle encodes slip rate and erosion rate |

---

## Hillshade Visualization

A raw DEM is hard to interpret visually — elevation values vary smoothly and the eye does not perceive subtle topographic variations well in a simple color map. **Hillshading** (also called shaded relief) dramatically improves interpretability by simulating a light source illuminating the surface from a specified direction and angle.

```{figure} ../figures/07_greece_dem_hillshade.png
---
width: 680px
alt: Side-by-side comparison of a hillshaded DEM and a Landsat image of the Paleochori fault area in Greece.
---
Hillshaded DEM (left) and Landsat false-color image (right) of the Paleochori fault area, Greece, which ruptured in a 1997 M6.5 earthquake. Both are illuminated from the southeast at 45° elevation. The fault scarp is clearly visible in the DEM as a bright-on-one-side, dark-on-the-other feature — the illuminated northeast-facing slope is bright; the shadowed northwest-facing slope is dark. After Funning (GEO 147 lecture notes).
```

Technically, hillshading modifies each pixel's color by moving it along the color vector in RGB space toward white (bright, sunlit) or toward black (shadowed), proportional to the calculated illumination angle. This is why hillshaded DEMs resemble oblique aerial photographs — they are simulating the same physical process of directional illumination.

👉 **The choice of illumination direction matters.** A fault scarp that runs parallel to the illumination direction will be invisible in the hillshade. Always view active fault zones from multiple illumination directions.

---

## Additional DEM Applications

**Topographic profiling and plateau analysis**
DEMs can extract quantitative topographic profiles across entire mountain belts. Fielding et al. (1994, "How flat is Tibet?") used GTOPO30 to show that the Tibetan Plateau maintains a remarkably uniform mean elevation of ~5,000 m — evidence for a maximum elevation sustained by the India–Eurasia collision.

**Synthetic drainage analysis**
Given a DEM, the flow direction at any pixel can be computed as the direction of steepest descent among its neighbors. Repeating this analysis across all pixels builds a synthetic drainage network — a hierarchy of first-, second-, third-order streams — without leaving the office. Drainage patterns are sensitive to fault activity: streams captured, deflected, or incised by fault motions leave distinctive signatures in the synthetic network.

---

## From Surveying to Satellite Photogrammetry

The oldest topographic maps in North America were made by traditional field surveying — teams of surveyors carrying plane tables, inclinometers, and theodolites from station to station, measuring azimuths and inclinations to every visible feature, then triangulating their positions in the office. This was extraordinarily labor-intensive.

When aerial photogrammetry became available in the 1930s — making topography from stereo pairs of aerial photographs — it rapidly displaced ground surveying. The same principles now apply to satellite imagery.

---

# Stereophotogrammetry

---

## How Humans See Depth

Stereophotogrammetry exploits the same geometric principle that allows humans to perceive depth: **parallax**. When you look at an object from two slightly different vantage points (your left and right eyes), near objects subtend a wider angle between the two viewpoints than distant objects. Your brain uses this angular difference — the **parallax angle** — to reconstruct depth.

Stereophotogrammetry replaces your two eyes with two satellite images acquired from different orbital positions or look angles. The parallax of features in the two images — how much a feature's position shifts between them — encodes its height above a reference surface.

---

## Image Distortion and Topographic Relief Displacement

When a camera images a surface from an oblique angle, features that protrude above the reference surface appear displaced in the image relative to where they would appear if the surface were flat. This **relief displacement** is the raw signal that stereophotogrammetry exploits.

For a feature of height $h$ above the reference surface, imaged at horizontal distance $R$ from the nadir point by a camera at altitude $H$:

$$\delta r = \frac{h \cdot R}{H}$$

The displacement in the image is proportional to the ratio of the feature height to the camera altitude, scaled by the distance from nadir. For typical satellite systems:

| Platform | Altitude (km) | Distortion per 500 m relief |
|---------|--------------|---------------------------|
| Aircraft (metric camera) | 10 | ~200 m |
| Low-orbit metric camera | 250 | ~180 m |
| Landsat | 705 | ~64 m |
| SPOT (nadir mode) | 832 | ~18 m |
| SPOT (tilted 27°) | 832 | ~271 m |

The much larger distortion in SPOT's tilted mode is precisely what makes it useful for stereophotogrammetry — larger distortion means a stronger signal to exploit.

---

## The Stereo Principle: Two Views, Two Unknowns

A single oblique image cannot separate height $h$ from horizontal position $R$ — the two are entangled in the distortion formula. Adding a second image from a different viewing angle provides a second equation, resolving the two unknowns:

$$h = H \cdot \frac{b}{B}$$

where $B$ is the baseline between the two satellite positions and $b$ is the measured parallax between corresponding features in the two images. The ratio $B/H$ — the **base-to-height ratio** — controls the stereo sensitivity. Values between 0.3 and 1.0 are optimal: too small and there is little stereo effect; too large and features cannot be matched between the two images.

```{figure} ../figures/07_spot_stereo_greece.png
---
width: 720px
alt: Two SPOT images of a fault scarp in Greece acquired from different look angles, showing different distortions of a road on the fault scarp face.
---
Two SPOT images of a normal fault scarp in Greece acquired at incidence angles of 14° (left-looking) and 23° (right-looking). A road at the foot of the scarp appears at similar positions in both images, but a road partway up the steep scarp face appears at significantly different positions — the parallax caused by its elevation above the reference surface. This parallax is the raw signal used to reconstruct the DEM. After Funning (GEO 147 lecture notes).
```

---

## Orthorectification

A by-product of the stereophotogrammetric process is **orthorectification** — removing perspective distortion from imagery so that every pixel appears as if viewed from directly overhead. Orthorectified images are geometrically consistent with maps and can be draped accurately onto DEMs. Google Earth uses orthorectified imagery throughout.

Orthorectification requires accurate ground control points (GCPs) — locations with known 3D coordinates in the image. In practice, ~30 or more well-distributed GCPs are needed to achieve map-quality accuracy.

---

## Global DEM Products from Stereophotogrammetry

| Dataset | Source | Resolution | Coverage | Released |
|---------|--------|-----------|---------|---------|
| SRTM | Space Shuttle InSAR (C-band) | 30 m | 60°S–60°N | 2000/2015 |
| ASTER GDEM | Terra ASTER stereo | 30 m | 83°S–83°N | 2009 |
| TanDEM-X | TanDEM-X radar interferometry | 12 m | Global | 2016 |
| Copernicus DEM | TanDEM-X | 30/10 m | Global | 2021 |
| ArcticDEM | DigitalGlobe stereo | 2 m | Arctic | Ongoing |

SRTM remains the standard for most global InSAR applications because it uses C-band radar (the same frequency as ERS and Sentinel-1), so it scatters from the same surface features — including vegetation canopy — as the interferograms it is used to correct.

---

# Lidar and Point Clouds

---

## The Resolution Revolution

The history of global topographic data shows a steady march toward higher resolution:

- **1 km** — early global datasets (GTOPO30, early ETOPO)
- **90 m** — SRTM global release (2005)
- **30 m** — SRTM US release, ASTER GDEM (2009)
- **1 m and better** — airborne lidar, now routinely available for much of the US

Each step change in resolution has opened new scientific questions. At 1 km, only large-scale topographic features are visible. At 30 m, fault scarps become apparent. At 1 m and below, individual offset stream channels, fault trace complexity, and even surface rupture geometry can be mapped directly from the topographic data.

---

## How Airborne Lidar Works

**Lidar** (light detection and ranging) measures distance by emitting laser pulses and timing their return. An airborne lidar system:

1. Fires laser pulses at 10,000–100,000+ Hz, sweeping a fan-shaped scan across the ground
2. Measures the two-way travel time of each returning pulse → range to the surface
3. Combines range with the precisely known position and attitude of the aircraft (from GPS + inertial measurement unit) to compute the 3D position of each return

```{figure} ../figures/07_lidar_acquisition.png
---
width: 700px
alt: Diagram showing an aircraft with a scanning lidar system sweeping laser pulses across the ground to build a point cloud.
---
Airborne lidar acquisition geometry. The laser sweeps perpendicular to the flight direction at tens of thousands of pulses per second. The aircraft position and orientation are continuously tracked by on-board GPS and an inertial measurement unit. The result is a dense point cloud at sub-meter resolution. After Funning (GEO 147 lecture notes).
```

**Key specifications** for typical airborne lidar systems:
- Laser wavelength: 500–1000 nm (visible to near-infrared)
- Pulse rate: 10,000–100,000+ Hz
- Laser footprint on ground: 15–20 cm diameter
- Point density: 1–10+ points per m²
- Vertical accuracy: 5–15 cm
- Horizontal accuracy: 20–30 cm
- Flight altitude: 600–1,000 m above ground

---

## Point Clouds and the Bare-Earth Problem

The result of a lidar survey is a **point cloud** — an irregular collection of millions of 3D points representing reflections of the laser from every surface it encountered: ground, vegetation canopy, branches, buildings, cars.

Because the laser pulse is narrow but energetic, it can penetrate through gaps in a tree canopy and return discrete reflections from multiple surfaces along the same pulse — canopy top, intermediate branches, and ground. This produces a **full-waveform** or **discrete return** record for each pulse.

```{figure} ../figures/07_lidar_vegetation_filtering.png
---
width: 700px
alt: Two hillshaded DEMs of an Alaskan fault zone - the first return DEM shows noisy vegetation; the bare-earth DEM reveals clear fault features including offset stream channels and en echelon fractures.
---
First-return (top) vs. bare-earth (bottom) lidar DEM of a fault zone in Alaska that ruptured in 2001. The first-return DEM is dominated by vegetation noise; the bare-earth DEM reveals offset stream channels, en echelon surface fractures, and the complexity of the surface rupture at high resolution. After Funning (GEO 147 lecture notes).
```

**Vegetation filtering:**
- **First-return DEM** (choose maximum elevation in each cell): captures the top of the vegetation canopy — useful for forestry but obscures geology
- **Bare-earth DEM** (choose minimum elevation, or apply sophisticated ground-classification algorithms): retains only ground returns — the geologist's product

👉 The ability to see through vegetation and reveal the bare earth is lidar's most transformative capability for active tectonic mapping.

---

## OpenTopography and Data Access

The lidar revolution in active tectonics has been enabled by open data. **OpenTopography** (opentopography.org) aggregates freely available lidar datasets for the US and globally. The number of freely available US datasets grew from 20 in 2004 to more than 1,000 today. For California in particular, the USGS 3DEP program has delivered statewide lidar coverage at 1 m resolution.

---

## Lidar Reveals Hidden Fault History: Wallace Creek

Perhaps the most scientifically influential early application of fault-zone lidar was Zielke et al. (2010) at Wallace Creek on the Carrizo segment of the San Andreas Fault.

```{figure} ../figures/07_wallace_creek_lidar.png
---
width: 720px
alt: Lidar hillshade of Wallace Creek on the San Andreas Fault showing multiple generations of offset stream channels with 5, 10, 15, and larger meter offsets.
---
Lidar hillshade of Wallace Creek, Carrizo Plain, San Andreas Fault. The stream channel shows a characteristic double bend — right-lateral slip has offset the channel as it crosses the fault. Measuring the offset of multiple features along the fault revealed a population of offsets at ~5, ~10, ~15 m intervals. After Zielke et al. (2010); Funning (GEO 147 lecture notes).
```

At Wallace Creek, Zielke et al. measured hundreds of offset stream channels, ridge crests, and other features visible in the 1 m lidar DEM. They found that the offset distribution was not random — it clustered at approximately 5, 10, 15, 20, and 25 m. Their interpretation: these represent the cumulative offsets of 1, 2, 3, 4, and 5 past earthquakes, each contributing approximately 5 m of slip.

**The impact:** Prior to this work, the 1857 Fort Tejon earthquake on this segment was thought to have produced ~10 m of slip. The lidar data revealed the true slip was ~5 m — overturning decades of interpretation and halving the expected recurrence-interval slip. This is the power of high-resolution topographic data for paleoseismology.

---

# 3D Displacement from Point Clouds

---

## Before and After: The Differencing Approach

If pre-event and post-event lidar datasets exist for the same fault zone, the coseismic displacement field can potentially be recovered by comparing them. The simplest approach is **DEM differencing**: subtract the pre-event bare-earth DEM from the post-event DEM pixel by pixel.

```{figure} ../figures/07_el_mayor_differencing.png
---
width: 720px
alt: Pre- and post-event lidar DEMs of the El Mayor-Cucapah earthquake fault zone and the resulting vertical displacement field showing normal fault scarps and apparent strike-slip signals.
---
Lidar DEM differencing for the 2010 El Mayor-Cucapah M7.2 earthquake in Baja California. Pre-event lidar (left) and post-event lidar (center) differ by the coseismic displacement. The difference map (right) shows vertical offsets of ~1–2 m along normal fault segments, plus apparent stripy signals in topographically complex areas caused by horizontal strike-slip translation of irregular terrain. After Oskin et al. (2012); Funning (GEO 147 lecture notes).
```

**The strike-slip artifact problem:** Simple DEM differencing measures only the vertical component of displacement. If the fault also has a horizontal component — as most large earthquakes do — then topographic features are translated horizontally between the two surveys. When the pre-event DEM is subtracted from the post-event DEM, a horizontally-shifted ridge or valley appears as a false vertical signal. This is the characteristic **stripy artifact** seen in DEM differencing of strike-slip earthquakes.

---

## The ICP Algorithm: 3D Matching of Point Clouds

A more powerful approach matches the **shape** of the topography rather than just the elevation values. The **Iterative Closest Point (ICP) algorithm**, originally developed for computer vision, finds the 3D rigid-body transformation (translation + rotation) that best aligns two point clouds.

Applied to earthquake geodesy (Nissen et al. 2012, 2014):

1. Divide the fault zone into small overlapping windows
2. In each window, find the translation that minimizes the distance between corresponding points in the pre- and post-event point clouds
3. This translation is the 3D displacement vector at that location

Because ICP matches 3D shapes rather than 1D elevation values, it recovers all three components of displacement — east, north, and up — simultaneously.

```{figure} ../figures/07_icp_comparison.png
---
width: 720px
alt: Three-panel comparison of simple DEM differencing versus ICP matching for the Fukushima-Hamadori earthquake showing improved signal recovery with ICP.
---
Comparison of DEM differencing (left) vs. ICP matching (center) for the 2011 Fukushima-Hamadori earthquake in Japan. The ICP result is substantially cleaner — the stripy artifact is suppressed and the true fault offsets emerge clearly. Displacement profiles (right) show sharp vertical steps at the fault in the ICP result that are obscured by noise in the differencing result. After Nissen et al. (2014); Funning (GEO 147 lecture notes).
```

**Case studies:**

*El Mayor-Cucapah (2010, M7.2):* One of the first earthquakes with extensive pre-event lidar coverage (from the SCEC community fault mapping effort in 2005). Oskin et al. (2012) used DEM differencing to map the complex normal fault ruptures and to reveal a previously unmapped system of antithetic faults on both sides of the main rupture.

*Fukushima-Hamadori (2011, M6.7):* Nissen et al. (2014) demonstrated that ICP significantly outperformed DEM differencing, recovering clean displacement profiles across the fault even in areas where simple differencing was dominated by the strike-slip artifact.

*Kaikōura (2016, M7.8):* Diederichs et al. (2019) recovered a highly complex 3D displacement field across the multi-fault Kaikōura rupture, including the remarkable discovery of the **Papatea fault** — a ~10–12 m block-like uplift with almost no surrounding elastic deformation, unlike any previously observed fault behavior. The near-rigid uplift of this crustal block challenged standard elastic dislocation models and suggested a fundamentally different deformation mechanism on at least some fault segments.

---

## The Value of Pre-Event Lidar

The Southern California Earthquake Center recognized in 2005 that a pre-event lidar baseline was essential for future earthquake science. They funded coverage of the major southern California fault systems — San Andreas, San Jacinto, Elsinore, Garlock — specifically to enable this differencing approach when the next large earthquake occurred.

👉 **The lesson:** pre-event lidar is a scientific investment that pays off only when an earthquake happens, but the payoff — full 3D coseismic displacement at meter-scale resolution — is enormous. Building and maintaining pre-event baselines on active fault systems is now a recognized priority in earthquake science.

---

# Structure from Motion

---

## Terrestrial Lidar

Before introducing Structure from Motion it is worth noting that lidar is not exclusively airborne. **Terrestrial laser scanners (TLS)** are tripod-mounted lidar units that scan their surroundings at high resolution from a fixed position. They are used to:

- Monitor progressive erosion of rock outcrops or sea cliffs
- Track mass movement on hillslopes at risk of landslide
- Measure beach morphology change
- Study volcano flank deformation

One evocative application: **precariously balanced rocks** — large boulders teetering on narrow pedestals. The fact that they have not toppled constrains the maximum ground shaking at that location since the boulder came to rest. TLS provides the precise 3D geometry needed to compute the tipping acceleration, turning these natural objects into paleoseismic accelerometers.

---

## Structure from Motion (SfM)

**Structure from Motion** is a photogrammetric technique that reconstructs 3D geometry from a set of overlapping photographs taken from different positions — with no requirement to know the camera parameters in advance or to specify where each photo was taken.

SfM algorithms:
1. Detect distinctive features in each image (corners, edges, textures)
2. Match those features across all image pairs that share overlapping content
3. Simultaneously solve for camera positions and orientations AND 3D point positions — the "structure" and "motion" together
4. Produce a dense point cloud and optionally a textured 3D model

The key advantages over traditional photogrammetry are that SfM requires no specialized metric camera, no prior knowledge of camera positions, and works with consumer cameras and smartphones.

```{figure} ../figures/07_sfm_hayward_curb.png
---
width: 700px
alt: Structure from motion point clouds of an offset curb on the Hayward Fault in Fremont CA, showing 3mm of creep measured between two yearly surveys.
---
Structure from Motion applied to fault creep monitoring on the Hayward Fault, Fremont, CA (work of J. Swiatlowski, UC Riverside). A curb crosscut by the fault was photographed from many positions in January of successive years. ICP alignment of the resulting point clouds reveals ~3 mm of right-lateral creep accumulated in one year. The entire survey used a consumer digital camera. After Funning (GEO 147 lecture notes).
```

---

## SfM from Drones and Kite Platforms

SfM combined with low-cost aerial platforms has democratized high-resolution topographic mapping:

**Drones (UAVs):** Most commercial drones have built-in cameras and GPS. Flying a systematic grid pattern over a fault zone at low altitude produces hundreds of overlapping images that SfM can process into a sub-decimeter-resolution point cloud and orthoimage. This is now the standard rapid-response tool for documenting surface ruptures after earthquakes.

**Kite and balloon platforms:** Before the drone era, cameras were flown on helium balloons or kites on strings, photographing the ground on a timer. Simpler and more fragile than drones, but capable of similar results in suitable conditions.

**Practical advantages:**
- Cost: a few thousand dollars vs. ~$100,000+ for airborne lidar
- Deployment time: hours vs. weeks
- Resolution: comparable or better than early lidar in areas without dense vegetation
- Limitation: doesn't penetrate vegetation; affected by wind; limited range

👉 SfM from drones is now a standard part of earthquake field response — teams can be in the air within days of a major surface rupture, producing meter-scale or better topographic models before erosion and anthropogenic modification obscure the rupture trace.

---

# Connecting to Crustal Deformation

These topographic techniques extend our view of the earthquake cycle in time and space:

| Technique | Timescale | What it reveals |
|-----------|----------|----------------|
| Hillshaded DEM | Hundreds to thousands of years | Cumulative fault geomorphology: scarps, offsets, ridges |
| Stream offset measurements | Multiple earthquake cycles | Recurrence slip, average slip per event |
| Lidar bare-earth | Single event to Holocene | Sub-meter fault trace, individual rupture features |
| Pre/post lidar differencing | Single event | Full 3D coseismic displacement field |
| SfM / drone survey | Single event or ongoing | Near-field surface rupture geometry, fault creep |
| InSAR | Single event to years | Regional deformation field at cm precision |
| GNSS | Years to decades | Point velocities, interseismic loading, postseismic |

The power of combining these techniques is that they span from the millimeter-per-year creep measured by SfM on curbs, through the meter-scale coseismic offsets measured by lidar differencing and InSAR, to the kilometers of cumulative offset preserved in the landscape as offset channels and fault scarps.

---

# Summary

- A **digital elevation model (DEM)** is a gridded topographic dataset. Hillshading (artificial illumination) dramatically improves the visibility of subtle tectonic landforms including fault scarps, offset channels, pressure ridges, and sag ponds.

- **Stereophotogrammetry** exploits the distortion that topographic relief imparts to oblique images acquired from two different viewing angles. The parallax between corresponding features in the two images encodes their height. The base-to-height ratio controls stereo sensitivity; values of 0.3–1.0 are optimal.

- **Airborne lidar** generates dense point clouds by timing laser pulses reflected from the ground. Because the laser can penetrate vegetation and record multiple returns per pulse, bare-earth DEMs can be extracted that reveal fault features hidden by vegetation — transforming active fault mapping in forested and scrubland environments.

- **Lidar revolutionized paleoseismology** at sites like Wallace Creek, where the 1 m bare-earth DEM revealed a population of offset features at multiples of ~5 m, cutting the estimated 1857 earthquake slip in half and rewriting the earthquake history of the Carrizo segment.

- **Pre/post event lidar differencing** can recover the coseismic vertical displacement field but suffers from a strike-slip artifact when horizontal displacement translates topographic features between surveys. The **ICP algorithm** resolves this by matching the 3D shape of topographic windows to recover full 3D displacement vectors.

- **Structure from Motion (SfM)** is a photogrammetric technique that reconstructs 3D geometry from overlapping photographs without prior knowledge of camera positions or calibration. Combined with drones, it provides sub-decimeter topographic models of fault zones at a fraction of the cost of airborne lidar, and is now a standard tool for rapid earthquake field response.

- Together, these techniques extend the geodetic view of the earthquake cycle from the centimeters per year of interseismic GNSS, through the meters of coseismic slip measured by lidar and InSAR, to the tens of meters of cumulative offset preserved in geomorphic features over many earthquake cycles.

---

# Additional Resources

> **Data portal:** [OpenTopography](https://opentopography.org)  
> Open access to lidar and other high-resolution topographic datasets for the US and globally. The starting point for any fault-zone topographic study.

> **Research article:** [Near-field deformation from the El Mayor-Cucapah earthquake revealed by differential LIDAR](https://doi.org/10.1126/science.1213778)  
> Oskin et al. (2012). The landmark paper demonstrating 3D coseismic displacement from pre/post lidar differencing for the 2010 El Mayor-Cucapah earthquake.

> **Research article:** [Coseismic displacements of the 2010–2011 Canterbury earthquake sequence from airborne lidar](https://doi.org/10.1002/jgrf.20066)  
> Nissen et al. (2014). Demonstration of the ICP algorithm for 3D point cloud matching to recover clean coseismic displacement fields.

> **Research article:** [Earthquake science at high resolution: The 2016 Kaikōura, New Zealand, earthquake](https://doi.org/10.1785/0220180292)  
> Diederichs et al. (2019). Kaikōura case study including the Papatea fault block uplift — an observation that challenged standard elastic models.

> **Classic paper:** [Slip in the 1857 and earlier large earthquakes along the Carrizo Plain, San Andreas Fault](https://doi.org/10.1126/science.1182781)  
> Zielke et al. (2010). How lidar overturned decades of understanding of the 1857 Fort Tejon earthquake slip and recurrence history.

> **Software:** [Agisoft Metashape](https://www.agisoft.com)  
> The standard commercial software for Structure from Motion point cloud generation. Academic licenses available.

> **Software:** [OpenDroneMap](https://www.opendronemap.org)  
> Open-source alternative for SfM processing of drone imagery.

---

# Sources

- Funning, G. (n.d.). *GEO 147: Active Tectonics and Remote Sensing* — DEMs, Photogrammetry and Lidar lecture series (Parts 1–5). University of California, Riverside. With materials contributed by Ed Nissen and Barry Parsons.
- Fielding, E. J., Isacks, B. L., Barazangi, M., & Duncan, C. (1994). How flat is Tibet? *Geology*, 22(2), 163–167. https://doi.org/10.1130/0091-7613(1994)022<0163:HFIT>2.3.CO;2
- Zielke, O., Arrowsmith, J. R., Ludwig, L. G., & Akciz, S. O. (2010). Slip in the 1857 and earlier large earthquakes along the Carrizo Plain, San Andreas Fault. *Science*, 327(5969), 1119–1122. https://doi.org/10.1126/science.1182781
- Oskin, M. E., et al. (2012). Near-field deformation from the El Mayor–Cucapah earthquake revealed by differential LIDAR. *Science*, 335(6069), 702–705. https://doi.org/10.1126/science.1213778
- Nissen, E., et al. (2014). Coseismic fault zone deformation revealed with differential lidar: Examples from Japanese Mw ~7 intraplate earthquakes. *Earth and Planetary Science Letters*, 405, 244–256. https://doi.org/10.1016/j.epsl.2014.08.031
- Diederichs, A., et al. (2019). Unusual kinematics of the Papatea fault (2016 Kaikōura earthquake) suggest anelastic rupture. *Science Advances*, 5(10). https://doi.org/10.1126/sciadv.aax5703
