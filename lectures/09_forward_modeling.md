# Elastic Dislocation — The Forward Problem

## Purpose

Faults are surfaces of displacement discontinuity embedded in the crust. When a fault slips, the surrounding rock deforms elastically, and the surface above it moves in a pattern that depends on the fault's geometry, depth, and slip distribution.

In this lecture, we will:

- establish why an elastic half-space is a useful model for the crust
- define a Green's function in the context of fault mechanics
- build intuition for how depth, dip, rake, and slip heterogeneity shape the surface signal
- introduce `cutde`, a modern implementation of the triangular dislocation element
- apply the forward model to a strike-slip earthquake and to a subduction zone
- use forward modeling to constrain the offshore extent of the 1700 Cascadia earthquake
- preview how the same Green's function matrix is used in the inverse problem

---

# Why an Elastic Half-Space?

The crust is not elastic everywhere or at all timescales. Over millions of years it flows viscously. Over a seismic cycle of centuries, however, the upper ~30 km behaves predominantly as an **elastic solid**: stress and strain are proportional, deformation is recoverable, and signals propagate instantaneously relative to tectonic timescales.

The simplest useful model is a **homogeneous, isotropic, linear elastic half-space**: a flat-topped solid that extends to infinite depth, described by two constants:

- **Lamé parameter** $\lambda$ and **shear modulus** $\mu$, or equivalently Poisson's ratio $\nu = \lambda / (2\lambda + 2\mu)$.
- For a **Poisson solid**, $\lambda = \mu$, so $\nu = 0.25$. This is a good approximation for most crustal rock.

This model is simpler than the real Earth — it ignores topography, layering, viscoelastic relaxation, and fluid effects — but it captures the dominant signal from most crustal earthquakes and interseismic loading to a useful approximation.

> **Check:** A typical crustal shear modulus is $\mu = 30$ GPa. If a fault patch slips 2 m, what is the order of magnitude of stress drop? (Hint: stress drop $\Delta\sigma \approx \mu \cdot \bar{s} / L$ where $L$ is the patch dimension.)

---

## The Boundary Value Problem

A fault is modeled as an **internal surface of displacement discontinuity** in the elastic half-space. The displacement jump $\mathbf{s}$ (the slip vector) is specified; the goal is to find the resulting displacement $\mathbf{u}(\mathbf{x})$ everywhere in the medium, and in particular at the free surface $z = 0$.

The governing equations are simply those of static linear elasticity:

$$
\nabla \cdot \boldsymbol{\sigma} = 0, \qquad \boldsymbol{\sigma} = \lambda\,\text{tr}(\boldsymbol{\epsilon})\,\mathbf{I} + 2\mu\,\boldsymbol{\epsilon}
$$

with the boundary condition that the free surface is traction-free:

$$
\boldsymbol{\sigma} \cdot \hat{\mathbf{n}}\big|_{z=0} = \mathbf{0}.
$$

The problem is linear. This fact is what makes everything that follows possible.

---

# Green's Functions and Linearity

**Linearity** means that if slip $\mathbf{s}_1$ on a patch produces surface displacement $\mathbf{u}_1$, and slip $\mathbf{s}_2$ on the same patch produces $\mathbf{u}_2$, then slip $\alpha \mathbf{s}_1 + \beta \mathbf{s}_2$ produces $\alpha \mathbf{u}_1 + \beta \mathbf{u}_2$.

A **Green's function** $G_{ij}(\mathbf{x}; \mathbf{x}_k)$ is the displacement at surface point $\mathbf{x}$ in direction $i$ caused by **1 m of slip** on fault patch $k$ in direction $j$. Once we know the Green's functions for every patch and every observation point, we can predict the surface displacement for any slip distribution by superposition:

$$
u_i(\mathbf{x}) = \sum_{k} \sum_{j} G_{ij}(\mathbf{x};\mathbf{x}_k) \, s_{kj}.
$$

In matrix form, collecting all observation points and both slip components into vectors:

$$
\boxed{\mathbf{d} = \mathbf{G}\mathbf{s}}
$$

where:

- $\mathbf{d}$ is the data vector — surface displacements at all observation points and components
- $\mathbf{G}$ is the **Green's function matrix** — computed once from geometry and elastic constants
- $\mathbf{s}$ is the slip vector — what we want to estimate in the inverse problem

> **Key point:** $\mathbf{G}$ depends only on fault geometry and the elastic constants, not on the slip distribution. Computing it is the forward problem. Finding $\mathbf{s}$ given $\mathbf{d}$ is the inverse problem.

---

## What Determines the Shape of a Green's Function?

A single patch's surface displacement depends on:

- **Depth.** Deeper patches produce broader, smoother signals with smaller peak amplitude. The signal from a very deep patch is nearly indistinguishable from that of a neighbouring patch — this is why deep slip is hard to resolve.
- **Dip.** The asymmetry between hanging-wall and footwall signals increases with dip. A vertical fault produces a symmetric signal; a shallowly dipping fault produces strongly asymmetric uplift and subsidence.
- **Rake.** Strike-slip produces primarily horizontal displacement; dip-slip produces a mix of horizontal and vertical; tensile opening produces primarily vertical.
- **Size.** The amplitude scales with patch area and slip magnitude. The spatial scale of the signal is set by the patch depth and dimensions.

> **Prediction:** A fault patch at 5 km depth and one at 20 km depth, both with the same slip, produce surface signals of very different character. Describe qualitatively how the two signals differ in peak amplitude, spatial width, and the sharpness of the zero-crossing.

---

# Okada's Solution

**Okada (1985, 1992)** derived closed-form analytical expressions for the surface and internal displacement and strain fields due to a rectangular dislocation in an elastic half-space. For a horizontal surface observation point $\mathbf{x} = (x, y, 0)$ and a rectangular fault patch parameterized by length $L$, width $W$, dip $\delta$, depth to top $d$, and slip vector $\mathbf{s} = (s_s, s_d, s_t)$ (strike-slip, dip-slip, tensile):

$$
u_i(x, y) = \frac{1}{2\pi} \sum_{\text{corners}} \pm F_i(x, y; \text{geometry})
$$

where $F_i$ is a sum of logarithms and arctangents that arise from the image-source solution satisfying the traction-free boundary condition.

The full expressions run to several pages. The key properties are:

- Exact and analytic — no numerical quadrature over the patch
- Valid for any dip from 0° (horizontal) to 90° (vertical)
- Reduces to the 1-D arctan profile (Savage–Burford) in the appropriate limits
- Units: if slip is in metres, displacement is in metres

```{figure} ../figures/09_okada1.png
---
name: Okada geometry
width: 480px
alt: Two diagrams showing the Okada (1985) coordinate system and fault geometry. Top panel shows a point source with depth and dip labelled and an observation point at (X,Y,Z). Bottom panel shows a rectangular fault source with along-strike half-lengths AL1 and AL2, down-dip widths AW1 and AW2, depth, dip, and three dislocation components DISL1 (strike-slip), DISL2 (dip-slip), and DISL3 (tensile), with an observation point at (X,Y,Z).
---
Coordinate system and source geometry for the Okada (1985) solution. The free surface is $z = 0$; depth is positive downward. Top: point-source approximation. Bottom: finite rectangular fault parameterized by along-strike half-lengths $AL1$, $AL2$, down-dip widths $AW1$, $AW2$, depth to the top edge, and dip. The three dislocation components are strike-slip ($DISL1$), dip-slip ($DISL2$), and tensile opening ($DISL3$). From [Okada (1985)](https://doi.org/10.1785/BSSA0750041135).
```

