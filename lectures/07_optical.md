# Optical Satellite Imagery

## Purpose

Optical satellites have observed Earth's surface continuously since 1972. By comparing images acquired before and after a geological event — or by tracking the motion of surface features through time — we can measure deformation that other methods cannot easily see.

In this lecture, we will:

- define remote sensing and distinguish passive from active approaches
- explain how electromagnetic radiation propagates and why only certain wavelength windows reach the ground
- describe how optical satellites acquire multispectral images
- explain the difference between line-scanning and push-broom instruments
- distinguish free and commercial satellite missions and their trade-offs
- interpret false-color imagery and spectral indices
- understand why sun-synchronous orbits matter for time-series analysis
- identify how optical imagery is used to measure crustal deformation

---

# Remote Sensing: Some Definitions

## What Is Remote Sensing?

**Remote sensing** is the use of electromagnetic radiation — heat, light, or radio waves — to detect and measure the characteristics of a distant target. The platform can be on the ground, on an aircraft, or in space. In this course we focus almost entirely on **satellite** platforms.

Remote sensing methods divide into two fundamental categories:

**Passive remote sensing** relies on an external source of illumination — almost always the Sun — to illuminate the ground. The satellite detects reflected radiation. Optical imagery is passive.

**Active remote sensing** generates its own electromagnetic radiation, directs it at the target, and measures what comes back. Radar and lidar are active. InSAR, which we cover in the next lecture, is an active method.

```{figure} ../figures/07_passive_active.webp
---
name: Active vs. passive remote sensing
width: 760px
alt: Schematic comparing passive and active remote sensing. In passive, sunlight reflects off the ground to the sensor. In active, the sensor emits its own pulse.
---
The difference between four major types of remote sensors: passive sensors (multispectral and hyperspectral) do not emit radiation themselves, but active sensors (LiDAR and radar) do. The passive modes are distinguished by the number of bands across which they measure radiance, whereas the active modes are distinguished by the wavelength of the radiation which they emit. Image: Astronaut photograph AS17-14822727 courtesy NASA Johnson Space Center Gateway to Astronaut Photography of Earth. 
```

> **Why passive matters for tectonics:** The first widely available satellite imagery that revealed the continent-scale network of active faults was passive optical data. The 1975 cover of *Science* magazine showed a mosaic of early Landsat images across Asia, with fault traces clearly visible in the landscape for the first time at regional scale.

---

# Electromagnetic Radiation

## Waves and Propagation

Electromagnetic energy propagates as waves — coupled oscillating electric and magnetic fields, perpendicular to each other and to the direction of travel. Key properties:

- **Wavelength** $\lambda$: distance between successive peaks (metres, or more practically µm and nm for optical)
- **Frequency** $f$: oscillations per second (Hz)
- **Speed**: all EM radiation travels at the speed of light $c$ in a vacuum

$$
c = f \lambda \qquad (c \approx 3 \times 10^8 \text{ m/s})
$$

EM radiation shows the classic wave behaviours: refraction, diffraction, and interference. The Young's two-slit experiment demonstrated light's wave character and directly underpins how we understand satellite imaging optics.

---

## The Electromagnetic Spectrum

The electromagnetic spectrum spans an enormous range of wavelengths, from gamma rays ($<10^{-12}$ m) to radio waves ($>10^{-1}$ m). Optical remote sensing operates in a narrow slice: the **visible** ($\sim$0.4–0.7 µm) and **infrared** ($\sim$0.7–14 µm) portions.

```{figure} ../figures/07_em_spectrum.svg
---
name: Electromagnetic spectrum
width: 800px
alt: The electromagnetic spectrum from gamma rays to radio waves, with the optical and infrared portion highlighted.
---
The electromagnetic spectrum. Optical satellites exploit the visible and infrared portions. Radar systems operate at centimetre to metre wavelengths.
```

---

## Solar Radiation

Not all wavelengths reach the ground. The atmosphere is transparent in some ranges and absorbs strongly in others. Gases including ozone (O₃), water vapour (H₂O), carbon dioxide (CO₂), and oxygen (O₂) each absorb at characteristic wavelength bands.

```{figure} ../figures/07_solar_radiation.jpg
---
name: Solar Radiaiton
width: 600px
alt: Spectrum of solar radiation above the atmosphere and at sea level. 
---
The spectrum of radiation from the sun that reaches the top of the Earth’s atmosphere (yellow) and at sea level (red). The difference between the two indicates the light that is absorbed by components of the atmosphere. Image from Wikipedia under the CC BY-SA 3.0. Minor edits were made to remove additional labels.
```

