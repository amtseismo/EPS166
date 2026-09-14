# Deformation Through the Seismic Cycle

## Purpose

Earthquakes last seconds to minutes, but the deformation that produces and follows them spans decades to centuries.

In this lecture, we will:

- connect interseismic strain accumulation to coseismic slip and postseismic relaxation
- recognize interseismic, coseismic, and postseismic signals in GNSS time series
- use the Savage–Burford elastic model to relate velocity profiles to fault slip rate and locking depth
- examine how fault geometry, creep, and Earth rheology complicate the simple picture
- preview how the same dislocation framework describes coseismic surface displacement
- connect slip deficit and recurrence interval to an earthquake moment budget

---

# The Earthquake Cycle

An earthquake is one brief part of a longer cycle. In terms of crustal deformation, the loading cycle is divided into four phases:

- **Interseismic** — slow, steady strain accumulation between earthquakes
- **Preseismic** — possible accelerating deformation immediately before rupture
- **Coseismic** — seconds to minutes of rapid fault slip and elastic rebound
- **Postseismic** — months to decades of decaying deformation following the earthquake

This fourfold structure has been assembled from geodetic observations in many places. Complete cycles spanning all four phases have been observed for intermediate-magnitude earthquakes in only a small number of locations — most records capture only part of the cycle.

```{figure} ../figures/04_seismic_cycle_timeseries.png
---
name: GNSS Earthquake Cycle
width: 600px
alt: Synthetic GNSS position time series showing interseismic loading, a coseismic offset, and postseismic deformation.
---
A GNSS station may record steady interseismic motion, a nearly instantaneous coseismic offset, and a decaying postseismic transient. The next loading interval begins before postseismic deformation has necessarily ended.
```

---

## Reid and Elastic Rebound

Reid's interpretation of the 1906 San Francisco earthquake established the conceptual framework we still use:

- steady plate motion gradually deforms the crust around a locked fault
- elastic strain accumulates over a long interval
- the fault eventually slips when elastic stress exceeds fault strength
- the surrounding crust rebounds toward a less strained configuration

```{figure} ../figures/04_reid_elastic_rebound.png
---
name: Elastic Rebound
width: 650px
alt: Historical diagram illustrating elastic rebound across a strike-slip fault.
---
Conceptual illustration of elastic rebound. The pre-earthquake distortion records stored elastic strain; fault slip releases part of that strain and the crust rebounds. After Reid (1910).
```

---

## GNSS Records All Phases of the Earthquake Cycle

Different geodetic representations emphasize different parts of the earthquake cycle:

| Observation | What it records | Typical units |
|---|---|---|
| Position time series | Temporal evolution at one station | mm |
| Interseismic velocity field | Spatial pattern of ongoing loading and creep | mm/yr |
| Coseismic offsets | Permanent earthquake displacement | mm to m |
| Postseismic velocity or displacement | Continuing response after rupture | mm/yr or mm |

Physical interpretation requires both temporal evolution and spatial pattern. A velocity field alone cannot distinguish interseismic loading from long-lived postseismic relaxation without additional constraints.

---

# Interseismic Deformation

During the interseismic period:

- the shallow seismogenic fault remains locked — no slip occurs
- deeper parts of the plate boundary continue to move at the long-term plate rate
- the elastic crust deforms to accommodate the mismatch between locked shallow fault and freely slipping deep fault
- the resulting velocity gradient represents elastic strain accumulation

This connects directly to the strain lecture: **spatial variation in velocity produces strain rate**, and that strain rate represents energy being stored in the crust.

```{figure} ../figures/04_deep_dislocation.png
---
name: Deep dislocation
width: 700px
alt: Schematic diagram of a deep dislocation beneath a locked fault and the resulting surface velocity field.
---
A locked fault above depth $D$ with steady creep below is equivalent to a buried dislocation at depth $D$. The elastic crust deforms smoothly in response, producing a broad velocity gradient at the surface.
```

---

## The Savage–Burford Model

For a vertical strike-slip fault and fault-perpendicular distance $x$, the surface velocity is:

$$
v_{\parallel}(x) = \frac{V_s}{\pi} \arctan\!\left(\frac{x}{D}\right)
$$

