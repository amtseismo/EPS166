# Constraints from Seismology

## Purpose

In previous weeks we measured crustal deformation using GNSS — recording the slow, steady accumulation of strain and the permanent offsets left behind by earthquakes. In this chapter we turn to seismology and ask: what do seismic waves tell us about the earthquake source itself?

We will:

- distinguish static (permanent) from dynamic (transient) deformation and see both in real data
- describe earthquake fault geometry using strike, dip, and rake
- define seismic moment and moment magnitude and connect them to physical fault properties
- interpret focal mechanisms and beachball diagrams in terms of fault motion and tectonic stress
- introduce Green's functions as the bridge between source and seismogram — and between this lecture and the inversion weeks ahead
- read seismotectonic patterns from populations of focal mechanisms

---

# Static vs. Dynamic Deformation

## Two Kinds of Ground Motion

An earthquake does two distinct things to the ground around it.

**Near the fault**, the two sides are permanently displaced. Roads are offset, fences are broken, and GNSS stations record a step in their position time series that never goes away. This is **static deformation** — the crust has moved and stayed moved.

**Far from the fault**, seismic waves radiate outward as transient disturbances. The ground shakes as each wave passes, then returns to rest. This is **dynamic deformation** — temporary motion with no permanent displacement.

```{figure} ../figures/05_gnss_offsets.png
---
name: Ridgecrest GNSS static offsets
width: 500px
alt: High-rate GNSS recordings of the Ridgecrest M7.1 earthquake at stations spanning 10 to 70+ km hypocentral distance.
---
High-rate (1 Hz) GNSS recordings of the 2019 Ridgecrest M7.1 earthquake. Close stations show large permanent offsets; distant stations record seismic wave passage with little or no static displacement. Both effects are visible in the same time series.
```

👉 The same earthquake produces both effects. Which dominates depends on where you are.

---

## Why This Distinction Matters

The static offset is what we have been working with all term: coseismic displacements, fault locking, strain accumulation. These are the geodetic observables.

The dynamic waves carry additional information: fault geometry, rupture duration, source mechanism. To extract that information we need seismology.

In the lab today you will see both signals in the same dataset — high-rate GNSS from stations at different distances from the 2019 Ridgecrest M7.1 earthquake.

👉 GNSS and seismology are complementary datasets that record the same physical event.

---

# Earthquake Fault Geometry

## Describing a Fault Plane

Earthquakes are modeled as slip across a planar fault. The orientation of that plane and the direction of slip are described by three angles:

- **Strike** ($\phi$): the direction of the fault trace measured clockwise from north
- **Dip** ($\delta$): the angle of the fault surface below horizontal (0° = horizontal, 90° = vertical)
- **Rake** ($\lambda$): the direction of slip of the hanging wall measured within the fault plane from the strike direction
  - $\lambda = 0°$ → left-lateral strike-slip
  - $\lambda = 180°$ → right-lateral strike-slip
  - $\lambda = 90°$ → reverse (thrust) faulting
  - $\lambda = -90°$ → normal faulting

```{figure} ../figures/05_fault_geometry.png
---
name: Fault geometry
alt: Fault geometry defined by strike, dip, and rake.
width: 400px
---
A planar fault is fully described by the strike and dip of the fault surface and the rake of the slip vector within that plane.
```

---

## Fault Types and Tectonic Setting

The rake angle connects fault geometry directly to the tectonic environment.

**Normal faults** ($\lambda \approx -90°$)
- hanging wall moves down relative to footwall
- associated with crustal extension
- common at divergent boundaries and rifts

**Reverse / thrust faults** ($\lambda \approx 90°$)
- hanging wall moves up relative to footwall
- associated with crustal compression
- dominant at convergent boundaries and subduction zones

**Strike-slip faults** ($\lambda \approx 0°$ or $180°$)
- horizontal motion along the fault
- right-lateral or left-lateral
- dominant at transform boundaries

Fault geometry encodes the style of deformation and the tectonic stress field.

---

# Seismic Moment and Magnitude

## Scalar Seismic Moment

The physical size of an earthquake is described by the **scalar seismic moment**:

$$
M_0 = \mu \, D \, A
$$

where:
- $\mu$ = shear modulus of the crust (typically $\sim 30$ GPa)
- $D$ = average slip on the fault
- $A$ = rupture area

This is the same slip $D$ and area $A$ that appear in geodetic fault models — seismic moment is a direct bridge between seismology and geodesy.

