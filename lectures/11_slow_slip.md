# Slow Slip Events and the Spectrum of Fault Slip

## Purpose

In the seismic cycle lecture we established the four-phase cycle of interseismic loading,
coseismic rupture, postseismic relaxation, and renewed locking — and noted that some
fault zones slip aseismically, either continuously or in episodic bursts. In this
lecture we examine those episodic aseismic events in detail.

**Slow slip events** (SSEs) occupy a remarkable middle ground: they release accumulated
strain over days to months, produce measurable surface deformation, and in subduction
zones are often accompanied by low-frequency seismic signals — yet they cause no felt
shaking and were largely invisible to seismologists before the GNSS era.

Understanding slow slip matters because:
- SSEs occur on the same faults that generate megathrust earthquakes, immediately
  downdip of the locked zone
- They modulate the stress on the locked zone with each cycle
- Their recurrence, location, and moment budget are key inputs to seismic hazard assessment
- Their physics illuminates fault friction at the transition between stable and unstable
  sliding — a regime we cannot access directly

In this lecture we will:

- place slow slip on the **spectrum of fault slip behaviors**
- describe what an SSE looks like in GNSS and seismic data
- explain the fault mechanics that produce slow slip
- characterize Cascadia SSEs in detail — the best-observed examples
- connect SSEs to the locked zone and the seismic cycle
- set up the quantitative inversion problem you will solve in the lab

---

# The Spectrum of Fault Slip

---

## From Fast to Slow

Fault slip occurs across an enormous range of timescales. Organizing these behaviors
into a spectrum reveals that "earthquake" and "creep" are the endpoints of a continuum
with rich structure in between.

```{figure} ../figures/12_slip_spectrum.png
---
width: 720px
alt: Diagram showing fault slip behaviors arranged by duration — from regular earthquakes
     (seconds) through slow slip events (days to months) to steady creep — with moment
     rate plotted against duration and lines of constant stress drop.
---
The spectrum of fault slip behaviors, adapted from Ide et al. (2007). Regular earthquakes
(upper left) have short durations and high moment rates — they are seismically efficient.
Low-frequency earthquakes (LFEs), very low frequency earthquakes (VLFEs), and slow slip
events (SSEs) have progressively longer durations at the same moment. Steady creep (lower
right) releases moment continuously. The dashed lines show constant stress drop — regular
earthquakes have stress drops of 1–100 MPa; SSEs have stress drops of order 0.001–0.01 MPa.
After Ide et al. (2007); Beroza & Ide (2011).
```

| Slip behavior | Duration | Stress drop | Seismic? | Observable |
|---|---|---|---|---|
| Regular earthquake | Seconds | 1–100 MPa | Yes | Seismograms, GNSS offset |
| Low-frequency earthquake (LFE) | Seconds | ~0.01 MPa | Marginally | Specialized filtering |
| Very low frequency earthquake (VLFE) | Minutes–hours | ~0.001 MPa | Barely | Long-period seismology |
| Slow slip event (SSE) | Days–months | ~0.001 MPa | No | GNSS time series |
| Steady aseismic creep | Continuous | — | No | GNSS velocity, creepmeter |

👉 The key insight: **stress drop decreases as duration increases**. This is not a
coincidence — it reflects the underlying friction physics that we will discuss below.

---

## Why Is Slow Slip "Slow"?

A regular earthquake propagates at roughly the shear wave speed (~3 km/s). A slow slip
event propagates at ~1–10 km/day — roughly a factor of 10,000 slower. This enormous
difference in propagation speed reflects fundamentally different friction behavior.

**Regular earthquakes** occur on velocity-weakening faults: as slip rate increases,
friction drops, which accelerates slip further — runaway instability. The process is
self-sustaining and radiates seismic energy efficiently.

**Slow slip events** occur in a narrow frictional regime: velocity-strengthening but
near-neutral — friction increases slightly with slip rate, preventing runaway, but the
stabilizing effect is weak enough that slip can still accelerate beyond the background
loading rate. The result is slip that is faster than interseismic loading but far slower
than an earthquake.