- $v_{\parallel}$: fault-parallel surface velocity
- $V_s$: long-term relative slip rate
- $D$: locking depth
- $x$: distance from the fault (positive on one side, negative on the other)

Far from the fault, the velocity asymptotes to $\pm V_s/2$. Near the fault, the velocity changes smoothly — the width of the transition zone is controlled by the locking depth.

This is a deliberately simple model: one vertical fault, uniform locking above one depth, homogeneous elastic half-space, no neighboring faults.

---

## Slip Rate and Locking Depth Affect Different Features

```{figure} ../figures/04_arctan.png
---
name: Savage-Burford Model
width: 700px
alt: Arctangent velocity profiles for four locking depths and four slip rates.
---
**Left:** locking depth controls the width of the velocity gradient — shallow locking produces a sharp, localized transition; deep locking spreads the deformation broadly. **Right:** slip rate scales the amplitude of the profile without changing its shape. The inflection point of the curve lies directly above the locking depth. Figure generated from the Savage–Burford (1973) formula.
```

> **Question:** Which locking depth produces the largest velocity gradient immediately adjacent to the fault? Which produces the smallest?

---

## Interseismic Deformation on the San Andreas

Despite its simplicity, the Savage–Burford model fits GNSS velocity profiles across locked segments of the San Andreas system remarkably well.

```{figure} ../figures/04_saf_coupling.png
---
name: SAF coupling
width: 700px
alt: GNSS and InSAR velocity profile across the San Andreas Fault showing an arctangent fit.
---
Strike-slip velocity profile across Southern California from GPS data: (a) location map, the dots are the GPS stations used; (b) the velocity profile, in which the staircase indicates the slip rates as determined by modeling the velocity data using the strong plastosphere model (see Figure 5.8). The results agree with geological data on the slip rate of the faults. (From Bourne et al., 1998.)
```

The fit is not perfect — but the dominant signal is well described by a single buried dislocation.

👉 Residual patterns are scientifically useful: they identify where the simple model breaks down and point to additional deformation sources.

---

## Caveats

The Savage–Burford model assumes a vertical fault. Real fault systems deviate in important ways:

- **Dipping faults** (subduction zones, thrust faults) produce asymmetric velocity profiles — the hanging wall moves more than the footwall
- **Multiple parallel faults** spread deformation across a wider zone than a single fault predicts (see above!)
- **Fault bends and stepovers** concentrate or distribute strain locally
- **3D fault geometry** requires numerical elastic dislocation models 

For strike-slip faults at shallow dip, the arctan model is a good first approximation. For subduction zones, it fails — and that failure is itself informative.

---

# Creep

Some faults slip continuously or episodically without producing felt earthquakes. This **fault creep** reaches the surface and can be measured directly — offset curbs, cracked sidewalks, and deformed building foundations are visible evidence in the East Bay.

```{figure} ../figures/04_offset_curb.jpg
---
width: 750px
alt: Offset curb on the Hayward fault at Rose and Prospect streets in Hayward CA.
---
An offset curb at Rose and Prospect streets on the Hayward fault in Hayward, CA — a classic surface expression of aseismic creep accumulating over decades. The fault creeps at ~5 mm/yr here, slowly shearing anything built across it. Image credit to Rong-Gong Lin II / Los Angeles Times.
```

- **Steady creep** — continuous slow slip at a roughly constant rate; accumulates millimeters per year
- **Episodic creep events** — short bursts of accelerated slip lasting hours to days, sometimes triggered by nearby earthquakes or slow slip transients
- Creep releases elastic strain continuously, reducing the slip deficit rate relative to a fully locked fault
- The Hayward fault creeps at 3–9 mm/yr along much of its length — but it is **not** fully creeping; locked patches remain and represent significant seismic hazard
- The central San Andreas (Parkfield to Hollister) is the classic creeping segment, slipping at ~25 mm/yr aseismically