```{figure} ../figures/09_okada2.png
---
name: Okada displacement fields
width: 620px
alt: Four 3-D block diagrams showing the elastic displacement field in a half-space for three fault types. Top left shows the fault model with dislocation magnitude U. Top right shows the strike-slip displacement field, with lateral warping of the free surface on either side of the fault. Bottom left shows the dip-slip field, with a broad upward bulge on the hanging-wall side and subsidence on the footwall. Bottom right shows the tensile field, with symmetric uplift above the opening crack. Displacement vectors are scaled to 0.1U.
---
Elastic displacement fields in a homogeneous half-space for a buried rectangular fault undergoing (top right) strike-slip, (bottom left) dip-slip, and (bottom right) tensile opening, each with dislocation magnitude $U$. Displacement vectors are scaled to $0.1U$ for visibility. The three cases correspond to the DISL1, DISL2, and DISL3 components in the Okada (1985) parameterisation. From [Okada (1985)](https://doi.org/10.1785/BSSA0750041135).
```

---

## Rectangular Patches and Their Limitations

The Okada solution is extremely efficient — each patch requires only a handful of function evaluations regardless of the observation grid size. But it has a fundamental geometric limitation:

- **Rectangular elements cannot tile a non-planar surface without gaps.** Real faults are curved, listric, or intersecting. Forcing a curved surface into a rectangular mesh leaves geometric gaps at element boundaries, and the strain singularities at every element edge no longer cancel — producing errors in displacement and stress calculations everywhere in the model (Meade 2007).
- **All dislocation elements are singular at their edges.** Strains diverge at the boundary of every patch, rectangular or triangular. With a gap-free triangular mesh the singularities of neighbouring elements cancel exactly; with a gapped rectangular mesh they do not.
- **Representing a curved fault with any finite element mesh requires bookkeeping** of varying strike and dip across patches — this is true regardless of element shape, and is the reason published fault models are distributed as mesh files rather than parameter lists.

For faults with complex geometry — and particularly for subduction zones — a gap-free triangular tessellation is the practical solution.

---

# Triangular Dislocation Elements

**Meade (2007)** derived a closed-form analytical solution for the displacements, strains, and stresses due to slip on an arbitrary triangular dislocation element (TDE) in a homogeneous elastic half-space.

The solution is constructed as a **dislocation loop**: each of the three triangle edges is represented as the superposition of two angular dislocations, and the six resulting deformation fields are summed. Consistent vertex ordering — clockwise when viewed from above — ensures that vertical segments of adjacent angular dislocations cancel exactly, leaving only the elastic effects of the triangular patch.

$$
\mathbf{u}(\mathbf{r}) = \sum_{j=1}^{N} \sum_{k=1}^{3} \left( \mathbf{u}_{kj}^{(1)} - \mathbf{u}_{kj}^{(2)} \right)
$$

```{figure} ../figures/09_meade_fig1.png
---
name: TDE construction
width: 600px
alt: Diagram showing how a triangular dislocation element is constructed from three dislocation legs, each formed by the superposition of two angular dislocations whose vertical segments cancel with those of adjacent legs.
---
Construction of a TDE by superposition of angular dislocation legs. Vertical segments of each leg cancel exactly with those of adjacent legs, leaving only the elastic effects of the triangular boundary. From Meade (2007), Fig. 1.
```

---

## TDEs in Practice — `cutde`

The `cutde` library implements Meade's solution in Python. The key function is:

```python
disp = hs.disp_free(obs_pts, triangles, slips, nu=0.25)
```

- `obs_pts` — shape `(N_obs, 3)`, surface observation points in metres
- `triangles` — shape `(N_tris, 3, 3)`, three vertices per triangle, ordered clockwise from above
- `slips` — shape `(N_tris, 3)`, [strike-slip, dip-slip, tensile] per triangle
- `disp` — shape `(N_obs, 3)`, [east, north, up] displacement in metres

The rake angle $r$ decomposes slip magnitude $s$ into components:

$$
s_s = s\cos r, \qquad s_d = -s\sin r
$$

where $r = 0°$ is left-lateral, $r = 90°$ is reverse, $r = -90°$ is normal, and $r = 180°$ is right-lateral.