The transition between these behaviors — the **velocity-neutral to weakly
velocity-strengthening regime** — is where SSEs live. This regime is thought to exist
at specific pressure–temperature conditions on subduction interfaces, explaining why
SSEs occupy a narrow depth range.

---

# What Does a Slow Slip Event Look Like?

---

## In GNSS Data

A slow slip event appears in a GNSS time series as a **transient offset** — a gradual
step that occurs over days to weeks, superimposed on the background secular trend and
seasonal signals. In Lab 2 you identified the 2015–2016 Cascadia SSE at station ALBH
by fitting and removing the trend and seasonal components.

```{figure} ../figures/12_albh_sse.png
---
width: 720px
alt: GNSS time series at ALBH showing the east component from 2010 to 2025, with
     trend and seasonal terms removed. Multiple westward transients are visible,
     each corresponding to a Cascadia SSE. The 2015-2016 event is highlighted.
---
East component residual time series at ALBH (southern Vancouver Island) after removing
the interseismic trend and seasonal terms. Each westward transient corresponds to a
Cascadia SSE. The 2015–2016 event (highlighted) is clearly the largest in this record.
The regularity of events — roughly every 12–14 months — is apparent. After Bartlow (2020).
```

Key observational characteristics:
- **Direction:** westward and slightly downward at coastal stations — the opposite of
  interseismic loading, consistent with slip on the thrust interface
- **Amplitude:** 2–10 mm horizontally at coastal stations for northern Cascadia events
- **Duration:** 2–4 weeks for typical northern Cascadia SSEs; months for southern Cascadia
- **Decay:** gradual onset and termination, no impulsive arrival

---

## In Seismic Data

SSEs produce no felt shaking — they are seismically silent. But they are accompanied by
a distinctive seismic signal that was only recognized once high-sensitivity broadband
instruments were deployed: **tectonic tremor**.

**Tectonic tremor** is a long-duration, emergent seismic signal that:
- lacks the clear P and S arrivals of regular earthquakes
- has dominant frequencies of 1–10 Hz (lower than typical local earthquakes)
- migrates along strike at 5–30 km/day — tracking the propagation of the slow slip front
- is thought to be generated by swarms of small LFEs on the subduction interface

```{figure} ../figures/12_tremor_gnss.png
---
width: 720px
alt: Three-panel figure showing tremor activity, GNSS east displacement, and GNSS
     north displacement during a Cascadia SSE episode, illustrating the simultaneous
     onset of tremor and surface displacement.
---
Simultaneous tremor activity (top) and GNSS surface displacement at ALBH during a
Cascadia SSE (bottom two panels). Tremor onset coincides with the start of the surface
displacement transient. As the slow slip propagates along strike, the tremor migrates
accordingly. This space-time correlation established that tremor is driven by the
underlying slip, not vice versa. After Rogers & Dragert (2003).
```

👉 **Episodic tremor and slip (ETS)** is the name given to the combined phenomenon —
the simultaneous occurrence of slow slip and tremor that was first described in Cascadia
by Rogers & Dragert (2003). The ETS discovery was transformative: it revealed that
subduction interfaces are not simply locked between large earthquakes but are
dynamically active throughout the seismic cycle.

---

## Spatial Pattern

The surface displacement pattern of an SSE is subtle — a few millimeters of westward
motion spread across hundreds of kilometers of coastline — and requires a dense
network to map. The pattern provides the key observational constraint on the depth and
along-strike extent of the slip.

```{figure} ../figures/12_sse_map.png
---
width: 700px
alt: Map of the Cascadia subduction zone showing GNSS displacement vectors during
     the 2015-2016 SSE, with arrows pointing westward and slightly southward at
     coastal stations in Washington and southern BC.
---
GNSS displacement field during the 2015–2016 Cascadia SSE. Arrows show the
horizontal displacement measured at coastal stations in Washington and southern BC.
The predominantly westward displacement is consistent with reverse slip on the
subduction interface. The pattern — largest near the coast and decaying inland —
constrains the depth and extent of the slip in the inversion you will do in Lab 12.
After Bartlow (2020).
```