```{figure} ../figures/05_seismogenic_zone.gif
---
name: Rupture geometry
alt: Fault rupture length, width, and slip.
width: 500px
---
Rupture length $L$, width $W$, and average slip $D$ determine the scalar seismic moment together with the shear modulus.
```

👉 Larger slip on a larger fault releases more moment — seismic moment is the fundamental physical measure of earthquake size.

---

## Worked Example: Ridgecrest M7.1

The July 6, 2019 Ridgecrest earthquake ruptured a NW-striking right-lateral fault in the eastern California shear zone.

From joint geodetic and seismic inversions (Liu et al. 2019):
- Rupture length $L \approx 50$ km
- Rupture width $W \approx 16$ km
- Average slip $D \approx 1.5$ m
- Shear modulus $\mu = 30$ GPa

**Step 1:** Compute rupture area

$$
A = L \times W = (50 \times 10^3)(16 \times 10^3) = 8.0 \times 10^{11} \text{ m}^2
$$

**Step 2:** Compute scalar seismic moment

$$
M_0 = \mu D A = (30 \times 10^9)(1.5)(8.0 \times 10^{11}) = 3.6 \times 10^{19}\ \mathrm{N{\cdot}m}
$$

**Step 3:** Convert to moment magnitude

$$
M_w = \frac{2}{3} \log_{10}(M_0) - 10.7
$$

where $M_0$ is in dyne-cm ($1 \mathrm{N{\cdot}m} = 10^7 \text{ dyne-cm}$):

$$
M_0 = 3.6 \times 10^{26} \text{ dyne-cm}
$$

$$
M_w = \frac{2}{3}(26.56) - 10.7 \approx 7.0
$$

The USGS catalog value is $M_w = 7.1$ — close agreement given the simplified uniform slip model.

👉 Seismic moment connects measurable fault properties directly to earthquake size.

---

## Moment Magnitude

**Moment magnitude** is defined as:

$$
M_w = \frac{2}{3} \log_{10}(M_0) - 10.7
$$

where $M_0$ is in dyne-cm.

Key properties:
- directly related to physical fault parameters ($\mu$, $D$, $A$)
- does not saturate for large earthquakes
- preferred scale for modern seismic hazard and geodetic studies

Because $M_w$ is logarithmic, each unit increase represents roughly a factor of 32 increase in seismic moment and a factor of ~10 in fault area or slip.

---

# Focal Mechanisms

## Beachball Diagrams

Earthquake focal mechanisms are displayed as **lower-hemisphere projections** called beachball diagrams. They are the seismological equivalent of a fault-plane solution — a compact summary of fault geometry readable at a glance.

```{figure} ../figures/05_beachballs.png
---
name: Focal mechanisms
width: 600px
alt: Examples of strike-slip, normal, and reverse fault focal mechanisms.
---
Focal sphere projections for the three main fault types. Compressional quadrants are shaded dark; dilatational quadrants are white. The two nodal planes divide the sphere into four quadrants.
```

**Reading a beachball:**
- Black (shaded) = compressional first motions
- White = dilatational first motions
- Normal faults → white center (P-axis near vertical)
- Reverse faults → black center (P-axis near horizontal)
- Strike-slip faults → four equal quadrants
- The two great circles are the fault plane and the auxiliary plane

With practice you can read fault type, slip direction, and approximate stress orientation directly from a beachball.

---

## Determining Focal Mechanisms from Seismic Data

The focal mechanism is determined from **P-wave first motions** recorded at many stations around the earthquake.

**Step 1:** Determine whether the first P-wave motion is upward (compressional) or downward (dilatational) at each station.

```{figure} ../figures/05_up_down.png
---
width: 800px
---
Upward and downward first motions on seismograms. The direction of initial ground motion at each station constrains the radiation pattern.
```

**Step 2:** Collect polarity observations from many stations and project rays back through the focal sphere using takeoff angles.

```{figure} ../figures/05_takeoff_angles.png
---
width: 300px
---
Polarity observations projected onto the focal sphere. Each station plots as a symbol (filled = compression, open = dilation) at the appropriate takeoff angle and azimuth.
```

**Step 3:** Find two orthogonal nodal planes separating compressional and dilatational quadrants. These give the strike, dip, and rake of the fault.

```{figure} ../figures/05_focal_mechanism.png
---
width: 600px
---
Fitting a focal mechanism to polarity observations. The two nodal planes are constrained to separate all compressional (filled) from dilatational (open) symbols.
```

