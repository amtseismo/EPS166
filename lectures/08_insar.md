# Measuring Deformation from Space: InSAR

## Purpose

Synthetic aperture radar interferometry — InSAR — lets us measure surface deformation across entire fault systems at millimeter precision from a satellite hundreds of kilometers away. It is the most spatially dense geodetic technique available for studying earthquakes, volcanoes, landslides, and subsidence, and it has transformed how we image the deformation field of crustal processes.

In this lecture, we will:

- understand how synthetic aperture radar (SAR) images the ground using microwaves
- learn how interferometry converts two SAR images into a map of surface displacement
- interpret interference fringes in terms of line-of-sight displacement
- recognize the sources of noise that limit InSAR — atmosphere and decorrelation
- see how InSAR is used to map topography, with SRTM as the canonical example
- connect InSAR deformation maps to the elastic dislocation models we will use in the inversion lecture

---

# Synthetic Aperture Radar

SAR uses a fundamentally different part of the electromagnetic spectrum from optical satellites. Instead of detecting sunlight reflected from the ground — passive remote sensing — SAR is an **active** technique: the satellite emits its own pulses of microwave radiation and records what bounces back.

The relevant wavelengths are **centimeters to tens of centimeters** — the microwave band. Two important civilian SAR bands:

| Band | Wavelength | Example satellites |
|------|-----------|-------------------|
| C-band | ~5–6 cm | ERS-1/2, Sentinel-1, Radarsat |
| L-band | ~24 cm | ALOS-2, NISAR (upcoming) |
| X-band | ~3 cm | TerraSAR-X, COSMO-SkyMed |

Because SAR generates its own illumination, it can image **at night** and **through clouds** — a major operational advantage over optical satellites, especially at high latitudes or in persistently cloudy regions.

---

## How Radar Works

The basic setup:

1. The satellite antenna emits a **pulse** of microwave radiation toward the ground
2. The pulse illuminates a target area and is **backscattered** back toward the satellite
3. The satellite records both the **amplitude** and the **phase** of the returning signal
4. Range (distance) to the target is determined from the two-way travel time of the pulse

SAR satellites fly in a **side-looking** geometry — the antenna points obliquely to the side of the flight direction rather than straight down. This is essential: a nadir-pointing radar would illuminate the ground like a mirror and most energy would scatter away from the satellite.

```{figure} ../figures/08_sar_geometry.png
---
name: SAR geometry
width: 700px
alt: Diagram showing the ERS-1 satellite, its 10-meter antenna, and the side-looking imaging geometry illuminating a swath about 100 km wide.
---
ERS-1 imaging geometry. The satellite flies at ~780 km altitude at ~7 km/s. The radar antenna (10 m long) points obliquely to the right of the flight direction, illuminating a swath roughly 100 km wide. The pulse rate is ~1,600 pulses/second. After Funning (GEO 147 lecture notes).
```

---

## The Synthetic Aperture: How We Get Resolution

The raw illuminated footprint from a single pulse is roughly **100 km × 5 km** — far too coarse to be useful. The "synthetic aperture" processing trick improves this dramatically.

Because the satellite is moving at ~7 km/s and firing pulses at ~1,600 Hz, any given point on the ground is illuminated by **dozens of separate radar pulses** from different positions along the orbit. If we combine all these returns coherently — treating the collection of imaging positions as if they were a single very long antenna — we synthesize an effective aperture of **~5 km** instead of the physical 10 m antenna.

Since resolution scales inversely with aperture length:

$$
\delta_{az} \propto \frac{1}{L_{aperture}}
$$

a 5 km synthetic aperture produces a ground resolution of **~20 meters** — 500× better than the raw beam.

👉 The longer the synthetic aperture, the better the azimuth resolution. This is why SAR satellites can produce high-resolution imagery despite having small physical antennas.

---

## What SAR Amplitude Tells Us

SAR amplitude images look different from optical images — they encode the **roughness and slope** of the surface, not its color or composition.

**Bright backscatter** from:
- Slopes facing toward the satellite
- Rough surfaces (rocks, buildings) that scatter in all directions
- Vegetation canopies (trees, shrubs) at short wavelengths

**Dark backscatter** from:
- Slopes facing away from the satellite (shadowing)
- Smooth surfaces (calm water, flat lava flows) that act like mirrors and deflect the signal away