---

# Cascadia: The Best Laboratory

---

## Why Cascadia?

The Cascadia subduction zone is the best-studied SSE system in the world for several reasons:

- **Dense GNSS network:** PNSN, PANGA, and the Canadian CACS network together provide
  continuous measurements at hundreds of stations across Washington, Oregon, and BC
- **Well-defined geometry:** the Juan de Fuca plate interface is relatively simple and
  well-constrained by earthquake relocations, seismic reflection, and the McCrory et al.
  and Slab2 interface models
- **Regular, well-separated events:** northern Cascadia SSEs recur every 12–14 months
  with remarkable regularity, enabling statistical analysis
- **Rapid scientific response:** the discovery of ETS in Cascadia in 2003 launched an
  intensive observational effort that has now produced two decades of well-documented events

---

## The Structure of Cascadia SSEs

Cascadia SSEs are not a single phenomenon — they vary systematically along strike in
duration, recurrence, and depth.

```{figure} ../figures/12_cascadia_segments.png
---
width: 700px
alt: Map of Cascadia showing the along-strike segmentation of SSE behavior — short,
     frequent events in the north, longer, less frequent events in the south, with
     intermediate behavior in Oregon.
---
Along-strike segmentation of Cascadia SSE behavior. Northern Cascadia (Vancouver Island
and Washington) hosts short-duration (~2 week), high-frequency (~14 month) events.
Southern Cascadia (northern California) hosts longer-duration (months), lower-frequency
events. Oregon is intermediate. This segmentation reflects variations in the thermal
structure, plate geometry, and frictional properties of the interface. After Bartlow (2020).
```

**Northern Cascadia (46–50°N):**
- Duration: 1–4 weeks
- Recurrence: ~12–14 months
- Depth: 25–40 km
- Mw: ~6.3–6.8 per event
- Well-defined propagation from NW to SE or vice versa

**Oregon (44–46°N):**
- Duration: weeks to a few months
- Recurrence: ~12–18 months
- Behavior is more complex and less regular

**Southern Cascadia/Northern California (40–44°N):**
- Duration: months to over a year
- Recurrence: irregular, multi-year
- Less well-constrained by the sparser network

---

## The Moment Budget

SSEs release accumulated strain — but how much, and how does it compare to the seismic
moment deficit building on the locked zone?

The seismic moment of an SSE can be estimated from the slip distribution recovered by
GNSS inversion (as you will do in Lab 12):

$$M_0^{SSE} = \mu \sum_k A_k s_k$$

where $A_k$ is the area of patch $k$ and $s_k$ is the recovered slip.

For northern Cascadia, individual SSEs have Mw~6.5, releasing roughly 1–3 cm of slip
over a fault area of order $10^{10}$ m².

The **long-term convergence rate** at northern Cascadia is ~40 mm/yr. If SSEs recur
every 14 months and release ~2 cm of slip each time, the average SSE slip rate is:

$$\dot{s}_{SSE} \approx \frac{20\text{ mm}}{1.2\text{ yr}} \approx 17\text{ mm/yr}$$

This is roughly **40% of the total convergence rate** — the SSEs are not a minor
perturbation but a major component of the strain budget. The remaining 60% must either
accumulate as elastic strain on the locked zone (to be released seismically) or be
accommodated by other aseismic processes.

👉 This moment budget argument is one of the reasons Cascadia SSEs are considered
seismically significant: they are continuously modulating the stress state of the
locked zone above them.

---

## Stress Transfer to the Locked Zone

Each SSE loads the locked zone incrementally. The geometry is straightforward: the SSE
slip patch is downdip of the locked zone, and slip on it transfers stress updip.