👉 The focal mechanism provides strike, dip, and rake — the same parameters we use in geodetic fault models.

---

## The Fault Plane Ambiguity

Seismic radiation from a double-couple source is identical for two orthogonal fault planes — the **primary fault plane** and the **auxiliary plane**. First motions alone cannot tell them apart.

```{figure} ../figures/05_ambiguity.png
---
name: Fault plane ambiguity
width: 500px
---
A right-lateral fault on a N-striking plane and a left-lateral fault on an E-striking plane produce identical far-field radiation patterns. Additional information is needed to identify the true fault.
```

Resolving the ambiguity requires additional information:
- aftershock locations (they outline the true fault plane)
- mapped surface rupture
- geodetic or InSAR observations of the deformation pattern

👉 Seismology tells us the mechanism; geodesy often tells us which plane actually slipped.

---

# Green's Functions

## The Forward Problem in Seismology

A central goal of seismology is the **forward problem**:

> Given an earthquake source and Earth structure, predict the seismograms recorded at any station.

Seismic wave propagation in an elastic medium is governed by the elastic wave equation:

$$
\rho \frac{\partial^2 u_i}{\partial t^2} = \partial_j \tau_{ij} + f_i
$$

Solving this directly for every possible earthquake source and Earth structure would be prohibitively expensive. Instead, we precompute the Earth's response to a simple unit impulse — the **Green's function**.

---

## Green's Functions as the Earth's Impulse Response

The displacement at receiver location $\mathbf{x}$ due to a point force $f_j$ at source location $\mathbf{x}_0$ is:

$$
u_i(\mathbf{x}, t) = G_{ij}(\mathbf{x}, t; \mathbf{x}_0, t_0) \, f_j
$$

The Green's function $G_{ij}$ contains everything about wave propagation in the Earth — velocities, reflections, attenuation, geometric spreading. Once computed for a given Earth structure, it can be used for any source.

Because the elastic wave equation is linear:

$$
u_i = \sum_j G_{ij} \, f_j
$$

👉 Any complicated earthquake source can be represented as a sum of simple point-force solutions.

---

## Why Green's Functions Matter for This Course

You will encounter Green's functions again in Week 4 when we move to forward and inverse modeling of fault slip. The connection is direct:

- **Forward problem:** given fault geometry and slip → multiply by Green's functions → predict GNSS or InSAR displacements
- **Inverse problem:** given observed displacements → divide by Green's functions → solve for fault slip

The Okada elastic dislocation model you will use in Week 4 is essentially an analytic Green's function for a dislocation in a homogeneous elastic half-space.

👉 Green's functions are the mathematical engine behind both seismic source inversions and geodetic fault models.

---

## Source Time Functions

Real earthquakes do not happen instantaneously. Fault slip accumulates over seconds to minutes, and the seismic moment evolves as $M(t)$.

Far-field seismic waves depend on $\dot{M}(t)$ — the time derivative of the moment function. This is the **source time function**, and it controls:
- rupture duration
- frequency content of the radiated waves
- pulse shape on seismograms

```{figure} ../figures/05_ridgecrest_stf.png
---
name: Ridgecrest source time function
width: 700px
alt: Slip model and source-time functions for the 2019 Ridgecrest earthquake sequence.
---
Slip model and source-time functions for the 2019 Ridgecrest M6.4 (pink) and M7.1 (cyan) earthquakes from joint inversion of strong-motion, GNSS, and InSAR data. The M7.1 ruptures for ~12 seconds; the M6.4 for ~6 seconds.
```

👉 The source time function connects the static picture (total slip) to the dynamic picture (seismic waves).

---

# Seismotectonics

## Reading Stress from Focal Mechanisms

A single focal mechanism tells us about one earthquake. A **population of focal mechanisms** tells us about the regional stress field.

The P-axis (pressure axis) and T-axis (tension axis) are related to the principal compressive and tensile stresses. Where many earthquakes share a common stress field, their focal mechanisms show consistent P and T axis orientations even when individual fault orientations vary.

**Three stress regimes and their characteristic mechanisms:**

| Tectonic setting | Dominant mechanism | Characteristic beachball |
|---|---|---|
| Extensional | Normal faulting | White center |
| Compressional | Reverse/thrust faulting | Dark center |
| Strike-slip | Strike-slip faulting | Four-quadrant |