```{figure} ../figures/04_los_creep.jpg
---
name: LOS creep in central CA
width: 750px
alt: (a) Interferometric synthetic aperture radar line-of-sight (LOS) surface deformation between 1992 and 2010. The red and blue colors represent the surface motion in the LOS direction toward and away from the satellite, respectively. The solid black line represents the surface trace of the San Andreas Fault. The Global Positioning System (GPS) stations are shown using the solid rectangles color-coded based on their 3-D displacement rates projected onto the LOS direction. The direction and magnitude of GPS horizontal rates are also shown using the yellow arrows. The black dashed lines show the location of fault-perpendicular profiles, where the interferometric synthetic aperture radar LOS rates are compared with the corresponding GPS values (Figure S1). (b) The distribution of inverted long-term creep rate on Central San Andreas Fault. The cumulative time series of creep for several patches is also shown, color-coded based on the SAR acquisition times. The best fit to each time series, determining the long-term rate, is also shown using the solid black line.
---
(a) Interferometric synthetic aperture radar line-of-sight (LOS) surface deformation between 1992 and 2010. The red and blue colors represent the surface motion in the LOS direction toward and away from the satellite, respectively. The solid black line represents the surface trace of the San Andreas Fault. The Global Positioning System (GPS) stations are shown using the solid rectangles color-coded based on their 3-D displacement rates projected onto the LOS direction. The direction and magnitude of GPS horizontal rates are also shown using the yellow arrows. The black dashed lines show the location of fault-perpendicular profiles, where the interferometric synthetic aperture radar LOS rates are compared with the corresponding GPS values (Figure S1). (b) The distribution of inverted long-term creep rate on Central San Andreas Fault. The cumulative time series of creep for several patches is also shown, color-coded based on the SAR acquisition times. The best fit to each time series, determining the long-term rate, is also shown using the solid black line. [Khoshmanesh and Shirzaei (2018)](https://doi.org/10.1002/2018GL077017)
```

👉 A creeping fault is not a safe fault — partial coupling means significant strain can still accumulate on locked patches between creeping sections.

---

## Creep in Northern California

Creep is not randomly distributed and not fully understood.  It correlates with fault rock composition and is pervasive in northern California. Faults cutting through **serpentinite** and **smectite-rich** fault gouge are weak and they resist earthquake nucleation and slip stably. Faults in stronger, accumulate elastic strain and rupture seismically.

```{figure} ../figures/04_creep_geology.png
---
name: Creep geology
width: 700px
alt: Geologic map showing the distribution of serpentinite and creep-prone lithologies along northern California fault systems.
---
A generalized geological map of California, showing the difference in basic geology east and west of -119.4°. Creep rate data are white circles where creep rate exceeds 3 mm/yr, black where creep rates are lower than 3 mm/yr. Image from [Earthquake Insights](https://earthquakeinsights.substack.com/p/why-are-some-faults-so-creepy)
```

Creep is widespread throughout northern California:

- **Central San Andreas** (San Juan Bautista to Parkfield) — creeps at 20–28 mm/yr, nearly the full plate rate; serpentinite and weak fault gouge dominate
- **Hayward fault** — creeps at 3–9 mm/yr along much of its length; partially coupled, with locked patches that represent significant M6.5–7 hazard
- **Calaveras fault** — creeps at up to 15 mm/yr in its central section
- **Rogers Creek and Maacama faults** — partially creeping in the North Bay

```{figure} ../figures/04_creep_distribution.png
---
name: NorCal creep distribution
width: 400px
alt: Map of northern California showing surface creep rates on major fault segments inferred from InSAR and geodetic observations.
---
Surface creep rates on major northern California fault segments from geodetic observations. The creeping central San Andreas accommodates nearly the full Pacific–North America plate motion aseismically. Partially creeping segments of the Hayward and Calaveras faults release some strain continuously but retain locked patches capable of producing damaging earthquakes.
```

👉 A creeping fault is not a safe fault. The Hayward fault creeps — and it is also one of the most hazardous faults in the United States, capable of an M7+ earthquake that would affect millions of people in the East Bay.


---

## Coupling

The **coupling fraction** $\phi$ describes how much of the long-term plate motion accumulates as elastic strain:

- $\phi = 1$: fully coupled — all motion stored as elastic strain, maximum earthquake potential
- $\phi = 0$: freely creeping — motion released continuously, little elastic strain accumulates
- $0 < \phi < 1$: partially coupled — mixed behavior

```{figure} ../figures/04_creep_profile.png
---
name: Creep Profile
width: 720px
alt: Velocity profiles for fully locked, partially coupled, and freely creeping strike-slip faults.
---
Averaged LOS velocity profiles perpendicular to the fault over Central California along the creeping section of the SAF (Figure 5c). The blue dots with 1 standard deviation error bars indicate the total LOS velocity, and the black lines are the GPS model. (a) Profile taken along the northern segment of the creeping section. (b) Profile taken along the central segment of the creeping section. [Tong et al. (2013)](https://doi.org/10.1029/2012JB009442)
```

The central San Andreas (Parkfield to San Juan Bautista) and the Hayward fault creep at measurable rates. A surface-creeping fault stores less slip deficit and poses a different seismic hazard than a fully locked fault at the same slip rate.

👉 **Far-field plate motion alone does not determine earthquake potential.** The coupling fraction must be considered.

---

## Cascadia Subduction Zone coupling

The Savage–Burford model breaks down most dramatically at subduction zones. Cascadia illustrates why.

```{figure} ../figures/04_cascadia_coupling.jpg
---
name: Cascadia coupling
width: 720px
alt: Map of the Cascadia subduction zone showing coupling distributions from three geodetic models and the slow slip region.
---
The Cascadia subduction zone and geodetic coupling models. The Gamma and Gauss models are from Schmalzle et al. (2014), the Li model is from Li et al. (2018). ”1 cm” is the down-dip edge with the highest weight in the National Seismic Hazard Map (Petersen et al., 2020). The slow slip region is the aggregated slip zone from Bartlow (2019). The 15 and 30 km slab depth contours are from Hayes et al. (2018).[Melgar et al. (2022)](https://doi.org/10.1029/2021GL097404)
```

Several features of the Cascadia coupling map are worth noting:

**Along-strike variation:** coupling is far from uniform. The northern and southern segments show different locking patterns, consistent with differences in historical seismicity and slow-slip behavior. No single arctan profile captures this.

**Model dependence:** the elastic models (Schmalzle Gamma and Gauss) and the viscoelastic model (Li et al. 2018) agree on the broad pattern but differ in the details — particularly the downdip extent of locking. Viscoelastic relaxation following past Cascadia megathrust earthquakes produces long-wavelength surface deformation that, if unaccounted for, is misinterpreted as interseismic loading and biases the inferred coupling distribution.

**The slow slip zone sits downdip of the locked zone.** Episodic tremor and slip (ETS) events occur regularly in this transition region, releasing strain aseismically. We will return to this in the slow slip lecture.

**Hazard implications:** the down-dip extent of significant coupling — the "1 cm" contour used in the National Seismic Hazard Map — varies between models. The choice of coupling model directly affects hazard estimates for Pacific Northwest cities.

👉 The simple arctan profile is a useful first model, but real fault systems require spatially variable coupling and — for subduction zones — realistic viscoelastic Earth structure.

---

## Interseismic Loading to Future Slip

For constant long-term rate $V_s$, coupling fraction $\phi$, and elapsed time $T$:

$$
S_{\text{deficit}} = \phi \, V_s \, T
$$

Example for the southern San Andreas:

$$
(1.0)(36\ \mathrm{mm/yr})(150\ \mathrm{yr}) = 5.4\ \mathrm{m}
$$

This is a **kinematic budget** — it tells us how much slip could potentially be released, not when or how it will be released. The deficit may be released in one large earthquake, several smaller ones, or partly as afterslip.

---

## Slip Deficit as a Moment Budget

If a rupture of length $L$ and width $W$ releases average slip $S$:

$$
M_0 = \mu L W S
$$

and

$$
M_w = \frac{2}{3}\left(\log_{10} M_0 - 9.1\right)
$$

Substituting the slip deficit:

$$
M_w = \frac{2}{3}\log_{10}\!\left(\mu \, L \, W \, \phi \, V_s \, T\right) - 9.1
$$