```{figure} ../figures/12_stress_transfer.png
---
width: 700px
alt: Cross-section of the Cascadia subduction zone showing the locked zone above,
     the SSE slip zone in the transition region, and arrows indicating stress transfer
     from the SSE patch to the locked zone updip.
---
Stress transfer from SSEs to the locked zone. Each SSE episode increases the Coulomb
failure stress on the locked zone by a small amount — typically 0.001–0.01 MPa. While
individually small, the cumulative effect of hundreds of SSE cycles over the centuries
between megathrust earthquakes is non-negligible. Whether SSEs advance or delay the
next megathrust earthquake depends on the stress state of the locked zone, which we
cannot directly observe. After Mazzotti & Adams (2004).
```

The stress increment per SSE cycle is small (~0.001–0.01 MPa), but over the centuries
between Cascadia megathrust earthquakes (the last was in January 1700) hundreds of SSE
cycles have accumulated. Whether this stress loading advances the timing of the next
megathrust, or whether the SSEs actually relieve stress by creeping past the locking
boundary, is an active research question.

---

# The Physics of Slow Slip

---

## Rate-and-State Friction

The frictional behavior of faults is well described by **rate-and-state friction** — an
empirical framework that captures how friction depends on slip rate and the history
of contact at the sliding interface.

The basic form is:

$$\mu = \mu_0 + a\ln\!\left(\frac{V}{V_0}\right) + b\ln\!\left(\frac{V_0\theta}{D_c}\right)$$

where:
- $V$ is slip rate
- $\theta$ is a state variable (evolving contact "age")
- $a$, $b$ are dimensionless friction parameters
- $D_c$ is a critical slip distance

The key parameter is $a - b$:
- $a - b > 0$: **velocity strengthening** — friction increases with slip rate, stabilizing
  slip. Fault creeps stably. No earthquakes.
- $a - b < 0$: **velocity weakening** — friction drops with slip rate, destabilizing
  slip. Earthquake nucleation can occur.
- $a - b \approx 0$: **velocity neutral** — slip is marginally stable. SSEs can occur.

```{figure} ../figures/12_rate_state_ab.png
---
width: 700px
alt: Depth profile of the (a-b) parameter on the Cascadia interface, showing velocity-
     weakening (negative a-b) in the locked zone, a transition zone at 20-35 km where
     slow slip occurs, and velocity-strengthening (positive a-b) below.
---
Schematic depth profile of the rate-and-state parameter $(a-b)$ on the Cascadia
subduction interface. The seismogenic zone (locked, earthquakes possible) has
$(a-b) < 0$. The transition zone at 20–35 km, where SSEs and tremor occur, has
$(a-b) \approx 0$ — marginally stable. Below ~40 km the interface is velocity-
strengthening ($(a-b) > 0$) and creeps steadily. The exact depths depend on temperature
and lithology.
```

---

## Why the Transition Zone?

The velocity-neutral regime that produces SSEs occurs in a specific pressure–temperature
window on subduction interfaces. Two mechanisms have been proposed:

**Thermal control:** At temperatures of roughly 350–450°C, phyllosilicate minerals
(clays, talc, serpentinite) that are velocity-strengthening at lower temperatures
transition to velocity-weakening or velocity-neutral behavior. This thermal window
corresponds to the ~25–40 km depth range where SSEs occur on the Cascadia interface.

**Fluid pressure:** High pore fluid pressure reduces effective normal stress, bringing
the fault closer to failure and potentially shifting the stability boundary. The downdip
edge of the locked zone — where subducted oceanic crust begins to dehydrate — is a
natural source of high-pressure fluids. The correlation of tremor and SSEs with regions
of elevated Vp/Vs ratios (interpreted as high fluid content) supports this mechanism.

Both mechanisms likely operate simultaneously, and their relative importance varies
along strike — which may explain the along-strike segmentation of SSE behavior described
above.

---

## SSE Propagation

Individual SSE episodes in Cascadia propagate along strike at ~5–15 km/day. This is
orders of magnitude slower than seismic wave propagation but much faster than plate
convergence. The propagation is thought to reflect the cascade of stress transfer:
as slip occurs on one patch, the stress on the adjacent downdip patch increases above
the threshold for slow slip nucleation.