```{figure} ../figures/05_mendo_fms.jpg
---
width: 600px
---
Focal mechanisms along the Mendocino Transform Fault zone (Dengler et al. 1994). The dominant right-lateral strike-slip pattern reflects the transform boundary between the Pacific and North American plates, with some normal faulting in the extensional region to the east.
```

👉 A map of focal mechanisms is a map of the stress field.

---

## The Global Picture: CMT Catalog

The **Global Centroid Moment Tensor (CMT) Catalog** contains moment tensor solutions for large earthquakes recorded globally since 1976. It is one of the most widely used earthquake source databases in seismology.

```{figure} ../figures/05_global_red.gif
---
name: Global CMT catalog
width: 800px
---
The Global CMT catalog of shallow earthquakes 1976–2005. Focal mechanisms are plotted at their epicenters. Plate boundaries emerge directly from the spatial pattern of seismicity, and the style of faulting changes systematically: thrust mechanisms at subduction zones, strike-slip at transforms, normal faulting at ridges and continental rifts.
```

The global pattern makes plate boundaries visible from seismicity alone:
- **Subduction zones** — dominantly thrust mechanisms, curved arcs
- **Transform faults** — strike-slip mechanisms, linear chains
- **Mid-ocean ridges** — normal faulting, offset by transforms
- **Continental collision zones** — complex mix of thrust and strike-slip

👉 The CMT catalog is freely available at [globalcmt.org](https://www.globalcmt.org/) and is a primary data source for seismotectonic studies.

---

## The Ridgecrest Sequence: A Case Study

The 2019 Ridgecrest sequence is an excellent local example of seismotectonic analysis from focal mechanisms.

```{figure} ../figures/05_ridgecrest.png
---
width: 800px
---
Focal mechanisms of the 2019 Ridgecrest aftershock sequence (Atterholt et al. 2025). The mainshock (M7.1, large mechanism) ruptured a NW-striking right-lateral fault. The M6.4 foreshock ruptured a conjugate NE-striking left-lateral fault. Aftershocks illuminate both fault planes and reveal the complexity of the fault system in the eastern California shear zone.
```

Key observations:
- **Mainshock (M7.1):** NW-striking, right-lateral — consistent with the eastern California shear zone
- **Foreshock (M6.4):** NE-striking, left-lateral — a conjugate fault activated by the regional stress field
- **Aftershock focal mechanisms:** mixed, reflecting slip on both conjugate fault orientations
- The pattern is consistent with NW-SE maximum horizontal compression across the region

👉 The focal mechanism map tells the tectonic story of the sequence more completely than the epicenter map alone.

---

## Big Picture: What Seismology Adds to the Geodetic View

| Observable | What it measures | What it misses |
|---|---|---|
| Static GNSS offsets | Permanent coseismic displacement | Fault geometry ambiguity, rupture timing |
| InSAR | Spatial pattern of surface deformation | Temporal evolution, dynamic effects |
| Focal mechanisms | Fault geometry, slip direction, stress regime | Which nodal plane is the fault |
| Source time function | Rupture duration, moment release history | Spatial slip distribution |
| Finite fault model | Slip distribution in space and time | Requires combining all of the above |

The lectures ahead — InSAR, forward modeling, and inversion — build toward that last row: combining geodetic and seismic observations to recover the full picture of fault slip.

---

## Summary

- Earthquakes produce both **static** (permanent) and **dynamic** (transient) deformation. High-rate GNSS captures both in a single time series.
- Fault geometry is described by **strike, dip, and rake**, which also determine the style of deformation and the tectonic stress regime.
- **Scalar seismic moment** $M_0 = \mu D A$ is the fundamental physical measure of earthquake size, directly connecting seismology to geodetic fault parameters.
- **Moment magnitude** $M_w$ is derived from $M_0$ and does not saturate for large earthquakes.
- **Focal mechanisms** (beachballs) display the fault geometry inferred from P-wave first motions. The fault plane ambiguity is resolved using aftershocks, surface rupture, or geodetic data.
- **Green's functions** describe the Earth's response to a point source. They are the mathematical bridge between earthquake sources and observed seismograms — and between seismology and the geodetic inversion methods we will develop in Week 4.
- **Populations of focal mechanisms** reveal the regional stress field and tectonic setting — a map of mechanisms is a map of stress.

---

# Additional Resources

Shearer, *Introduction to Seismology*, Chapter 9, Section 2: Earthquake faults, Section 3: Radiation Patterns and Beachballs, and Section 1: Green's functions and the Moment Tensor