The estimate depends on rupture dimensions, shear modulus, coupling, recurrence interval, and the fraction of the deficit released coseismically.

```{figure} ../figures/04_recurrence_magnitude.png
---
name: Slip defecit, recurrence, and magnitude
width: 820px
alt: Slip deficit and equivalent moment magnitude plotted against recurrence interval.
---
For fixed rupture dimensions, slip deficit increases linearly with recurrence interval, whereas moment magnitude increases only logarithmically. Doubling the recurrence interval doubles the slip but increases $M_w$ by only $\sim$0.2 units.
```

> **Question:** Why is this an earthquake-equivalent moment budget rather than a prediction of the next earthquake magnitude?

---

# Coseismic Deformation

The coseismic phase lasts seconds to minutes. GNSS, InSAR, and strong-motion seismometers record the resulting permanent displacement field.

Offset direction and amplitude depend on fault **strike, dip, rake, depth, dimensions, and slip distribution**. The same elastic dislocation theory that describes interseismic loading describes coseismic displacement — the difference is the sign and geometry of the slip.

```{figure} ../figures/04_tohoku_animation.mp4
---
name: Tohoku Animation
width: 760px
alt: Displacement animation of 30 s kinematic data from the 2011 Tohoku-Oki Earthquake
---
Displacement animation of 30 s kinematic data from [Grapenthin and Freymuller, 2011](https://doi.org/10.1029/2011GL048405)
```

---

## Coseismic Deformation from the 2019 Ridgecrest Sequence

Closer to home — the 2019 Ridgecrest M7.1 produced clear coseismic offsets in GNSS and a striking InSAR interferogram. You analyzed the GNSS time series in the seismology lab; the InSAR signal will be the focus of the InSAR lecture.

```{figure} ../figures/04_ridgecrest_coseismic.png
---
name: Ridgecrest Coseismic
width: 700px
alt: GNSS coseismic displacement vectors from the 2019 Ridgecrest M7.1 earthquake.
---
Horizontal coseismic displacement field from the 2019 Ridgecrest M7.1 earthquake from GNSS. Stations near the fault moved up to several meters; the pattern reflects right-lateral slip on the NW-striking fault plane. This is the same dataset you worked with in the seismology lab — here we see the spatial pattern rather than the time series at a single station.
```

---

## A Simple Model for Coseismic Surface Displacement

The same screw dislocation framework used for interseismic loading also describes coseismic surface displacement — with the argument of the arctan flipped.

For a **surface-rupturing** strike-slip earthquake with slip $S$ and seismogenic depth $D$:

$$
u(x) = \frac{S}{\pi} \arctan\!\left(\frac{D}{x}\right)
$$

Compare to the interseismic case:

$$
v(x) = \frac{V_s}{\pi} \arctan\!\left(\frac{x}{D}\right)
$$

```{figure} ../figures/04_interseismic_vs_coseismic.png
---
name: Elastic Rebound Model Comparison
width: 700px
alt: Comparison of interseismic and coseismic arctan surface deformation profiles.
---
Schematic diagram illustrating a simple elastic rebound model. On the left, the interseismic displacement and strain accumulation fields are modeled with slip at a steady rate below a locking depth D.On the right, coseismic slip and strain release is modeled with slip on the fault down to the depth D.
```

The key differences:

| | Interseismic | Coseismic |
|---|---|---|
| Formula | $\frac{V_s}{\pi}\arctan\!\left(\frac{x}{D}\right)$ | $\frac{S}{\pi}\arctan\!\left(\frac{D}{x}\right)$ |
| Shape | Broad, smooth gradient | Peaked at fault, decays away |
| Discontinuity at fault | No | Yes — equals slip $S$ |
| Far-field value | $\pm V_s/2$ | $0$ |
| Parameter controlling width | $D$ (locking depth) | $D$ (seismogenic depth) |

👉 These two profiles are complementary: interseismic loading stores elastic strain broadly across the fault zone; the earthquake releases it, with the largest displacement right at the fault.

We will return to more realistic 3D elastic dislocation models — the Okada (1985) formulation — in the forward modeling and inversion lectures.

---

# Postseismic Deformation