The propagation velocity itself provides constraints on the frictional parameters —
specifically the product $(a-b)\sigma_n$ where $\sigma_n$ is the effective normal stress.
Lower effective normal stress (higher pore pressure) predicts faster propagation,
consistent with observations in high-fluid-content regions.

---

# From Observation to Inversion

---

## The Inverse Problem for SSEs

In Lab 12 you will invert the GNSS surface displacement field of the 2015–2016 Cascadia
SSE for the spatial distribution of slip on the interface. This is exactly the same
linear inverse problem from the lecture and Lab 11, applied to a real dataset.

The key steps are:

**1. Data extraction:** fit and remove the interseismic trend and seasonal terms from
GNSS time series at multiple stations (as in Lab 2), then measure the SSE displacement
as the difference between pre- and post-event window means. The uncertainties
$\sigma_{offset}$ populate the diagonal of the data covariance matrix $\mathbf{C}_d$.

**2. Fault geometry:** we use the McCrory et al. triangulated Cascadia interface mesh,
restricted to the SSE depth range (8–35 km) in northern Cascadia (46–50°N). This gives
526 triangular patches representing the subduction interface where slip is expected.

**3. Green's function matrix:** using cutde (triangular dislocation elements), we compute
the surface displacement at each GNSS station due to unit thrust slip on each fault patch.
The slip direction is constrained to updip (reverse/thrust) — the direction consistent with
the Juan de Fuca plate subducting beneath the North American plate.

**4. Inversion:** we solve the weighted, damped, non-negative least-squares problem:

$$\min_{\mathbf{m} \geq 0} \left\| \mathbf{W}(\mathbf{G}\mathbf{m} - \mathbf{d}) \right\|^2 + \lambda^2\|\mathbf{m}\|^2$$

The non-negativity constraint enforces thrust-only slip. We choose $\lambda$ using the
L-curve, then compute the resolution matrix to understand what spatial scales of slip
we can actually recover from the land-based network.

---

## What the Data Can and Cannot Tell Us

Before interpreting the results, it is important to understand the fundamental limitations
of the inversion:

**Resolution decreases with depth:** shallow patches near the coast are well-constrained
by the GNSS network; deep patches (>35 km) beneath the Cascades are poorly resolved. The
resolution matrix quantifies this explicitly.

**The network is one-sided:** all stations are on land, east of the trench. Offshore
deformation — the largest signal, directly above the slip patch — is unmeasured. This
limits our ability to localize the trench-ward edge of the SSE.

**Horizontal is better constrained than vertical:** east and north displacements from
thrust slip are well-resolved by horizontal GNSS; vertical displacements are noisier.
We use only horizontal components.

**Regularization introduces bias:** the non-negativity constraint and damping both bias
the recovered slip toward smaller values. The true peak slip is likely larger than what
the inversion recovers, especially for patches with low resolution.

👉 A good seismologist interprets the slip distribution alongside the resolution matrix,
not just the slip map alone.

---

# Summary

- **Slow slip events** occupy a middle ground in the spectrum of fault slip behaviors —
  they release strain over days to months, produce measurable GNSS signals, and are
  accompanied by tectonic tremor, but cause no felt shaking.

- The **rate-and-state friction framework** provides a physical explanation: SSEs
  occur in a velocity-neutral to weakly velocity-strengthening frictional regime that
  exists in a specific pressure–temperature window on subduction interfaces, typically
  at 25–40 km depth.

- **Cascadia SSEs** are the best-observed examples — recurrent, regular (~12–14 month
  period in northern Cascadia), with individual events releasing Mw~6.5 equivalent
  moment and producing 1–10 mm of surface displacement at coastal GNSS stations.

- SSEs collectively release ~40% of the long-term convergence budget, making them
  a major component of the strain cycle. Each event incrementally loads the locked
  zone updip, potentially influencing the timing of future megathrust earthquakes.