---

## Atmospheric Windows

The result is a set of **atmospheric windows** — wavelength ranges where transmission is high and satellites can actually observe the surface:

| Window | Wavelength | Key absorbers (outside window) |
|---|---|---|
| Visible | 0.4–0.7 µm | O₃ absorbs UV at <0.3 µm |
| Near infrared (NIR) | 0.7–1.0 µm | — relatively transparent |
| Short-wave infrared (SWIR) | 1.5–1.8 µm, 2.0–2.5 µm | H₂O absorbs between these |
| Thermal infrared (TIR) | 8–14 µm | CO₂ and H₂O close gaps |
| Microwave / radar | 1 mm–1 m | transparent (used by InSAR) |

Satellite spectral bands are designed to sit within these windows. The specific gaps in the Landsat band table are not arbitrary — they correspond to atmospheric absorption features where observations are impossible regardless of detector quality.

```{figure} ../figures/07_atmospheric_windows.jpg
---
name: Atmospheric windows
width: 820px
alt: Plot of atmospheric transmittance versus wavelength showing transparent windows and absorption features from O3, H2O, CO2 and O2.
---
Atmospheric transmittance as a function of wavelength. Satellite instruments are designed to operate within the transparent windows. Absorption by ozone, water vapour, and CO₂ defines where the windows open and close.
```

> **The ozone layer** absorbs almost all ultraviolet radiation below 0.3 µm — protecting life from ionising radiation but also preventing satellite observations at those wavelengths. The ozone absorption feature at ~9.6 µm also partially limits the thermal infrared window.

---

# Imaging Earth From Space

## The Landsat Record

The Landsat mission is the longest-running civilian Earth observation programme. It began in 1972 with the launch of ERTS-1 (Earth Resources Technology Satellite 1), later renamed Landsat 1, and has continued through Landsat 9 (launched 2021).

This continuity is scientifically invaluable. A 50-year archive of the same locations, acquired with consistent geometry and calibration, allows us to detect slow changes in land cover, glacier extent, river migration — and fault creep.

Each generation carried a progressively more capable instrument: the Multispectral Scanner (MSS), Thematic Mapper (TM), Enhanced Thematic Mapper Plus (ETM+), and — on the current satellites — the Operational Land Imager (OLI) paired with the Thermal Infrared Sensor (TIRS).

| Satellites | Instrument | Years active | Key capability |
|---|---|---|---|
| Landsat 1–3 | MSS | 1972–1983 | 4 bands (VIS + NIR), 80 m |
| Landsat 4–5 | TM | 1982–2013 | 7 bands, 30 m; Landsat 5 lasted 29 years |
| Landsat 7 | ETM+ | 1999–present | Added 15 m panchromatic |
| Landsat 8–9 | OLI + TIRS | 2013–present | 11 bands, push-broom, 30 m / 15 m pan |

Landsat 5 vastly exceeded its design life, remaining operational for 29 years. In that time, Landsat 6 was launched and failed to reach orbit. Overlapping launch dates throughout the programme ensured there was no gap in the archive.

```{figure} ../figures/07_landsat_timeline.png
---
name: Landsat missions
width: 800px
alt: This is an image depicting the timeline of the Landsat program, from Landsat 1, which launched in 1972, through Landsat 9, currently being built. The hashed lines for Landsats 7-9 indicate the uncertain lifespan of the satellites. Landsat 6 failed to reach orbit on launch.
---
The Landsat mission timeline. Overlapping launches ensured continuity of the archive. Landsat 5 vastly exceeded its design life, operating for 29 years.  The hashed lines for Landsats 7-9 indicate the uncertain lifespan of the satellites. Landsat 6 failed to reach orbit on launch.
```

---

## How Do Optical Satellites Acquire Images?

### Line Scanning

The first seven Landsats used a **line-scanning** approach: a rotating mirror sweeps reflected light from the ground across a set of detectors. The mirror scans perpendicular to the flight direction while the satellite moves forward, building up an image one line at a time.

The size of each detector controls spatial resolution. Larger detectors collect more photons but blur fine detail; smaller detectors improve resolution but require more light or a narrower spectral band. This is why Landsat 7's thermal band (band 6) has 60 m pixels while its panchromatic band (band 8) achieves 15 m — the detectors for the two bands are physically different sizes.

### Push Broom