Postseismic deformation begins immediately after the earthquake and can 
persist for months to decades. It reflects the Earth's continuing mechanical 
response to the sudden stress change imposed by the rupture.

The postseismic signal is important for two reasons:

1. It carries information about fault friction, crustal fluids, and mantle 
   rheology that is not accessible from the coseismic snapshot alone
2. It can contaminate velocity fields interpreted as steady interseismic 
   loading if the observation period is too close to a past earthquake

```{figure} ../figures/04_postseismic_mechanisms.png
---
name: Postseismic mechanisms
width: 750px
alt: Two-panel synthetic figure showing a GNSS time series with stacked 
postseismic contributions from afterslip, poroelastic rebound, and 
viscoelastic relaxation, and a log-time plot of the individual mechanisms.
---
**Top:** synthetic GNSS time series at a near-fault station showing 
interseismic loading, the coseismic step, and the three postseismic 
contributions stacked. Poroelastic rebound saturates quickly; afterslip 
dominates the first months to years; viscoelastic relaxation grows slowly 
and eventually becomes the dominant signal. **Bottom:** the three mechanisms 
plotted individually on a log time axis, with characteristic timescales 
marked. The logarithmic decay of afterslip, rapid saturation of poroelastic 
rebound, and slow onset of viscoelastic relaxation are the key observational 
diagnostics.
```

---

## Afterslip

**What it is:** continued aseismic slip on the fault surface after the main 
rupture, driven by the stress concentration left at the rupture edges. 
Afterslip is governed by rate-and-state friction — the same fault that 
slipped seismically continues to creep in the velocity-strengthening regions 
surrounding the rupture.

**Where it occurs:** on or immediately adjacent to the fault — often in areas 
that did not rupture coseismically, or at the downdip and along-strike edges 
of the slip patch.

**Spatial signature:** concentrated near the fault trace; mirrors the rupture 
geometry — stations close to the fault move most.

**Timescale:** days to years; decays roughly **logarithmically** in time. 
This logarithmic signature is a key diagnostic distinguishing afterslip from 
viscoelastic relaxation.

```{figure} ../figures/04_afterslip_literature.png
---
width: 700px
alt: Map and GNSS time series showing postseismic afterslip following a 
major earthquake from the published literature.
---
[Add published afterslip figure here — good options include Perfettini et al. 
(2010) for the 2007 Pisco Peru earthquake, or Twardzik et al. (2019) for 
Ridgecrest postseismic.]
```

---

## Poroelastic Rebound

**What it is:** redistribution of pore fluids in the crust in response to 
coseismic stress changes. Coseismic slip compresses some parts of the crust 
and dilates others; fluids flow in response, and the associated volume 
changes deform the surface.

**Where it occurs:** in fluid-saturated crust surrounding the rupture — 
particularly in sedimentary basins or heavily fractured rock near the fault.

**Spatial signature:** near-field; may produce deformation that locally 
**reverses** the sense of coseismic displacement as pore pressures 
re-equilibrate.

**Timescale:** days to months — controlled by crustal permeability and fluid 
diffusivity. The most rapidly decaying of the three mechanisms.

---

## Viscoelastic Relaxation

**What it is:** flow of the viscoelastic lower crust and upper mantle in 
response to the coseismic stress step. The elastic upper crust is coupled to 
a viscoelastic substrate that flows slowly over years to decades, dragging 
the surface with it.

**Where it occurs:** lower crust and upper mantle — producing a broad, 
long-wavelength deformation field at the surface that can extend hundreds of 
kilometers from the fault.

**Spatial signature:** wide spatial extent, often far beyond the rupture zone. 
Unlike afterslip, which peaks near the fault, viscoelastic deformation may 
be largest at intermediate distances.

**Timescale:** years to decades — controlled by mantle viscosity. 
Characteristic relaxation times of 1–10 years are typical for the lower 
crust; upper mantle relaxation can persist for decades.

---

## Separating the Mechanisms