> **Check:** A right-lateral fault has $r = 180°$. What are $s_s$ and $s_d$ for 2 m of slip? What does it mean for $s_s$ to be negative in the cutde convention?

---

## Recovering Familiar Results

`cutde` reproduces the classical 1-D profiles in the appropriate limits.

**Coseismic surface rupture** (infinite vertical fault, surface-breaking, right-lateral):

$$
u_\parallel(x) = \frac{s}{\pi} \arctan\!\left(\frac{D}{x}\right),
$$

where $D$ is the locking depth and $x$ is fault-perpendicular distance. Displacement is discontinuous at $x = 0$ (the fault trace) and decays to zero far from the fault.

**Interseismic (Savage–Burford)** (infinite vertical fault, creeping below depth $D$):

$$
v_\parallel(x) = \frac{V_s}{\pi} \arctan\!\left(\frac{x}{D}\right),
$$

where $V_s$ is the far-field plate velocity. The ratio inside the arctan is inverted relative to the coseismic case: this is the mathematical signature of the complementary relationship between the two phases of the seismic cycle.

> **Interpret:** The locking depth $D$ appears in the denominator of the coseismic argument and in the denominator of the interseismic argument. In both cases, increasing $D$ broadens the profile. Explain this physically for each case: why does deeper locking (coseismic) and deeper creep onset (interseismic) produce a broader surface signal?

```{figure} ../figures/09_profiles.png
---
name: Coseismic and interseismic profiles
width: 820px
alt: Two panels showing fault-perpendicular displacement profiles for coseismic and interseismic cases, each with three locking depths overlaid.
---
Surface displacement profiles for (left) a surface-rupturing coseismic event and (right) the Savage–Burford interseismic model, for locking depths of 5, 10, and 20 km. Deeper locking produces a broader, more gradual profile in both cases.
```

---

# The Green's Function Matrix

## Building G

For a fault mesh with $N_p$ patches, $N_s$ GNSS stations, and a satellite InSAR scene with $N_r$ pixels, the complete Green's function matrix has the structure:

$$
\mathbf{G} =
\begin{bmatrix}
\mathbf{G}_\text{GNSS} \\
\mathbf{G}_\text{InSAR}
\end{bmatrix},
\quad
\mathbf{G}_\text{GNSS} \in \mathbb{R}^{3N_s \times 2N_p}, \quad
\mathbf{G}_\text{InSAR} \in \mathbb{R}^{N_r \times 2N_p}.
$$

The factor of 3 in the GNSS rows comes from the three displacement components (east, north, up) per station. The factor of 2 in the columns comes from the two independent slip components (strike-slip and dip-slip) per patch — we do not assume a fixed rake.

Each GNSS row block has the form:

$$
\mathbf{G}_\text{GNSS} = 
\begin{bmatrix}
G_{E,1,\text{ss}} & G_{E,1,\text{ds}} & G_{E,2,\text{ss}} & \cdots \\
G_{N,1,\text{ss}} & G_{N,1,\text{ds}} & G_{N,2,\text{ss}} & \cdots \\
G_{U,1,\text{ss}} & G_{U,1,\text{ds}} & G_{U,2,\text{ss}} & \cdots \\
G_{E,2,\text{ss}} & G_{E,2,\text{ds}} & \cdots & \\
\vdots & & & \ddots
\end{bmatrix}
$$

where $G_{i,k,j}$ is the displacement at station $k$ in direction $i$ due to unit slip on patch in direction $j$.

Each InSAR row is a scalar line-of-sight (LOS) projection:

$$
G^\text{LOS}_{k,j} = \hat{\mathbf{l}} \cdot \mathbf{G}_{\text{GNSS},k,j},
$$

where $\hat{\mathbf{l}}$ is the unit LOS vector from ground to satellite, which depends on the satellite look geometry (incidence angle and heading).