Modern satellites — including Landsat 8/9, Sentinel-2, SPOT 6/7, and Pleiades — use a **push-broom** design. A linear array of detectors, oriented perpendicular to the flight track, images an entire row of pixels simultaneously as the satellite moves forward. There are no moving mirrors.

Push-broom instruments are more reliable (fewer mechanical parts), more sensitive (each detector stares at the ground longer), and better suited to very high resolution. The transition from line-scan to push-broom was driven primarily by falling detector costs.

```{figure} ../figures/07_pushbroom.png
---
name: Pushbroom vs. whiskbroom
width: 760px
alt: Schematic comparison of line-scanning and push-broom imaging modes.
---
Whiskbroom-type imaging instrument and pushbroom-type imaging instrument.
```

---

# Spectral Bands and Color

## How We See Color

The human eye is itself a multispectral sensor. The retina contains two types of photoreceptors:

- **Rods** — panchromatic sensors that detect light intensity but not color. They dominate in low-light conditions, which is why we cannot distinguish colors in the dark.
- **Cones** — three types, each sensitive to a different wavelength range (broadly: blue, green, red). Their combined signals create the perception of color.

The visual system in the brain interprets three numbers — the outputs of the three cone types — and constructs the full range of colors we perceive. This is why **any image display only needs three channels** (red, green, blue) to reproduce all visible colors.

Satellite sensors extend this principle: instead of three bands restricted to visible wavelengths, they record many bands across a much wider spectrum.

---

## Landsat 8 Spectral Bands

For Landsat 8's OLI instrument:

| Band | Name | Wavelength | Spatial res. | Primary use |
|---|---|---|---|---|
| 1 | Coastal / aerosol | 430–450 nm | 30 m | Aerosols, coastal water |
| 2 | Blue | 450–510 nm | 30 m | Water depth, atmosphere |
| 3 | Green | 530–590 nm | 30 m | Vegetation, water |
| 4 | Red | 640–670 nm | 30 m | Vegetation discrimination |
| 5 | NIR | 850–880 nm | 30 m | Vegetation, biomass |
| 6 | SWIR-1 | 1570–1650 nm | 30 m | Soil moisture, geology |
| 7 | SWIR-2 | 2110–2290 nm | 30 m | Clay minerals, geology |
| 8 | Panchromatic | 500–680 nm | **15 m** | High-resolution detail |
| 9 | Cirrus | 1360–1380 nm | 30 m | High cloud detection |
| 10–11 | Thermal (TIRS) | 10.6–12.5 µm | 100 m | Surface temperature |

Note how bands 6 and 7 (SWIR) sit within atmospheric windows between water vapour absorption features. The cirrus band (9) is placed inside a water vapour absorption feature — clouds at high altitude are above most of the water vapour, so they appear bright in this band while the surface is dark.

```{figure} ../figures/07_landsat_bands.png
---
name: Landsat Bands
width: 800px
alt: Landsat spectral bands superimposed on the atmospheric windows.
---
Landsat spectral band graphic showing the evolution of Landsat's spectral bands from the first generation Multispectral Scanner System (MSS) to Landsat 9's Operational Land Imager 2 (OLI-2).
```
---

## False-Colour Imagery

Because our display systems show only red, green, and blue, we assign satellite bands to these three display colors to visualise non-visible information. The choice of which band goes to which display color is called a **band combination** or **composite**. There is no single correct choice — the right combination depends on what you are trying to see.

Note that band numbers are instrument-dependent: NIR is band 4 on Landsat 7, band 5 on Landsat 8/9, and band 8 on Sentinel-2. It is clearer to describe composites by band name rather than number.

**True color** assigns red→red, green→green, blue→blue. The result looks approximately as your eye would see it from space — intuitive, but limited to what human vision can already detect.

**Colour Infrared (CIR)** assigns NIR→red, red→green, green→blue:

- **Vegetation** appears bright red — plants reflect strongly in NIR while absorbing red for photosynthesis
- **Water** appears very dark — strong NIR absorption
- **Built-up areas** appear cyan or purplish — broad visible reflectance, weak NIR
- **Bare rock and soil** varies with mineralogy

**Geology composite** assigns SWIR-2→red, SWIR-1→green, red→blue. Clay minerals, iron oxides, and hydrothermal alteration zones appear in distinct colors invisible in true color — useful for mapping lithology and fault zones through varied rock types.

```{figure} ../figures/07_bands.png
---
name: Common Landsat bands
width: 800px
alt: Common Landsat false color combinations showing how different band assignments reveal different surface properties.
---
A selection of common Landsat band combinations and what each reveals about the surface.
```