| Mechanism | Spatial extent | Temporal decay | Key diagnostic |
|---|---|---|---|
| Afterslip | Fault-centered | Logarithmic, days–years | Mirrors rupture geometry; near-fault stations move most |
| Poroelastic | Near field | Rapid exponential, days–months | May reverse coseismic sense; permeability-controlled |
| Viscoelastic | Broad, far field | Slow exponential, years–decades | Long wavelength; grows after initial postseismic period |

In practice these mechanisms operate simultaneously and their signals overlap 
in both space and time. Separating them requires dense spatial coverage, long 
time series, and mechanical forward models. The GNSS era has made this 
possible for the first time.

👉 A velocity field measured within a decade of a major earthquake may include 
significant postseismic signal — this is not interseismic loading and should 
not be interpreted as such.

---

# Laboratory

In the lab, you will:

1. rotate North America-fixed GNSS velocities into San Andreas fault coordinates
2. construct a fault-perpendicular velocity profile across the SAF
3. fit the Savage–Burford model to recover slip rate, locking depth, and a velocity offset
4. examine how creep modifies the predicted profile
5. convert a slip-deficit rate and recurrence interval into a moment budget

In the coming weeks, we will move from this 1D forward model to full 3D elastic dislocation models — the Okada (1985) formulation — and then to the inverse problem: recovering fault slip from observed surface deformation.

---

# Summary

- The earthquake cycle spans four phases: interseismic, preseismic, coseismic, and postseismic.
- Interseismic velocity gradients record elastic strain accumulation around locked faults. The Savage–Burford model predicts an arctangent profile; locking depth controls the width of the gradient and slip rate controls the amplitude.
- The arctan model fits locked segments of the SAF well, but real fault systems require spatially variable coupling. Subduction zones like Cascadia require viscoelastic Earth models to correctly infer locking from surface velocities.
- Fault creep reduces the coupling fraction and lowers the slip deficit rate — far-field plate velocity alone does not determine earthquake potential.
- Slip deficit provides a kinematic moment budget, not a deterministic earthquake forecast.
- Coseismic displacement follows $u(x) = \frac{S}{\pi}\arctan(D/x)$ for a surface-rupturing fault — the same dislocation physics as interseismic loading, with the arctan argument flipped.
- Postseismic deformation reflects three overlapping mechanisms — afterslip, poroelastic rebound, and viscoelastic relaxation — each with distinct spatial and temporal signatures.

---

# Additional Resources

> **Textbook:** [The Mechanics of Earthquakes and Faulting (3rd ed.)](https://doi.org/10.1017/9781316681473)  
> Scholz, C. H. (2019). Chapters 4–5 cover elastic rebound, fault mechanics, and the seismic cycle in depth. The standard graduate reference for this material.

> **Classic Paper:** [Geodetic Determination of Relative Plate Motion in Central California](https://doi.org/10.1029/JB078i005p00832)  
> Savage & Burford (1973). The original derivation of the arctangent interseismic velocity profile and its application to San Andreas geodetic data.

> **Research Article:** [Geodetically Inferred Locking State of the Cascadia Megathrust Based on a Viscoelastic Earth Model](https://doi.org/10.1029/2018JB015620)  
> Li et al. (2018). Shows how ignoring viscoelastic relaxation from past Cascadia earthquakes leads to systematic overestimation of current coupling — a cautionary example for interpreting any velocity field near a recently ruptured subduction zone.

> **Research Article:** [Multiscale Interseismic Strain Partitioning and Seismic Hazard Along the San Andreas Fault System](https://doi.org/10.1029/2021GL097404)  
> Khoshmanesh & Shirzaei (2022). Combined InSAR and GNSS coupling model for the full SAF system — shows both where the arctan model works and where it breaks down.

> **Teaching Animation:** [Kinematic GPS During the 2011 Tohoku-Oki Earthquake](https://doi.org/10.1029/2011GL048405)  
> Grapenthin & Freymueller (2011). The 30-second kinematic GNSS displacement animation used in lecture.

> **Interactive Tool:** [UNAVCO Velocity Viewer](https://www.unavco.org/software/visualization/GPS-Velocity-Viewer/GPS-Velocity-Viewer.html)  
> Browse and download GNSS velocity fields for any region. Useful for constructing your own fault-perpendicular profiles beyond the lab dataset.