> **Note:** The InSAR LOS vector $\hat{\mathbf{l}} = (-\sin\theta\sin\alpha,\, -\sin\theta\cos\alpha,\, \cos\theta)$ where $\theta$ is the incidence angle and $\alpha$ is the satellite heading measured clockwise from north. For Sentinel-1 ascending, $\theta \approx 38°$ and $\alpha \approx -12°$.

---

## The Size and Cost of G

The memory and compute cost of $\mathbf{G}$ scale as:

$$
\text{Memory} = (3N_s + N_r) \times 2N_p \times 8\ \text{bytes}.
$$

For a practical example: the Cascadia Mccrory mesh has $N_p = 1545$ patches, and we use $N_s = 439$ GNSS stations. The Green's function matrix $\mathbf{G} \in \mathbb{R}^{1317 \times 3090}$ occupies about 33 MB — modest enough to load on a laptop.

Computing $\mathbf{G}$ requires one `cutde` call per patch (or a vectorized batch). For the Ridgecrest lab mesh (40 patches, 150 stations), this takes a few seconds. For Cascadia (1545 patches, 439 stations), it would take several minutes — which is why the Cascadia $\mathbf{G}$ is pre-computed and distributed.

> **Lab reference:** In Parts V and VI of the lab you will build $\mathbf{G}$ for Ridgecrest from scratch, then load the pre-computed Cascadia $\mathbf{G}$. The verification step — confirming that `G @ s_backslip × 1000` reproduces the provided interseismic velocity field to numerical precision — confirms that the units and sign convention are correct before you use $\mathbf{G}$ for anything else.

---

# Two Case Studies

## Case Study 1: Ridgecrest M7.1 (2019)

The 2019 Ridgecrest sequence ruptured a system of conjugate faults in the Eastern California Shear Zone. The main M7.1 event ruptured a **NW-striking, near-vertical, right-lateral** fault.

Published fault geometry (Liu et al. 2019):

| Parameter | Value |
|---|---|
| Strike | 322° |
| Dip | 85° |
| Rake | 180° (right-lateral) |
| Length | ~50 km |
| Width | ~16 km |
| Depth to top | ~0 km (surface-rupturing) |

The near-vertical geometry means:
- Horizontal displacement dominates — the surface signal is primarily east and north.
- The vertical signal is small (a near-vertical fault produces almost no vertical surface motion in the far field).
- The four-lobed horizontal pattern is the kinematic signature of strike-slip: the two lobes on the same side of the fault move in the same horizontal direction, with opposite lobes moving in opposite directions.

```{figure} ../figures/09_ridgecrest_forward.png
---
name: Ridgecrest forward model
width: 840px
alt: Two maps showing observed and predicted GNSS coseismic offsets for the Ridgecrest M7.1 earthquake, with fault trace marked.
---
Observed GNSS coseismic offsets (left) and forward model prediction for uniform 1.5 m right-lateral slip (right) for the Ridgecrest M7.1. The forward model captures the far-field pattern but cannot reproduce the spatial variation in offset amplitude near the fault — the motivation for slip inversion.
```

> **Interpret:** The uniform-slip forward model reproduces the far-field pattern but shows systematic misfits near the fault. What does this tell you about the actual slip distribution?

---

## Case Study 2: Cascadia Subduction Zone

The Cascadia subduction zone presents a very different geometry from Ridgecrest:

| Parameter | Ridgecrest | Cascadia |
|---|---|---|
| Dip | 85° | ~8–15° |
| Depth range | 0–16 km | 5–40 km |
| Along-strike extent | ~50 km | ~1100 km |
| Dominant displacement | Horizontal (E–W) | Both (NE + subsidence/uplift) |
| Surface signal scale | ~tens of km | ~hundreds of km |

The shallow dip of the Cascadia megathrust means:

- **Hanging-wall uplift** over the locked zone and **footwall subsidence** (or smaller uplift) on the other side during a great earthquake.
- **Broad, smooth signals** at the surface — the shallow dip distributes the elastic deformation over a wide horizontal area.
- **Strong vertical component** — unlike a near-vertical strike-slip fault, the thrust geometry produces significant vertical surface motion.