> **Prediction:** In a CIR image, what color would fresh lava appear, and why?

---

## The Normalized Difference Vegetation Index (NDVI)

Our eyes perceive a leaf as green because wavelengths in the green region of the spectrum are reflected by pigments in the leaf, while the other visible wavelengths are absorbed. In addition, the components in plants reflect, transmit, and absorb different portions of the near-infrared radiation that we cannot see.

```{figure} ../figures/07_leaf_absorption.webp
---
name: Leaf absorption
width: 760px
alt: Absorbed and reflected components of the electromagnetic spectrum for a healthy leaf.
---
Absorbed and reflected components of the electromagnetic spectrum for a healthy leaf.
```

Reflected near-infrared radiation can be sensed by satellites, allowing scientists to study vegetation from space. Healthy vegetation absorbs blue- and red-light energy to fuel photosynthesis and create chlorophyll. A plant with more chlorophyll will reflect more near-infrared energy than an unhealthy plant. Thus, analyzing a plants spectrum of both absorption and reflection in visible and in infrared wavelengths can provide information about the plants' health and productivity.

```{figure} ../figures/07_red_edge.jpg
---
name: Red Edge
width: 600px
alt: Reflectance about vegetation across various wavelengths of light, ranging from visible light to NIR band
---
Reflectance about vegetation across various wavelengths of light, ranging from visible light to NIR band: Vital vegetation (green line) shows a rapid increase in reflectance at the RE band, but dry vegetation (brown line) does a relatively low rise in the RE band.
```

The spectral contrast between red absorption and NIR reflectance by vegetation can be quantified as the **NDVI**:

$$
\text{NDVI} = \frac{\rho_{\text{NIR}} - \rho_{\text{red}}}{\rho_{\text{NIR}} + \rho_{\text{red}}}
$$

- Dense green vegetation: NDVI → 1
- Bare rock, concrete, soil: NDVI → 0
- Water: NDVI < 0

NDVI is useful in geology wherever vegetation follows geological boundaries — fault traces damming groundwater, soil chemistry controlling plant communities, or volcanic heat stimulating anomalous growth.


---

```{iframe} http://localhost:3100/spectral-widget-c74c3d379e9446ba3c15f2a2d4f90e45.html
:width: 100%
:title: True color, false color, and NDVI
```

---

# Satellite Missions

## Sentinel-2

Sentinel-2 is a two-satellite constellation operated by the European Space Agency. The two satellites (2A and 2B) are phased six days apart, providing combined revisit times of five days at the equator and more frequently at higher latitudes.

Key specifications:
- **13 spectral bands** from visible through SWIR, including several narrow red-edge bands
- **10 m** resolution in visible and NIR bands (better than Landsat)
- **290 km swath** (wider than Landsat or SPOT)
- **Freely available** through the Copernicus Data Space

Sentinel-2 does not carry a thermal band, but its higher spatial resolution and more frequent revisit make it particularly useful for tracking surface changes and pixel-tracking deformation.

```{figure} ../figures/07_sentinel2_landsat_comparison.png
---
width: 800px
alt: Spectral band comparison between Sentinel-2 MSI and Landsat 8 OLI showing band positions and widths.
---
Sentinel-2 and Landsat 8 spectral band comparison. Sentinel-2 achieves 10 m resolution in its visible and NIR bands and adds narrow red-edge bands for vegetation discrimination.
```

---

## SPOT

