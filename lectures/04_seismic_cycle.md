# GNSS IV: Deformation Through the Seismic Cycle

## Purpose

Earthquakes last seconds to minutes, but the deformation that produces and follows them spans decades to centuries.

In this lecture, we will:

- connect interseismic strain accumulation to coseismic slip
- recognize interseismic, coseismic, and postseismic GNSS signals
- use a simple elastic model to relate a velocity profile to fault slip rate and locking depth
- examine how fault creep changes where deformation accumulates
- connect slip deficit and recurrence interval to an earthquake moment budget

---

# An Earthquake Is One Brief Part of a Longer Cycle

```{figure} figures/05_seismic_cycle_timeseries.png
---
width: 850px
alt: Synthetic GNSS position time series showing interseismic loading, a coseismic offset, and postseismic deformation.
---
A station may record steady interseismic motion, a nearly instantaneous coseismic offset, and a decaying postseismic transient. The next loading interval begins before postseismic deformation has necessarily ended.
```

> **Ask:** Which part of this record would contribute to a velocity estimated from the entire time series?

---

# Reid Connected the 1906 Offsets to Elastic Rebound

Reid's interpretation of the 1906 San Francisco earthquake was that:

- steady plate motion gradually deforms the crust around a locked fault
- elastic strain accumulates over a long interval
- the fault eventually slips
- the surrounding crust rebounds toward a less strained configuration

```{figure} figures/05_reid_elastic_rebound.png
---
width: 650px
alt: Historical diagram illustrating elastic rebound across a strike-slip fault.
---
Conceptual illustration of elastic rebound used in the source seismic-cycle lecture. The pre-earthquake distortion records stored elastic strain; fault slip releases part of that strain.
```

---

# Interseismic Deformation Stores Elastic Strain

During the interseismic period:

- the shallow seismogenic fault may remain locked
- deeper parts of the plate boundary continue to move
- velocities vary across the fault
- the resulting velocity gradient represents elastic strain accumulation

This connects directly to the previous lecture: **spatial variation in velocity produces strain rate**.

---

# Coseismic Slip Produces Permanent Surface Offsets

The coseismic phase lasts seconds to minutes. GNSS and InSAR measure the resulting displacement field.

```{figure} figures/05_coseismic_insar.png
---
width: 760px
alt: InSAR observations of coseismic ground displacement.
---
An InSAR coseismic displacement field from the source lecture (Feng et al., 2010). The spatial pattern constrains fault location, geometry, and slip.
```

Offset direction and amplitude depend on fault strike, dip, rake, depth, dimensions, and slip.

---

# A Network Sees More Than a Single Station

Different representations emphasize different parts of the earthquake cycle:

| Observation | What it records | Typical units |
|---|---|---|
| Position time series | Evolution at one station | mm |
| Interseismic velocity field | Ongoing loading and creep | mm/yr |
| Coseismic offsets | Permanent earthquake displacement | mm to m |
| Postseismic velocity or displacement | Continuing response after rupture | mm/yr or mm |

The physical interpretation comes from both the temporal evolution and the spatial pattern.

---

# A Locked Strike-Slip Fault Produces a Broad Velocity Gradient

Imagine an infinitely long vertical strike-slip fault:

- below depth $D$, the two sides move steadily at relative rate $V$
- above $D$, the fault is locked
- the surrounding elastic crust deforms to accommodate the mismatch

Far from the fault, the two sides approach velocities of $-V/2$ and $+V/2$. Near the fault, the velocity changes smoothly.

---

# The Arctangent Model Describes the Interseismic Profile

For fault-perpendicular distance $x$,

$$
v_{\parallel}(x)=c+\frac{V}{\pi}\tan^{-1}\left(\frac{x}{D}\right).
$$

- $v_{\parallel}$: fault-parallel surface velocity
- $V$: long-term relative slip rate
- $D$: locking depth
- $c$: reference-frame or block-translation offset

This is a deliberately simple model: one vertical fault, uniform slip below one locking depth, homogeneous elastic material, and no neighboring faults.

---

# Slip Rate and Locking Depth Affect Different Features

```{figure} figures/05_arctan_locking_depth.png
---
width: 720px
alt: Arctangent velocity profiles for three different locking depths.
---
Slip rate controls the far-field velocity difference. Locking depth controls how broadly the transition is distributed across the fault.
```

> **Prediction:** Which locking depth produces the largest velocity gradient immediately adjacent to the fault?

---

# Rotate the GNSS Data Into Fault Coordinates

For fault strike $\alpha$, clockwise from north,

$$
v_{\parallel}=v_E\sin\alpha+v_N\cos\alpha.
$$

We also project station positions onto axes parallel and perpendicular to the fault.

This rotation does not change the motion. It expresses the observations in coordinates that make the fault mechanics easier to see.

---

# Real San Andreas Deformation Is Distributed

```{figure} figures/05_interseismic_california.png
---
width: 680px
alt: California map and velocity profile showing deformation distributed across multiple faults.
---
Interseismic deformation near the San Andreas system is distributed among multiple faults and tectonic blocks (Shen et al., 1997, as reproduced in the source lecture). A single-fault profile is therefore an approximation, not a complete regional model.
```

Residual patterns are scientifically useful: they can reveal secondary faults, block rotation, creep, or an inappropriate fault geometry.