- The **geodetic inverse problem** for SSEs maps the GNSS surface displacement field
  to a slip distribution on the fault interface. The key challenges are the strongly
  underdetermined system (many more fault patches than observations), the need for
  regularization, and the resolution limitation imposed by the land-only network.

- The **resolution matrix** is essential for interpreting the inversion result — it
  quantifies how much the recovered slip at each patch is blurred by regularization
  and constrained by the data coverage.

---

# Additional Resources

> **Discovery paper:** [Episodic tremor and slip on the Cascadia subduction zone](https://doi.org/10.1126/science.1084783)  
> Rogers, G., & Dragert, H. (2003). *Science*, 300(5627), 1942–1943.
> The paper that identified ETS in Cascadia, launched a decade of research.

> **Review:** [A long-term view of episodic tremor and slip in the Pacific Northwest](https://doi.org/10.1029/2019GL085303)  
> Bartlow, N. M. (2020). *Geophysical Research Letters*, 47.
> Comprehensive catalog of Cascadia SSEs from 2007–2019; the source of the SSE timing used in Lab 12.

> **Spectrum of slip:** [Slow earthquakes and nonvolcanic tremor](https://doi.org/10.1029/2011RG000371)  
> Beroza, G. C., & Ide, S. (2011). *Reviews of Geophysics*, 49.
> Excellent review of the full spectrum of fault slip behaviors and their physical interpretation.

> **Friction physics:** [Rate and state dependent friction and the stability of sliding between tectonic plates](https://doi.org/10.1029/JB093iB08p08659)  
> Ruina, A. (1983). *Journal of Geophysical Research*, 88(B8), 10,359–10,370.
> The foundational paper on rate-and-state friction. Worth reading for the derivation.

> **Cascadia SSE catalog:** [Pacific Northwest Seismic Network tremor catalog](https://pnsn.org/tremor)  
> Real-time and historical tremor locations in Cascadia.

> **Interface geometry:** [Juan de Fuca slab geometry](https://doi.org/10.1029/2012JB009407)  
> McCrory et al. (2012). *Journal of Geophysical Research*, 117.
> The plate interface model used in Lab 12.

---

# Sources

- Rogers, G., & Dragert, H. (2003). Episodic tremor and slip on the Cascadia subduction
  zone: the chatter of silent slip. *Science*, 300(5627), 1942–1943.
  https://doi.org/10.1126/science.1084783
- Bartlow, N. M. (2020). A long-term view of episodic tremor and slip in the Pacific
  Northwest. *Geophysical Research Letters*, 47. https://doi.org/10.1029/2019GL085303
- Beroza, G. C., & Ide, S. (2011). Slow earthquakes and nonvolcanic tremor. *Reviews of
  Geophysics*, 49. https://doi.org/10.1029/2011RG000371
- Ide, S., Beroza, G. C., Shelly, D. R., & Uchide, T. (2007). A scaling law for slow
  earthquakes. *Nature*, 447, 76–79. https://doi.org/10.1038/nature05780
- Ruina, A. (1983). Slip instability and state variable friction laws. *Journal of
  Geophysical Research*, 88(B8), 10,359–10,370. https://doi.org/10.1029/JB088iB12p10359
- Mazzotti, S., & Adams, J. (2004). Variability of near-term probability for the next
  great earthquake on the Cascadia subduction zone. *Bulletin of the Seismological
  Society of America*, 94(5), 1954–1959. https://doi.org/10.1785/012004032
- McCrory, P. A., Blair, J. L., Waldhauser, F., & Oppenheimer, D. H. (2012). Juan de
  Fuca slab geometry and its relation to Wadati-Benioff zone seismicity. *Journal of
  Geophysical Research*, 117. https://doi.org/10.1029/2012JB009407
- Schmalzle, G. M., McCaffrey, R., & Creager, K. C. (2014). Central Cascadia subduction
  zone creep. *Geochemistry, Geophysics, Geosystems*, 15(4), 1515–1532.
  https://doi.org/10.1002/2013GC005172