```{figure} ../figures/08_sar_kilauea.png
---
name: SAR Kilauea
width: 700px
alt: SAR amplitude image of Kilauea caldera in Hawaii showing bright crater walls on the east side, dark shadowed walls on the west, and bright patches of tree stands.
---
SAR amplitude image of Kīlauea caldera, Hawaii. The satellite flew south-to-north with the radar looking right (east). Crater walls facing the satellite (east-facing slopes) are bright; west-facing walls are shadowed. Bright patches in the caldera floor are tree stands with high roughness; darker dendritic patterns are smooth sediment-filled stream channels. After Funning (GEO 147 lecture notes).
```

---

## Why SAR Is Particularly Valuable

- **All-weather imaging** — microwaves pass through clouds unimpeded
- **Day and night** — no dependence on sunlight
- **Sensitive to surface roughness and slope** — complementary to optical data
- **Planetary applications** — Venus was mapped by the Magellan probe in the early 1990s using SAR (its permanent cloud cover makes optical imaging impossible); Titan (Saturn's moon) was mapped by Cassini's SAR instrument

---

# InSAR: The Basic Concept

---

## From Amplitude to Phase

SAR imaging uses the **amplitude** of the backscattered signal. **InSAR** — interferometric SAR — uses the **phase**.

Phase is the position within the wave cycle at the time it arrives back at the satellite. It encodes the **distance** between the satellite and the ground:

$$
\phi = \frac{4\pi}{\lambda} \cdot r
$$

where $\lambda$ is the radar wavelength and $r$ is the range (distance to the ground). A single SAR image contains phase information, but that phase is dominated by the unknown scattering characteristics of each pixel — it looks essentially random.

The key insight: **if we take the phase difference between two SAR images of the same area acquired at different times, the random scattering term cancels out** — so long as the ground didn't change between the two acquisitions. What remains is a map of how the range changed between the two passes.

$$
\Delta\phi = \phi_2 - \phi_1 = \frac{4\pi}{\lambda}\Delta r + \phi_{topo} + \phi_{atm} + \phi_{noise}
$$

If we correct for topography and satellite position, $\Delta\phi$ tells us how much the ground moved toward or away from the satellite.

---

## Making an Interferogram

The process:

1. **Acquire two SAR images** of the same area from approximately the same orbital position, with an event of interest (earthquake, volcanic inflation, etc.) between them
2. **Co-register** the two images using the amplitude data — align them to sub-pixel accuracy
3. **Difference the phase** of the two images pixel by pixel
4. **Remove topographic phase** using a digital elevation model (SRTM is the standard choice)
5. **Remove orbital phase** using precise satellite ephemeris
6. The result is an **interferogram** — a map of phase difference that encodes surface displacement

```{figure} ../figures/08_izmit_interferogram.png
---
name: Izmit interferogram
width: 700px
alt: InSAR interferogram of the 1999 Izmit M7.4 earthquake showing colored interference fringes across the North Anatolian Fault.
---
ERS interferogram of the 1999 Izmit (M7.4) earthquake on the North Anatolian Fault, Turkey. Left: SAR amplitude image. Right: interferogram showing the surface deformation field. Each full color cycle (blue→yellow→red) represents 2.8 cm of line-of-sight displacement toward the satellite. After Funning (GEO 147 lecture notes).
```

---

## Reading an Interferogram

Each **fringe** — one complete color cycle, typically displayed blue→yellow→red — represents **half a radar wavelength** of line-of-sight (LOS) displacement. For C-band (λ ≈ 5.6 cm):

$$
\Delta r_{fringe} = \frac{\lambda}{2} = 2.8 \text{ cm}
$$

**Convention for counting fringes:**

1. Choose a reference area far from the deformation — assume it didn't move (zero displacement)
2. Count color cycles moving toward the deformation center
3. Each cycle = 2.8 cm of range change (toward or away from satellite, depending on fringe direction)

```{figure} ../figures/08_fringe_counting.png
---
name: Fringe counting
width: 600px
alt: Schematic diagram showing how to count fringes and estimate displacement from an interferogram.
---
Fringe counting: moving inward from the reference area, each blue→yellow→red cycle = 28 mm of range decrease (ground moving toward satellite). Ten fringes = 28 cm of range change. The fringe density increases toward the fault, reflecting the gradient of displacement.
```

> **Question:** The Izmit interferogram shows ~20 fringes on each side of the fault. What is the total range change across the fault, and how does it compare to the expected coseismic offset for an M7.4 earthquake?

---

# Interpreting InSAR Deformation Signals

---

## Line-of-Sight Geometry

InSAR measures displacement in the **line-of-sight (LOS)** direction — the direction from the ground to the satellite. This is neither purely vertical nor purely horizontal.

The LOS direction depends on:
- **Incidence angle** ($\theta_i$): angle between the radar beam and vertical, typically 20°–45°
- **Heading**: the satellite flight direction (ascending = roughly northward, descending = roughly southward)

For a typical right-looking geometry:

$$
\Delta LOS = -\Delta u_E \sin\theta_i \cos\alpha - \Delta u_N \sin\theta_i \sin\alpha + \Delta u_U \cos\theta_i
$$

where $\Delta u_E$, $\Delta u_N$, $\Delta u_U$ are east, north, and up displacements and $\alpha$ is the satellite heading angle.

👉 InSAR is most sensitive to **vertical displacement** and **east-west horizontal displacement**. It is relatively insensitive to north-south displacement (because satellites fly roughly north-south and the north-south sensitivity is small).

---

## Ascending and Descending Tracks

SAR satellites acquire data on both **ascending** (south-to-north) and **descending** (north-to-south) orbital passes. Because the LOS direction differs between the two:

- **Ascending**: satellite looks roughly west → sensitive to eastward and upward motion
- **Descending**: satellite looks roughly east → sensitive to westward and upward motion

Combining ascending and descending interferograms allows partial decomposition of 3D displacement. For a purely strike-slip earthquake, one track may show large signal while the other shows little — using both together helps determine whether displacement was horizontal or vertical.

```{figure} ../figures/08_asc_desc.png
---
name: Ascending descending geometry
width: 700px
alt: Diagram comparing ascending and descending LOS sensitivity directions for a right-looking SAR satellite.
---
Ascending vs. descending LOS geometry. The different viewing angles mean the two tracks sample different components of the 3D displacement field. Combining them constrains both horizontal and vertical motion.
```

---

## Earthquake Deformation: A Surface-Rupturing Strike-Slip Fault

The Izmit interferogram is a textbook example of a large strike-slip earthquake recorded by InSAR.

```{figure} ../figures/08_izmit_full.png
---
name: Izmit full interferogram
width: 700px
alt: Full Izmit interferogram showing fringes on both sides of the North Anatolian Fault with opposite senses of motion.
---
Full ERS interferogram of the Izmit M7.4 earthquake. The fault (North Anatolian Fault) runs roughly east-west through the center. North of the fault: fringes go blue→yellow→red moving toward the fault — the ground moved *toward* the satellite (range decrease). South of the fault: fringes go red→yellow→blue — the ground moved *away from* the satellite (range increase). This antisymmetric pattern is exactly what elastic rebound predicts for right-lateral slip on a roughly east-west fault viewed from the west (ascending pass).
```

Key observations:
- **Fringes are tightest near the fault** — the displacement gradient (strain) is highest near the rupture
- **Opposite fringe directions on opposite sides** — the two blocks moved in opposite directions
- **Profile through the data** follows the arctangent shape predicted by the Savage-Burford model — direct evidence that earthquakes are elastic rebound phenomena

---

## Earthquake Deformation: A Buried Normal Fault

Not all earthquakes rupture the surface. When a fault slips below the surface, the deformation pattern is different — concentric closed fringes rather than a sharp offset.

```{figure} ../figures/08_wells_interferogram.png
---
name: Wells Nevada interferogram
width: 650px
alt: InSAR interferogram of the 2008 M6.0 Wells Nevada earthquake showing concentric closed fringes indicating subsidence without surface rupture.
---
ERS interferogram of the 2008 M6.0 Wells, Nevada earthquake. Each blue→yellow→red cycle = 28 mm of displacement *away* from the satellite (subsidence). Four complete fringes = ~11 cm of subsidence at the center. The closed, bull's-eye pattern with no sharp discontinuity indicates a blind (non-surface-rupturing) normal fault. If it rained, you would expect a puddle roughly 12 km × 8 km × 11 cm deep — invisible to the naked eye, but clearly imaged by radar. After Funning (GEO 147 lecture notes).
```

---

## Phase Unwrapping

The raw interferogram is **wrapped** — phase repeats every $2\pi$ (every half-wavelength), just as a clock face wraps at 12. To recover a continuous displacement map, we must **unwrap** the phase — essentially adding the correct integer multiple of $2\pi$ to each pixel.

```{figure} ../figures/08_unwrapping.png
---
name: Phase unwrapping
width: 700px
alt: Side-by-side comparison of a wrapped interferogram showing colored fringes and the corresponding unwrapped displacement map showing a continuous color scale.
---
**Left:** wrapped interferogram — phase repeats modulo $2\pi$, displayed as cycling colors. **Right:** unwrapped displacement map — a continuous surface displacement field. Blue = motion away from satellite; red = motion toward satellite. The unwrapped data is what we use for modeling.
```

Unwrapping can fail where:
- The fringe density is too high (displacement gradient exceeds $\lambda/2$ per pixel)
- Coherence is lost (decorrelation — see below)
- The signal is discontinuous across a surface rupture

👉 Phase unwrapping is one of the most challenging steps in InSAR processing and is an active area of algorithm development.

---

## From Interferogram to Fault Model

Once we have an unwrapped displacement map, the workflow for modeling an earthquake is:

1. **Downsample** — reduce the ~millions of pixels to ~thousands by spatially averaging far-field pixels where the signal varies slowly. This makes the inversion computationally tractable without losing information.

2. **Optimize fault geometry** — use a non-linear search to find the fault parameters (strike, dip, depth, dimensions) that best fit the observed deformation pattern. The forward model is typically Okada (1985) elastic dislocation in a half-space.

3. **Invert for slip distribution** — divide the fault plane into sub-patches and solve for the slip on each patch. This reveals **asperities** — areas of enhanced slip — and the spatial extent of the rupture.

```{figure} ../figures/08_inversion_workflow.png
---
name: InSAR inversion workflow
width: 720px
alt: Four-panel figure showing the steps from unwrapped InSAR data to downsampled data to fault geometry optimization to slip distribution model.
---
Workflow from InSAR data to fault model, illustrated for a Tibet M6.1 earthquake. (a) Unwrapped LOS displacement — up to 2.5 m offset at the fault. (b) Downsampled data — millions of pixels reduced to thousands. (c) Fault geometry optimization — searching for the best-fitting fault plane. (d) Slip distribution on the fault — asperities visible as areas of high slip. After Funning (GEO 147 lecture notes).
```

We will return to this workflow in detail in the forward modeling and inversion lectures.

---

## InSAR Beyond Earthquakes

InSAR can measure any surface deformation that occurs between two satellite passes. Applications include:

**Volcanic deformation**
- **Inflation**: magma intruding into a shallow chamber causes the ground to dome upward and outward — a warning sign of potential eruption
- **Deflation**: eruption empties the magma chamber, causing the volcano to sink inward
- InSAR has detected inflation at volcanoes months before eruptions

**Groundwater and subsidence**
- Pumping of aquifers causes land subsidence — the Central Valley of California has subsided by meters in some areas due to groundwater extraction
- Recharge of aquifers causes uplift — InSAR detected the rebound of the Santa Clara Valley (San Jose/Sunnyvale area) in the 1990s when groundwater pumping was reduced
- Detection of subsidence above oil fields

**Glaciers and ice sheets**
- InSAR can measure the speed of glaciers flowing into the sea — critical for sea-level rise estimates

**Landslides and slow slope movement**
- Millimeter-per-year creep on hillsides can be detected before catastrophic failure

**Water level changes**
- In wetlands like the Everglades, radar double-bounces off reeds and the water surface — InSAR can detect centimeter-scale changes in water level over large areas

---

# Sources of Noise in InSAR

---

## Atmospheric Delay

The largest and most persistent source of noise in InSAR is **tropospheric water vapor**. Microwaves travel slightly slower through moist air than through dry air — the delay is proportional to the integrated water vapor along the radar path.

If the water vapor distribution is different on the two acquisition dates, the differential delay appears as a spurious phase signal in the interferogram. This can be:

**Turbulent atmosphere** — spatially variable water vapor that produces a patchy, irregular fringe pattern that can masquerade as deformation. Particularly bad in:
- Coastal regions
- Areas with strong diurnal convection
- Winter versus summer season pairs

**Stratified atmosphere** — water vapor decreases with altitude, so topography that sticks up into the atmosphere creates a phase signal correlated with elevation. This can look like:
- An apparent uplift of high terrain
- Or an apparent subsidence, depending on the sign of the water vapor anomaly

```{figure} ../figures/08_atmospheric_noise.png
---
name: Atmospheric noise examples
width: 720px
alt: Two examples of atmospheric noise in InSAR interferograms - turbulent atmosphere over Los Angeles and stratified atmosphere correlated with topography in Tibet.
---
**Left:** One-day interferogram over Los Angeles — no tectonic signal expected, but strong turbulent atmospheric noise produces fringe patterns that could be mistaken for deformation. **Right:** Tibet interferogram showing atmospheric signal correlated with topography (the high plateau produces less delay than the surrounding lowlands). After Funning (GEO 147 lecture notes).
```

**Mitigation strategies:**
- Stack many interferograms — atmospheric noise is random and averages down while tectonic signal accumulates
- Use weather model corrections (ERA5, HRES)
- Use GPS/GNSS observations to estimate and remove the tropospheric delay
- Choose image pairs from the same time of day (sun-synchronous orbits help)

---

## Decorrelation

When the ground surface **changes** between two SAR acquisitions, the scattering characteristics of pixels change — the random phase term no longer cancels when we difference the two images. This is called **decorrelation** and it causes loss of signal (the interferogram becomes noisy or blank in those areas).

Common causes:
- **Snow** — falling or melting snow completely changes the scattering properties of pixels
- **Vegetation** — leaves growing or falling, crops being planted or harvested, trees blowing in wind
- **Flooding** — water on the ground looks completely different from dry ground
- **Surface changes** — fires, landslides, construction

```{figure} ../figures/08_decorrelation.png
---
name: Decorrelation example
width: 700px
alt: Two InSAR interferograms of a Tibet earthquake showing the same event but different time windows - the longer time span has good coherence while the shorter winter span shows decorrelation from snow.
---
Tibet M6.0 earthquake (1993). **Left:** July 1992 to March 1993 interferogram — the earthquake signal is clear, but some areas show decorrelation from snow that fell in winter. **Right:** February to March 1993 (shorter span, but spanning the snowfall) — the earthquake signal is largely lost because snow changed the surface scattering. The snow decorrelation removes signal in vegetated/high-altitude areas while bare rock areas remain coherent. After Funning (GEO 147 lecture notes).
```

**Decorrelation increases with time** — the longer the interval between passes, the more chances for the surface to change. This means:
- Short repeat times are better for maintaining coherence
- Deserts and bare rock are ideal for InSAR — the surface rarely changes
- Vegetated areas at short wavelengths (C-band) are challenging

**Mitigation:**
- Use longer wavelengths — L-band (24 cm, e.g., NISAR) penetrates vegetation canopy and scatters from more stable soil and branches; less sensitive to surface changes
- Use short temporal baselines — Sentinel-1's 6-day repeat dramatically reduces decorrelation compared to ERS's 35-day repeat
- Persistent scatterer InSAR (PS-InSAR) — identifies pixels (buildings, rocks) that remain coherent over many acquisitions and exploits only those

---

## Current Satellites

The operational landscape has improved dramatically since the first civilian InSAR satellites:

| Satellite | Agency | Band | Wavelength | Repeat | Status |
|-----------|--------|------|-----------|--------|--------|
| ERS-1/2 | ESA | C | 5.6 cm | 35 days | Retired |
| Envisat | ESA | C | 5.6 cm | 35 days | Retired |
| Sentinel-1A/B | ESA | C | 5.6 cm | 6–12 days | Operational |
| ALOS-2 | JAXA | L | 24 cm | 14 days | Operational |
| TerraSAR-X | DLR | X | 3.1 cm | 11 days | Operational |
| NISAR | NASA/ISRO | L+S | 24/9 cm | 12 days | ~2025 launch |

**Sentinel-1** (launched 2014/2016) is the current workhorse for tectonic InSAR — free data, 6-day repeat with both satellites, global coverage, and consistent acquisition strategy. It has enabled near-real-time earthquake response for the first time.

---

# InSAR for Topography

---

## The Topographic Phase

When the satellite is not in exactly the same orbital position on two passes — which is always the case — the change in viewing geometry introduces a phase contribution that depends on **topography**, not just deformation. This is the **topographic phase** and it must be removed when we want to measure deformation.

The geometry is straightforward: a tall mountain is closer to the satellite on one pass than on another, depending on the baseline between the two orbital positions. The longer the **perpendicular baseline** $B_\perp$ (the component of the baseline perpendicular to the LOS direction), the stronger this topographic contribution.

For ERS satellites:

$$
H_a = \frac{10,000}{B_\perp}
$$

where $H_a$ is the **altitude of ambiguity** — the elevation change required to produce one full fringe (2π phase change). For $B_\perp = 20$ m, $H_a = 500$ m per fringe; for $B_\perp = 100$ m, $H_a = 100$ m per fringe.

👉 **For deformation studies:** use small baselines ($B_\perp < 200$ m) to minimize topographic sensitivity. **For topographic mapping:** use large baselines ($B_\perp \approx 100$ m) to maximize topographic sensitivity.

```{figure} ../figures/08_topo_phase.png
---
name: Topographic phase
width: 700px
alt: Two interferograms of the same mountainous area with different baselines showing different fringe densities correlated with topography.
---
Topographic phase for the same area at two different perpendicular baselines. **Left:** 20 m baseline — 500 m/fringe, showing ~2 fringes across ~1,000 m of relief. **Right:** 100 m baseline — 100 m/fringe, showing many more fringes across the same terrain. For deformation studies we use short baselines to minimize this effect; for topographic mapping we use longer baselines to maximize sensitivity. After Funning (GEO 147 lecture notes).
```

---

## The Shuttle Radar Topography Mission (SRTM)

The most famous application of InSAR to topographic mapping was the **Shuttle Radar Topography Mission (SRTM)**, which flew on Space Shuttle Endeavour for 11 days in February 2000.

**Mission design:**
- Two C-band SAR antennas: one in the cargo bay (transmitter + receiver), one on a 60-meter boom extended from the cargo bay (receiver only)
- The two antennas recorded simultaneously — no decorrelation (the ground couldn't change between two simultaneous acquisitions) and no differential atmospheric delay (both signals traveled through the same atmosphere)
- This eliminated the two main sources of InSAR noise in one stroke

**Coverage and resolution:**
- Covered the entire tectonically active Earth between 56°S and 60°N (excluding poles and Greenland/Antarctica)
- 225 km swath width — mapped the whole world in one orbital cycle
- 30 m pixel resolution (originally released at 90 m outside the US; full resolution now globally available)
- Elevation accuracy: < 10 m vertical error globally
- 12.3 terabytes of data — enormous in 2000, modest today

```{figure} ../figures/08_srtm_setup.png
---
name: SRTM setup
width: 700px
alt: Diagram showing Space Shuttle Endeavour with the 60-meter radar boom extended from the cargo bay, with two SAR antennas separated by the boom length.
---
SRTM mission setup. The 60 m boom extended from Endeavour's cargo bay separated the two C-band antennas. Simultaneous acquisition eliminated decorrelation and differential atmospheric noise — the two main InSAR noise sources. After Funning (GEO 147 lecture notes).
```

**Why SRTM matters for InSAR:**

SRTM is the standard DEM used to remove the topographic phase from deformation interferograms. Conveniently, because SRTM used C-band radar (the same frequency as ERS and Sentinel-1), it scatters from the same surface features — including vegetation canopy. When we remove the topographic phase from a Sentinel-1 interferogram using SRTM, we are effectively correcting for the same scattering surface, which minimizes residual topographic errors.

SRTM is also the DEM underlying Google Earth and most global mapping products.

---

# Summary

- **SAR** images the ground using active microwave illumination. It records both amplitude (brightness of backscatter) and phase (distance to ground). It can image through clouds, at night, and in all weathers.

- **Synthetic aperture** processing combines returns from many orbital positions to synthesize a large virtual antenna, achieving ground resolution of ~20 m from a small physical antenna in space.

- **InSAR** differences the phase of two SAR images acquired at different times. Where the random scattering term cancels (coherent pixels), the phase difference measures **line-of-sight displacement** with millimeter sensitivity.

- **Each fringe** in an interferogram represents $\lambda/2$ of LOS displacement (~2.8 cm for C-band). Counting fringes from a reference area gives cumulative displacement; fringe density maps the gradient of displacement.

- **InSAR measures LOS displacement**, not 3D displacement. Combining ascending and descending interferograms allows partial decomposition into horizontal and vertical components. The technique is relatively insensitive to north-south motion.

- **Sources of noise:** (1) atmospheric water vapor — the dominant noise source, correlated with topography (stratified) or spatially random (turbulent); (2) decorrelation — changes in ground scattering between passes, due to vegetation, snow, flooding, or surface change. Both worsen with longer time intervals.

- **InSAR applications** span earthquakes, volcanoes, landslides, glaciers, groundwater, and subsidence — any surface deformation at spatial scales of meters to thousands of kilometers.

- **SRTM** — the global 30 m DEM produced by simultaneous InSAR from two antennas on Space Shuttle Endeavour — is the standard topographic reference for InSAR processing and the foundation of Google Earth.

- The deformation maps produced by InSAR are the primary data inputs to the **elastic dislocation inversions** we will study in the next two weeks.

---

# Laboratory

In the lab, you will:

1. Load and interpret real InSAR interferograms from the Ridgecrest M7.1 earthquake
2. Convert fringe counts to LOS displacement
3. Compare ascending and descending interferograms to understand the 3D displacement field
4. Identify and discuss sources of noise — atmospheric signals and decorrelation
5. Compare the InSAR displacement profile to the coseismic GNSS offsets from Lab 4

---

# Additional Resources

> **Textbook chapter:** [InSAR: Seeing the Earth's Surface Deform](https://doi.org/10.1146/annurev-earth-040610-133404)  
> Bürgmann, R., Rosen, P. A., & Fielding, E. J. (2000). Synthetic aperture radar interferometry to measure Earth's surface topography and its deformation. *Annual Review of Earth and Planetary Sciences*, 28, 169–209.

> **Review article:** [InSAR in natural hazards](https://doi.org/10.1038/s43017-021-00155-5)  
> Biggs, J. & Wright, T. J. (2020). How satellite InSAR has grown from opportunistic science to routine monitoring over the last decade. *Nature Geoscience*, 13, 388–396.

> **Data portal:** [ARIA (Advanced Rapid Imaging and Analysis)](https://aria.jpl.nasa.gov)  
> NASA/Caltech portal for rapid InSAR products after major earthquakes. Processed Sentinel-1 interferograms are typically available within days of a large event.

> **Data portal:** [Copernicus Open Access Hub](https://scihub.copernicus.eu)  
> Free access to all Sentinel-1 SAR data. Free registration required.

> **Software:** [ISCE (InSAR Scientific Computing Environment)](https://github.com/isce-framework/isce2)  
> NASA/JPL open-source InSAR processing software. The standard tool for processing Sentinel-1 and ALOS-2 data.

> **Dataset:** [SRTM 30m global DEM](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-digital-elevation-shuttle-radar-topography-mission-srtm-1)  
> USGS distribution of the SRTM 1 arc-second (30 m) DEM. Free and global.

---

# Sources

- Funning, G. (n.d.). *GEO 147: Active Tectonics and Remote Sensing* — InSAR lecture series (Parts 1–4). University of California, Riverside.
- Massonnet, D., & Feigl, K. L. (1998). Radar interferometry and its application to changes in the earth's surface. *Reviews of Geophysics*, 36(4), 441–500. https://doi.org/10.1029/97RG03139
- Bürgmann, R., Rosen, P. A., & Fielding, E. J. (2000). Synthetic aperture radar interferometry to measure Earth's surface topography and its deformation. *Annual Review of Earth and Planetary Sciences*, 28, 169–209. https://doi.org/10.1146/annurev.earth.28.1.169
- Farr, T. G., et al. (2007). The shuttle radar topography mission. *Reviews of Geophysics*, 45(2). https://doi.org/10.1029/2005RG000183
- Okada, Y. (1985). Surface deformation due to shear and tensile faults in a half-space. *Bulletin of the Seismological Society of America*, 75(4), 1135–1154.