```{figure} ../figures/09_cascadia_mesh.png
---
name: Cascadia fault mesh
width: 720px
alt: Map of the Cascadia subduction zone with the Mccrory fault mesh patches coloured by depth, and GNSS stations overlaid.
---
The Mccrory et al. (2012) Cascadia fault mesh: 849 nodes, 1545 triangular patches, depth range 5.5 to 39.3 km. GNSS stations used in the analysis are shown in blue.
```

The Mccrory mesh stores vertex coordinates as `(lon, lat, depth_km)` where depth is **negative** below the surface, and the GNSS station file uses **0–360° east longitude**. Careful attention to these conventions is necessary before any computation.

---

# The Hinge Line Argument

## Coastal Deformation as a Slip Constraint

The 1700 Cascadia earthquake left a rich paleoseismic record:

- **Ghost forests** along the Washington and Oregon coasts: coastal trees killed by sudden saltwater inundation, preserved in salt marshes.
- **Buried soil horizons**: marsh soils abruptly overlain by intertidal sediment, recording sudden subsidence of 0.5–1.5 m.
- **Japanese tsunami records**: eyewitness accounts and tide gauge data constraining the moment to M~9.

The paleoseismic record constrains the vertical deformation at the coast. The forward model predicts what that deformation should be for different slip geometries. The intersection of observation and prediction is a constraint on the slip distribution.

> **Prediction:** Before looking at the model results — if coseismic slip is confined to patches far offshore (shallow, beneath the ocean), would you expect the coast to subside or uplift? Explain your reasoning with a sketch of the hanging wall and footwall geometry.

---

## The Hinge Line

The **hinge line** is the zero-vertical-displacement contour on the surface for a given coseismic slip model. Its position depends on the depth extent of slip:

- **Shallow slip** (all offshore): the hinge line lies seaward of the coast. The coast is on the footwall side of the rupture and **subsides**.
- **Deep slip** (extending under the coast): the hinge line moves landward. The coast is on the hanging-wall side and **uplifts**.

We quantify this by computing the forward model for uniform slip on all patches shallower than a cutoff depth $D$, and plotting the mean vertical displacement at coastal GNSS stations as a function of $D$.

```{figure} ../figures/09_hinge_line.png
---
name: Hinge line argument
width: 900px
alt: Two panels. Left: vertical displacement profiles perpendicular to the Cascadia coast at 46 degrees N for cutoff depths of 10 to 40 km. Right: mean coastal vertical displacement as a function of cutoff depth, with the 1700 paleoseismic constraint shaded.
---
The hinge line argument for the 1700 Cascadia earthquake. Left: vertical surface displacement at ~46°N for uniform 10 m slip confined to different depth ranges. Right: mean vertical displacement at coastal GNSS stations as a function of downdip slip extent. The paleoseismic constraint (0.5–1.5 m of subsidence, red band) requires that the bulk of slip was shallower than ~30 km — predominantly offshore.
```

For the Mccrory mesh, the sign change in coastal vertical displacement occurs at approximately **D ≈ 30–33 km**. At 40–47°N the fault reaches this depth roughly 100–150 km offshore. This means the rupture did not extend significantly beneath the coast, consistent with the ghost forest evidence.

> **Note:** This argument was originally made by Satake et al. (1996, 2003) using a simpler rectangular fault model. The triangulated mesh produces a more nuanced picture because it captures the along-strike variation in slab geometry — the fault dips more steeply in the north than in the south, so the hinge depth is not constant along the margin.

---

## What the Hinge Line Cannot Tell Us

- **Along-strike variation in slip:** uniform slip is an assumption, not a result. A model with asperities concentrated offshore would produce similar coastal subsidence, even if some inland patches slipped.
- **The moment independently:** the hinge line argument constrains the spatial extent of slip, not its magnitude. Moment is separately constrained by the Japan tsunami amplitudes and attenuation.
- **Whether the rupture was a single event or a sequence:** the paleoseismic record integrates all deformation within a few minutes — it cannot resolve sub-events.