---

# Fault Creep Changes Where Motion Occurs

**Locked fault:** relative plate motion is stored as broad elastic strain around the fault.

**Creeping fault:** some relative motion reaches the surface continuously or episodically.

The coupling fraction $C$ describes the fraction of long-term motion accumulating as slip deficit:

- $C=1$: fully coupled
- $C=0$: freely creeping
- $0<C<1$: partially coupled

---

# Locking and Creep Can Produce the Same Far-Field Rate

```{figure} figures/05_coupling_creep_profiles.png
---
width: 720px
alt: Velocity profiles for fully locked, partially coupled, and freely creeping strike-slip faults.
---
All three profiles accommodate the same long-term relative motion. What changes is whether deformation is broadly stored in the crust or localized as creep near the fault.
```

This is why far-field plate motion alone does not determine earthquake potential.

---

# Slip Deficit Links Interseismic Loading to Future Slip

For constant long-term rate $V$, coupling $C$, and elapsed time $T$,

$$
S_{deficit}=CVT.
$$

Example:

$$
(1)(36\ \mathrm{mm/yr})(150\ \mathrm{yr})=5.4\ \mathrm{m}.
$$

This is a kinematic budget. It does not require that all accumulated deficit be released in one earthquake.

---

# Slip Deficit Can Be Expressed as a Moment Budget

If a rupture of length $L$ and width $W$ releases average slip $S$,

$$
M_0=\mu LWS,
$$

and, using SI units,

$$
M_w=\frac{2}{3}\left(\log_{10}M_0-9.1\right).
$$

The estimate depends on rupture dimensions, shear modulus, coupling, recurrence interval, and the fraction of the deficit released coseismically.

---

# Longer Recurrence Builds More Slip—but Magnitude Is Logarithmic

```{figure} figures/05_recurrence_magnitude.png
---
width: 820px
alt: Slip deficit and equivalent moment magnitude plotted against recurrence interval.
---
For fixed rupture dimensions, slip deficit increases linearly with time, whereas moment magnitude increases logarithmically.
```

> **Ask:** Why is this an earthquake-equivalent moment budget rather than a prediction of the next earthquake magnitude?

---

# Parkfield Shows That Recurrence Is Not Clockwork

```{figure} figures/05_parkfield_recurrence.png
---
width: 680px
alt: Historical Parkfield earthquake sequence and recurrence forecast.
---
The Parkfield earthquakes appeared approximately characteristic and quasiperiodic, motivating a prediction before 1993. The next magnitude 6 earthquake occurred in 2004. Historical recurrence graphic after Bakun and McEvilly (1984), as reproduced in the source lecture.
```

Recurrence intervals summarize past behavior. Fault interactions, variable stress, aseismic slip, and incomplete records limit deterministic forecasts.

---

# Postseismic Deformation Starts Immediately After Rupture

```{figure} figures/05_nankai_postseismic.png
---
width: 610px
alt: Historical postseismic geodetic time series following the 1946 Nankai earthquake.
---
Postseismic deformation following the 1946 Nankai earthquake, after Savage (1995), as presented in the source lecture.
```

The postseismic signal can persist for months to decades and bias a velocity interpreted as steady interseismic loading.

---

# Several Processes Produce Postseismic Motion

| Mechanism | Where it occurs | Typical spatial signature | Typical timescale |
|---|---|---|---|
| Afterslip | On or near the fault | Fault-centered; related to rupture geometry | Days to years |
| Poroelastic rebound | Fluid-bearing crust around the rupture | Near field; may reverse across structures | Days to months |
| Viscoelastic relaxation | Lower crust and upper mantle | Broad, long-wavelength response | Years to decades |

These mechanisms may occur simultaneously. Distinguishing them requires spatial coverage, time dependence, and mechanical models.

---

# The Simple Profile Opens the Door to Modeling

In the lab, you will:

1. rotate North America-fixed GNSS velocities into San Andreas coordinates
2. construct a fault-perpendicular velocity profile
3. fit slip rate, locking depth, and a velocity offset
4. examine how creep changes the predicted profile
5. convert a slip-deficit rate and recurrence interval into a moment budget

Next week, we will ask more generally how forward and inverse models connect fault processes to surface deformation.

---

# Seismic-Cycle Summary

- Interseismic velocity gradients record strain accumulation around locked faults.
- Coseismic offsets record rapid fault slip and elastic rebound.
- Locking depth controls the width of an idealized interseismic velocity profile.
- Creep reduces the fraction of plate motion stored as slip deficit.
- Slip deficit provides an earthquake moment budget, not a deterministic prediction.
- Postseismic deformation reflects several overlapping fault and rheological processes.

---

# Sources

- Reid, H. F. (1910), *The Mechanics of the Earthquake*, in *The California Earthquake of April 18, 1906*.
- Savage, J. C. and Burford, R. O. (1973), Geodetic determination of relative plate motion in central California.
- Kreemer, C., Hammond, W. C., and Blewitt, G. (2022), *Crustal Strain Rates in the Western United States and Their Relationship with Earthquake Rates*.
- Kreemer et al. velocity data: [doi:10.7910/DVN/BICMWB](https://doi.org/10.7910/DVN/BICMWB).
- Additional figures and examples adapted from the supplied `07_seismic_cycle.pptx`; original citations are retained in captions where available.