The SPOT (Satellite Pour l'Observation de la Terre) series is a French constellation now on its sixth and seventh satellites. A key capability distinguishing SPOT is its **steerable cameras**: the instrument can tilt up to 30° from nadir, enabling:

- **Rapid revisit** of a specific target without waiting for an overhead pass
- **Along-track and across-track stereo** for generating digital elevation models

SPOT's spatial resolution has improved to **6 m** multispectral and **1.5 m** panchromatic on SPOT 6/7, with a 60 km swath.

---

## Very High Resolution: WorldView and Pleiades

Commercial satellites from Maxar (WorldView series) and Airbus (Pleiades) achieve sub-metre panchromatic resolution:

| Mission | Pan resolution | MS resolution | Swath | Operator |
|---|---:|---:|---:|---|
| WorldView-3 | 0.31 m | 1.24 m | 13.1 km | Maxar |
| Pleiades 1A/1B | 0.50 m | 2.0 m | 20 km | Airbus |

At these resolutions, individual buildings, surface rupture features, and offset stream channels become visible. Pleiades can acquire **tri-stereo** imagery, enabling elevation models in complex terrain.

> **These data are not freely available.** Access typically requires a purchase or research agreement.

### The Kokoxili Earthquake — what VHR imagery can see

A landmark demonstration of VHR imagery for tectonics came from IKONOS data of the 2001 M7.9 Kokoxili earthquake on the Kunlun fault, Tibet (Klinger et al., 2005). At 1 m resolution, individual offset stream channels and terraced risers were visible. By sliding pre- and post-earthquake image tiles relative to each other, Klinger et al. could measure offset at each point along the ~400 km rupture, producing the first high-resolution coseismic slip distribution derived from optical imagery.

They also documented a pull-apart extensional structure at a bend in the fault — something identifiable only because the resolution was sufficient to see individual rupture strands.

```{figure} ../figures/07_vhr_kokoxili.png
---
width: 800px
alt: IKONOS imagery of the Kokoxili earthquake rupture showing offset stream channels and a pull-apart structure.
---
IKONOS imagery of the 2001 Kokoxili earthquake rupture on the Kunlun fault, Tibet (Klinger et al., 2005). At 1 m resolution, offset stream channels and a pull-apart extensional structure are visible. Sliding image tiles to re-align features yields slip estimates along the rupture.
```

---

## Planet

Planet Labs operates the **PlanetScope** constellation of over 130 CubeSats, providing **daily global coverage** at 3–5 m resolution in four visible/NIR bands. Individually modest, but collectively unmatched for temporal frequency.

Planet imagery was critical during the 2019 Ridgecrest, California earthquake sequence: images were acquired between the M6.4 and M7.1 mainshocks, allowing scientists to separate the surface ruptures produced by each event — something no other operational satellite could have provided at that moment.

---

# Satellite Orbits

## Orbital Mechanics

Satellites orbit Earth on elliptical paths. For imaging satellites the orbits are nearly circular, at altitudes of roughly 500–800 km. The orbital period follows from Newton's laws:

$$
T = 2\pi\sqrt{\frac{r^3}{GM_\oplus}}
$$

where $r$ is the orbital radius, $G$ is the gravitational constant, and $M_\oplus$ is Earth's mass.

| Altitude | Period | Examples |
|---|---|---|
| ~400 km | ~92 min | International Space Station |
| ~700 km | ~100 min | Landsat, Sentinel-2 |
| ~36,000 km | ~24 h | Geostationary (weather satellites) |

At geostationary altitude, the orbital period matches Earth's rotation: the satellite hovers indefinitely above the same equatorial point. This is ideal for weather satellites and communications but impractical for high-resolution imaging — at 36,000 km, achieving 10 m resolution would require an impossibly large aperture.

---

## Sun-Synchronous Orbits

For time-series analysis of surface change, consistent illumination is essential. If a satellite imaged the same location at different times of day, shadows from topography would shift with solar angle, making it impossible to distinguish real surface change from illumination effects.

The solution is a **sun-synchronous orbit**: the orbital plane precesses westward at the same rate Earth orbits the Sun (~1°/day eastward), so the satellite crosses every latitude at the same local solar time on every pass.

This precession exploits the torque exerted by Earth's equatorial bulge on a slightly inclined polar orbit. By choosing altitude and inclination carefully, the precession rate can be set to exactly match Earth's orbital motion.

For Landsat:
- **16-day repeat cycle** (233 orbits before the ground track repeats)
- **~10:00–10:30 AM** local solar time at every latitude
- Consistent illumination geometry across the entire 50-year archive

> Sun-synchronicity is why you can meaningfully compare a Landsat image from 1990 with one from today: the illumination angle is nearly identical.

```{figure} ../figures/07_sun_synchronous_orbit.png
---
width: 760px
alt: Diagram of a sun-synchronous polar orbit showing the orbital plane rotating to keep pace with Earth's motion around the Sun.
---
A sun-synchronous orbit precesses at ~1°/day westward, matching Earth's orbital motion around the Sun. The satellite always crosses a given latitude at the same local solar time, keeping illumination consistent throughout the year.
```

---

# Optical Imagery and Crustal Deformation

## What Can Optical Imagery Measure?

Optical imagery measures the **position of surface features**. If the same feature can be identified in two images acquired at different times, its displacement can be estimated.

Two main approaches:

**1. Visual mapping**
At VHR, coseismic surface ruptures, offset stream channels, displaced fence lines, and landslide scarps can be identified and measured directly — as in the Kokoxili example above.

**2. Pixel tracking (sub-pixel correlation)**
Cross-correlating two images at the sub-pixel level yields a displacement field across the entire scene — not just at identifiable features. This works best when:
- the surface has stable texture (rocks, bare ground, crops in a consistent state)
- the two images have similar viewing geometry and illumination
- deformation signals exceed the noise floor (~1/10 pixel)

For Sentinel-2 at 10 m resolution, this corresponds to sensitivity of roughly **1 m** of surface displacement.

---

## Why Optical Complements InSAR for Strike-Slip Faults

InSAR measures displacement in the **satellite line-of-sight (LOS)** direction — a mix of vertical and horizontal motion projected onto the look vector. For Sentinel-1, the look direction is ~35–40° from vertical and approximately perpendicular to the along-track direction.

For a **strike-slip fault** trending parallel to the satellite track — such as the Hayward or San Andreas fault — fault-parallel horizontal motion is nearly perpendicular to the LOS. InSAR is largely insensitive to it:

$$
\text{InSAR sensitivity to strike-slip} \approx \sin(\delta)\sin(\alpha - \phi)
$$

where $\delta$ is the look angle from vertical, $\alpha$ is the look azimuth, and $\phi$ is the fault strike. When $\alpha \approx \phi$, sensitivity approaches zero.

Optical pixel tracking measures displacement in **both range and azimuth directions**. The azimuth direction is approximately along-track — and therefore **parallel to a NW-trending fault**. This is precisely the component InSAR misses.

> **This is why optical pixel tracking is the method of choice for measuring Hayward fault creep from space.** The ~5 mm/yr of surface creep on the Hayward fault is essentially invisible to InSAR but detectable in Sentinel-2 azimuth offsets accumulated over several years.

```{figure} ../figures/07_insar_vs_optical_geometry.png
---
width: 820px
alt: Diagram comparing InSAR line-of-sight sensitivity and optical azimuth sensitivity for a strike-slip fault.
---
InSAR LOS is nearly perpendicular to fault-parallel motion on a NW-trending strike-slip fault. Optical pixel tracking in the image azimuth direction is sensitive to exactly this component.
```

---

# Summary

- **Remote sensing** uses electromagnetic radiation to characterise distant targets. Optical imagery is **passive** — it detects reflected sunlight.
- The atmosphere is transparent only in certain **spectral windows**; satellite bands are designed to sit within these windows. Ozone, water vapour, and CO₂ define where the windows open and close.
- Early Landsat satellites used **line-scanning** with a rotating mirror. Modern satellites use **push-broom** linear detector arrays — more reliable and more sensitive.
- **False-color composites** assign non-visible bands to display colors, revealing features the eye cannot see. **NDVI** exploits the contrast between plant red-absorption and NIR-reflectance to map vegetation and can reveal fault-controlled groundwater anomalies.
- **Sun-synchronous orbits** ensure consistent illumination across a multi-decade archive, essential for time-series analysis.
- Optical satellites range from Landsat/Sentinel-2 at 10–30 m and free, to WorldView/Pleiades at <1 m and commercial. Planet provides daily coverage at 3–5 m.
- **Pixel tracking** extends optical imagery to displacement measurement. For NW-trending strike-slip faults, optical azimuth offsets capture fault-parallel motion that InSAR cannot.

> In the next lecture we turn to InSAR — a fundamentally different approach that is highly sensitive to vertical and fault-normal motion but blind to the fault-parallel component that optical imagery measures well.

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

> **Paper:** Klinger, Y., et al. (2005). High-resolution satellite imagery mapping of the surface rupture and slip distribution of the Mw ~7.8, November 14, 2001 Kokoxili earthquake (Kunlun fault, northern Tibet, China). *BSSA*, 95(5), 1970–1987.

> **Tool:** [Copernicus Data Space Ecosystem](https://dataspace.copernicus.eu/)  
> Free access to the complete Sentinel-2 archive. Registration required.

> **Tool:** [USGS EarthExplorer](https://earthexplorer.usgs.gov/)  
> Download the full Landsat archive. Search by location, date, and cloud cover.

> **Paper:** Leprince, S., et al. (2007). Automatic and precise orthorectification, coregistration, and subpixel correlation of satellite images, application to ground deformation measurements. *IEEE TGRS*, 45(6), 1529–1558.  
> The foundational paper for the COSI-Corr pixel-tracking method.