---

# Slow Slip Events

## A Different Regime on the Same Fault

The Cascadia megathrust does not only produce great earthquakes. At 25–40 km depth — below the seismically locked zone — **Episodic Tremor and Slip (ETS)** events occur on a remarkably regular schedule: every ~14 months in most of the margin, involving:

- 1–5 cm of dip-slip over patches at 25–40 km depth
- Spatial extent of 100–300 km along strike
- Duration of 1–6 weeks
- Seismic moment equivalent to M6.5–7.0

The same Green's function matrix that predicts great earthquake signals also predicts the SSE surface signal — the only differences are the slip magnitude, the active patches, and the sign (SSE slip is in the *same* direction as coseismic slip, not opposite).

---

## The Detection Problem

The forward model predicts peak vertical signals of **5–9 mm** for a typical northern Cascadia ETS event. Against a daily GNSS vertical noise floor of ~2 mm, the signal-to-noise ratio is 2.5–4.5.

This is a marginal detection problem — not hopeless, but requiring:

- **Dense networks**: station spacing must be smaller than the signal's spatial footprint (~100–200 km). The Pacific Northwest GNSS network (PNSN/PANGA) achieved adequate density only in the early 2000s.
- **Continuous recording**: campaign (periodic) GNSS measurements cannot resolve a 2–3 week transient.
- **Time series stacking**: detecting the signal in a single station's time series requires ~1–2 weeks of data at the ETS slip rate.

> **Interpret:** ETS events release moment equivalent to M6.5–7.0 yet produce no felt shaking and only a few mm of surface displacement. What must be different about the slip process — specifically the slip duration and stress drop — compared to a regular M6.5 earthquake?

```{figure} ../figures/09_sse_signal.png
---
name: SSE surface signal
width: 900px
alt: Four maps of the Pacific Northwest showing vertical surface displacement for three SSE scenarios and one M9 scenario, all plotted on the same plus-or-minus 5 mm colour scale.
---
Vertical surface displacement for three SSE scenarios (northern ETS, Oregon ETS, transition zone) and a M9 great earthquake scenario, all plotted on the same ±5 mm colour scale. The great earthquake signal is ~2 m peak — two orders of magnitude larger — but the colour scale is fixed to show SSE signals at their actual amplitude. Gold dots mark the active fault patches.
```

> **Lab reference:** In Part VIII of the lab you will compute these SSE signals and fill in a detectability table comparing peak amplitude, signal-to-noise ratio, and number of stations above the noise floor for each scenario.

---

# From Forward Problem to Inverse Problem

## The Forward Problem Is Easy; the Inverse Is Not

The forward problem — given slip $\mathbf{s}$, compute displacement $\mathbf{d} = \mathbf{G}\mathbf{s}$ — has a unique, stable solution. The inverse problem — given $\mathbf{d}$, find $\mathbf{s}$ — is fundamentally different:

| Property | Forward | Inverse |
|---|---|---|
| Uniqueness | Unique solution | Generally non-unique |
| Stability | Stable (small slip → small displacement) | Often unstable (small noise → large slip artefacts) |
| Computation | Matrix–vector multiply | Requires regularization |
| Physical insight needed | Geometry and elastic constants | Also data uncertainty, smoothness assumptions |

The non-uniqueness arises because $\mathbf{G}$ is typically **underdetermined** (fewer observations than slip parameters) and because deep patches produce nearly identical surface signals — the inverse problem cannot distinguish between them without additional constraints.

---

## Regularisation

The standard approach to the geodetic slip inversion is **damped least squares** (Tikhonov regularization):

$$
\hat{\mathbf{s}} = \operatorname*{arg\,min}_{\mathbf{s}} \left\{ \|\mathbf{W}^{1/2}(\mathbf{G}\mathbf{s} - \mathbf{d})\|^2 + \lambda^2 \|\mathbf{L}\mathbf{s}\|^2 \right\},
$$

where:

- $\mathbf{W}$ is a diagonal data-weighting matrix (inverse of data variance)
- $\lambda$ is the **regularization parameter** — controls the trade-off between fitting the data and satisfying the smoothness constraint
- $\mathbf{L}$ is the **regularization operator** — often a Laplacian that penalizes roughness in the slip distribution

The solution is:

$$
\hat{\mathbf{s}} = (\mathbf{G}^T \mathbf{W} \mathbf{G} + \lambda^2 \mathbf{L}^T \mathbf{L})^{-1} \mathbf{G}^T \mathbf{W} \mathbf{d}.
$$

Choosing $\lambda$ requires a **trade-off curve** (L-curve or cross-validation): too small and the model is rough and fits noise; too large and the model is oversmoothed and fits poorly.

> **Looking ahead:** In the next two labs you will build this inversion machinery step by step — first designing the regularization operator for the Cascadia mesh, then inverting joint GNSS and InSAR data for a slip distribution. The Green's function matrix you loaded in this lab is the same one that enters the inversion.

---

# Summary

- An elastic half-space is a practical model for the seismogenic crust at timescales from seconds to centuries. Its linearity is the key property that makes Green's function methods work.

- A **Green's function** is the surface displacement due to 1 m of slip on one fault patch. It depends on patch depth, dip, rake, and size — not on the slip distribution elsewhere on the fault.

- The **`cutde`** library implements triangular dislocation elements, allowing Green's functions to be computed for faults of arbitrary geometry. Rectangular patches (Okada) are a special case.

- The **Green's function matrix** $\mathbf{G}$ encodes the complete linear relationship between slip and surface displacement. Building it is the forward problem; solving for slip given observed displacement is the inverse problem.

- **Strike-slip faults** (Ridgecrest) produce sharp, primarily horizontal signals. **Thrust faults** (Cascadia) produce broad signals with a significant vertical component and strong hanging-wall/footwall asymmetry.

- The **hinge line argument** uses forward modeling to translate a paleoseismic observation — coastal subsidence — into a constraint on the offshore extent of a great earthquake rupture. For the 1700 Cascadia event, widespread coastal subsidence requires slip predominantly shallower than ~30 km.

- **Slow slip events** produce 5–9 mm vertical signals on the same fault — at the detection threshold of continuous GNSS. Their discovery required dense, continuously recording networks.

---

# Additional Resources

> **Key Paper:** [Okada (1985) — Surface deformation due to shear and tensile faults](https://doi.org/10.1785/BSSA0750041135)  
> The original derivation of the analytical solution for a rectangular dislocation in an elastic half-space. The primary reference for geodetic forward modeling for four decades.

> **Key Paper:** [Meade (2007) — Algorithms for triangular dislocation elements](https://doi.org/10.1016/j.cageo.2006.12.003)  
> Derives the closed-form solution for triangular dislocation elements. The mathematical foundation for `cutde` and all modern mesh-based geodetic inversions.

> **Software:** [cutde library](https://github.com/cutde-org/cutde)  
> Python implementation of the triangular dislocation element, with a vectorized API suitable for large meshes.

> **Key Paper:** [Satake et al. (2003) — Tsunami source of the 1700 Cascadia earthquake](https://doi.org/10.1029/2003JB002521)  
> The definitive application of the hinge line argument to constrain the 1700 Cascadia slip distribution from Japanese tsunami records and Pacific Northwest paleoseismic data.

> **Fault Model:** [Mccrory et al. (2012) — Juan de Fuca slab geometry](https://doi.org/10.1029/2012JB009407)  
> The published fault model used in the Cascadia sections of the lab. The triangulated mesh is distributed with the paper.

> **Community Resource:** [USGS SLAB2 — Global subduction zone geometries](https://www.sciencebase.gov/catalog/item/5aa1b00ee4b0b1c392e86467)  
> Depth, dip, and strike grids for all major subduction zones, updated in 2018 (Hayes et al.). A practical starting point for constructing fault meshes for any subduction zone.
