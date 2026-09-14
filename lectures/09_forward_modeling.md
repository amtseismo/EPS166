# Elastic Dislocation: The Forward Problem

## Purpose

To invert geodetic data for fault slip, we first need a model that predicts surface
deformation given a fault geometry and slip distribution. This is the **forward
problem** — the mathematical machinery that converts fault parameters into predicted
observations. Understanding it deeply is essential before we can run inversions or
critically evaluate published slip models.

In this lecture, we will:

- establish the elastic half-space as the standard model for the crust
- derive the Green's function concept and explain why linearity is so powerful
- work through the Okada (1985) rectangular dislocation model for a point source
  and finite fault
- build physical intuition for how fault geometry, depth, and slip direction
  control the surface deformation pattern
- show how the forward model connects to everything we have seen so far:
  the Savage–Burford interseismic model, the 1D coseismic profiles, and the
  synthetic InSAR interferograms from the lab

---

# The Elastic Half-Space

---

## Why Elasticity?

The crust deforms elastically on the timescales relevant to the earthquake cycle.
This means:

- deformation is **instantaneous** — stress changes propagate at the speed of
  seismic waves, far faster than geodetic observations can resolve
- deformation is **linear** — doubling the applied force doubles the displacement
- deformation is **recoverable** — remove the force and the material returns to
  its original shape

These three properties together make the elastic half-space an almost ideal
model for crustal deformation. Its predictions are:

1. **Fast to compute** — analytical solutions exist for simple geometries
2. **Linear in slip** — so the inverse problem is linear
3. **Well-validated** — decades of geodetic observations confirm the elastic
   approximation works remarkably well for the coseismic and early postseismic
   periods

The half-space approximation — treating the crust as a homogeneous elastic medium
occupying the region $z \leq 0$ with a free surface at $z = 0$ — is a simplification.
Real crust is layered, heterogeneous, and viscoelastic at depth. But for most
geodetic applications the errors introduced by ignoring layering are smaller than
the data uncertainties, especially at the spatial scales we work with.

---

## Elastic Parameters

Two parameters fully describe the elastic behavior of an isotropic material:

**Lamé parameters** $\lambda$ and $\mu$:
- $\mu$ (shear modulus) — resistance to shearing deformation
- $\lambda$ — relates stress to volumetric strain

In practice we more commonly use:
- $\mu$ — shear modulus (~30 GPa for typical crust)
- $\nu$ — Poisson's ratio, the ratio of lateral to longitudinal strain

For a **Poisson solid** ($\nu = 0.25$, $\lambda = \mu$) — a common approximation
for the crust:

$$\nu = 0.25, \quad \mu = \lambda \approx 30\ \text{GPa}$$

Most Okada-based forward models assume a Poisson solid. The sensitivity of the
predicted displacement to the exact value of $\nu$ is generally small compared
to uncertainty in fault geometry.

---

## The Governing Equations

Surface deformation due to a fault in an elastic half-space is governed by the
equations of static elasticity:

$$\nabla \cdot \boldsymbol{\sigma} = 0 \quad \text{(equilibrium)}$$

$$\boldsymbol{\sigma} = \lambda (\nabla \cdot \mathbf{u})\mathbf{I} + \mu(\nabla \mathbf{u} + \nabla \mathbf{u}^T) \quad \text{(constitutive relation)}$$

with boundary conditions:
- stress-free surface at $z = 0$: $\sigma_{iz}|_{z=0} = 0$
- displacement vanishes at infinity

A dislocation (fault) is introduced as a **displacement discontinuity** across a
surface $\Sigma$ embedded in the half-space.

Solving these equations analytically for a rectangular fault with uniform slip is
exactly what Okada (1985) did.

---

# Green's Functions and Linearity

---

## The Green's Function Concept

A **Green's function** $G_{ij}(\mathbf{x}; \mathbf{x}_0)$ describes the
displacement at surface location $\mathbf{x}$ in direction $i$ due to a unit
point force at source location $\mathbf{x}_0$ in direction $j$.

For our purposes the "source" is slip on a fault patch and the "response" is
surface displacement. If we know the Green's function for a unit-slip patch at
every point on the fault, we can predict the surface displacement for **any**
slip distribution by superposition:

$$u_i(\mathbf{x}) = \sum_{k=1}^{N} G_{ij}(\mathbf{x}; \mathbf{x}_k) \cdot s_j^{(k)}$$

where $s_j^{(k)}$ is the slip on the $k$-th fault patch in direction $j$.

This is the fundamental equation underlying all elastic dislocation inversions.

---

## Why Linearity Is So Powerful

Because the elastic equations are linear in displacement and stress, and because
the fault slip enters as a boundary condition, the predicted surface displacement
is **linear in slip**. This has profound consequences:

**For the forward problem:** we can compute the displacement from any slip
distribution as a weighted sum of pre-computed Green's functions. No matter how
complicated the slip distribution, the computation is just matrix multiplication.

**For the inverse problem:** the relationship between observations $\mathbf{d}$
and slip $\mathbf{s}$ is:

$$\mathbf{d} = \mathbf{G} \mathbf{s}$$

This is a **linear system** — the most well-understood class of inverse problem,
for which robust and efficient solution methods exist. We will exploit this
heavily in the next lecture.

```{figure} ../figures/10_greens_function_concept.png
---
width: 700px
alt: Schematic showing how surface displacement is predicted as a superposition of Green's functions — one per fault patch — each weighted by the slip on that patch.
---
The superposition principle. Each fault patch (colored rectangles) contributes a characteristic surface displacement pattern (its Green's function, shown as arrows). The total predicted displacement at any surface station is the sum of contributions from all patches, each weighted by the local slip. Doubling the slip on any patch doubles its contribution — this is linearity.
```

---

# The Okada (1985) Model

---

## What Okada Solved

Okada (1985) derived **closed-form analytical expressions** for the displacement,
strain, and stress at any point in a homogeneous elastic half-space due to a
**rectangular dislocation** (fault patch) with uniform strike-slip, dip-slip,
and tensile components.

This is the workhorse of crustal deformation modeling. Nearly every geodetic
slip model published since 1985 uses Okada's formulas, or triangular
dislocation elements (Meade 2007) that are equivalent for rectangular patches.

The inputs to the Okada model are:

| Parameter | Symbol | Description |
|-----------|--------|-------------|
| Strike | $\phi$ | Fault trace direction, clockwise from North |
| Dip | $\delta$ | Fault plane angle below horizontal |
| Rake | $\lambda$ | Slip direction on the fault plane |
| Depth to top | $d$ | Depth to the shallowest edge |
| Length | $L$ | Along-strike extent |
| Width | $W$ | Down-dip extent |
| Slip magnitude | $U$ | Average slip |
| Poisson's ratio | $\nu$ | Elastic parameter (usually 0.25) |

The outputs are the three components of surface displacement $(u_x, u_y, u_z)$
— east, north, and up — at any specified observation point.

---

## Fault Geometry Conventions

```{figure} ../figures/10_okada_geometry.png
---
width: 650px
alt: Diagram defining strike, dip, rake, and the four corners of a rectangular fault patch in the Okada coordinate system.
---
Okada (1985) fault geometry. Strike $\phi$ is measured clockwise from North; dip $\delta$ is measured from horizontal. The rake $\lambda$ is measured in the fault plane from the along-strike direction: $\lambda = 0°$ is left-lateral, $\lambda = 90°$ is reverse (hanging wall up), $\lambda = 180°$ is right-lateral, $\lambda = -90°$ is normal. The fault patch has length $L$ along strike and width $W$ down dip, with its top edge at depth $d$.
```

**Rake conventions** (Aki & Richards):
- $\lambda = 0°$ — left-lateral strike-slip
- $\lambda = 90°$ — reverse/thrust (hanging wall moves up)
- $\lambda = 180°$ or $-180°$ — right-lateral strike-slip
- $\lambda = -90°$ — normal (hanging wall moves down)

---

## Point Source vs. Finite Fault

**Point source (Mogi-like):** In the limit where the fault patch is much smaller
than the observation distance, the Okada solution approaches a double-couple
point source. This is appropriate when modeling the far-field of a small
earthquake.

**Finite fault:** For near-field observations or large earthquakes, the spatial
extent of the fault matters. A finite fault produces fundamentally different
surface deformation than a point source of the same moment — the deformation
is concentrated near the fault rather than distributed uniformly around it.

```{figure} ../figures/10_point_vs_finite.png
---
width: 720px
alt: Comparison of surface displacement patterns from a point source and a finite fault of the same seismic moment, showing how the finite fault concentrates deformation near the fault trace.
---
Point source (left) vs. finite fault (right) of the same seismic moment. The point source produces a smooth, nearly symmetric four-lobed pattern. The finite fault concentrates deformation along the fault trace and produces a sharp offset at the surface for a surface-rupturing event. As observation distance increases relative to fault size, the two solutions converge.
```

---

## Building Physical Intuition

Before fitting data we need to understand qualitatively how each parameter
controls the surface displacement pattern.

### Depth

Depth has a dominant effect on the pattern:

- **Shallow fault:** large near-fault gradients, sharp surface offset if it
  ruptures to the surface, rapid spatial decay
- **Deep fault:** broad, smooth deformation extending far from the fault,
  no surface discontinuity

The **characteristic length scale** of the surface deformation pattern is
approximately equal to the source depth. A fault at 10 km depth affects the
surface over a zone roughly 10–20 km wide; at 30 km depth, the zone is
30–60 km wide.

```{figure} ../figures/10_depth_effect.png
---
width: 700px
alt: Series of synthetic surface displacement profiles showing how increasing fault depth broadens and smooths the surface deformation pattern.
---
Effect of depth on surface deformation for a vertical right-lateral fault with fixed slip and dimensions. As depth increases from 2 km (purple) to 20 km (yellow), the deformation pattern broadens and the peak gradient near the fault decreases. This is why deep faults are harder to locate precisely from surface observations.
```

> **Question:** A geodetic survey detects a displacement signal extending over a
> zone 40 km wide. What does this tell you about the minimum depth of the source?

---

### Fault Dimensions

For a fixed slip magnitude and depth:
- **Longer fault** → displacement extends further along strike
- **Wider fault** → displacement extends further from the fault (equivalent to
  deeper bottom edge)
- **Aspect ratio** controls the shape of the deformation ellipse

The surface deformation pattern is sensitive to fault **length** in the
along-strike direction and relatively insensitive to fault **width** beyond
a certain point — this is one reason why along-strike extent is generally
better resolved than down-dip width in geodetic inversions.

---

### Rake

The rake determines which component of displacement dominates at the surface.

For a vertical fault viewed from above:
- **Strike-slip** ($\lambda = 0°$ or $180°$): horizontal displacement dominates,
  four-lobed pattern in map view
- **Normal** ($\lambda = -90°$): vertical displacement dominates, asymmetric
  because one block goes up and the other goes down
- **Reverse** ($\lambda = 90°$): vertical displacement dominates, opposite
  sense to normal

For a dipping fault, the **hanging wall** always moves more than the footwall
— the deformation is asymmetric across the fault trace in proportion to the dip.

```{figure} ../figures/10_rake_comparison.png
---
width: 720px
alt: Map-view surface displacement fields for strike-slip, normal, and reverse faults of the same geometry, showing how rake controls the horizontal and vertical displacement patterns.
---
Surface displacement for three fault types: right-lateral strike-slip (left), normal (center), and reverse (right). All faults have the same geometry (strike=0°, dip=60°, depth=5 km, length=30 km, width=15 km, slip=1 m). The horizontal displacement (arrows) and vertical displacement (color) differ dramatically — rake is the dominant control on which component dominates and on the asymmetry of the pattern.
```

---

### Dip

Dip has two effects:
1. It determines how much of the slip appears as **vertical vs. horizontal**
   surface displacement
2. It makes the deformation **asymmetric** between hanging wall and footwall —
   the hanging wall always shows larger displacement than the footwall for
   dip-slip faults

For a thrust fault dipping at $\delta$:
- The **hanging wall** moves up and toward the footwall
- The **footwall** moves down and away (or barely moves for shallow dips)
- The asymmetry increases as $\delta$ decreases (shallower thrust)

This asymmetry is diagnostic — it is one of the key ways InSAR and GNSS can
determine fault dip from surface observations alone.

---

## The Savage–Burford Model as a Special Case

The interseismic velocity profile we studied in the seismic cycle lecture is a
limiting case of the Okada model:

$$v(x) = \frac{V_s}{\pi} \arctan\!\left(\frac{x}{D}\right)$$

This corresponds to an **infinitely long vertical fault** with **uniform creep**
from depth $D$ to infinity. Taking the Okada solution for a vertical strike-slip
fault and extending its length to infinity recovers exactly this arctangent
profile.

Similarly, the coseismic profile:

$$u(x) = \frac{S}{\pi} \arctan\!\left(\frac{D}{x}\right)$$

is the Okada solution for a surface-rupturing vertical strike-slip fault with
uniform slip $S$ down to depth $D$.

👉 The Savage–Burford model and the 1D coseismic profiles are not separate
theories — they are analytical limits of the same Okada elastic dislocation
framework.

---

# From a Single Patch to a Slip Distribution

---

## Subdividing the Fault

Real earthquakes do not slip uniformly — slip concentrates in **asperities**
(high-slip patches), varies along strike and down dip, and often involves
multiple fault segments. To represent this spatial variability we divide the
fault into an array of rectangular sub-patches and assign an independent slip
value to each.

```{figure} ../figures/10_fault_subdivision.png
---
width: 700px
alt: A rectangular fault plane divided into a 6x4 grid of sub-patches, each with an independently varying slip shown by color.
---
A fault plane divided into $N$ sub-patches. Each patch has its own slip value; the total surface displacement is the superposition of contributions from all patches. This is the fundamental parameterization used in finite fault inversions. For Ridgecrest, a typical inversion might use 50–200 patches; for a large subduction zone earthquake, thousands.
```

---

## The Green's Function Matrix

For each sub-patch $k$ with unit slip, we compute the surface displacement at
every observation point $i$ using the Okada formula. This gives one column of
the Green's function matrix $\mathbf{G}$:

$$G_{ij,k} = \text{displacement at station } i \text{ in direction } j \text{ due to unit slip on patch } k$$

Assembling all patches and all stations:

$$\underbrace{\mathbf{d}}_{M \times 1} = \underbrace{\mathbf{G}}_{M \times N} \underbrace{\mathbf{s}}_{N \times 1}$$

where:
- $\mathbf{d}$ is the data vector ($M$ observations)
- $\mathbf{G}$ is the Green's function matrix ($M$ observations × $N$ patches)
- $\mathbf{s}$ is the slip vector ($N$ patch slip values)

This is the central equation of geodetic fault slip inversion. In the next
lecture we will solve it for $\mathbf{s}$ given $\mathbf{d}$ and $\mathbf{G}$.

---

## Different Data Types, Same Framework

One of the great strengths of the Okada framework is that it handles multiple
data types within the same linear system — we just stack the data vector and
the corresponding rows of $\mathbf{G}$:

$$\begin{pmatrix} \mathbf{d}_{GNSS} \\ \mathbf{d}_{InSAR} \\ \mathbf{d}_{hr-GNSS} \end{pmatrix} = \begin{pmatrix} \mathbf{G}_{GNSS} \\ \mathbf{G}_{InSAR} \\ \mathbf{G}_{hr-GNSS} \end{pmatrix} \mathbf{s}$$

Each data type contributes differently:

| Data type | Components | Spatial coverage | Strength |
|-----------|-----------|-----------------|---------|
| GNSS offsets | 3D (E, N, U) | Sparse point measurements | All 3 components; absolute |
| InSAR LOS | 1D (LOS direction) | Dense spatial coverage | Spatial detail; relative |
| HR-GNSS | 3D time series | Sparse points | Rupture timing; directivity |
| Seismic | Waveforms | Global | Rupture propagation; moment |

For **InSAR**, the Green's functions must be projected onto the line-of-sight
direction before comparison with data:

$$d_{LOS} = \mathbf{\hat{r}}_{LOS} \cdot \mathbf{u} = \hat{r}_E u_E + \hat{r}_N u_N + \hat{r}_U u_U$$

For **ascending and descending tracks**, we have two LOS projections of the
same displacement field — two independent constraints on the 3D motion.

---

# Two Examples

---

## Example 1: Ridgecrest M7.1 — Forward Model

Using the published fault geometry (strike 322°, dip 85°, rake 180°, length
50 km, width 16 km, depth to top 0 km, uniform slip 1.5 m), we can predict
the surface displacement at any point using the Okada formula.

```{figure} ../figures/10_ridgecrest_forward.png
---
width: 720px
alt: Predicted horizontal displacement vectors and vertical displacement from the Okada forward model for the Ridgecrest M7.1 earthquake, alongside the observed GNSS offsets.
---
Forward model prediction for the Ridgecrest M7.1 (uniform slip model). **Left:** predicted horizontal surface displacement vectors (arrows) and vertical displacement (color). **Right:** observed GNSS coseismic offsets from Lab 4. The overall pattern matches well — this is the starting point for the full inversion in Lecture 12. After Funning / Liu et al. (2019).
```

The forward model serves multiple purposes before we invert:
- **Sanity check** — does the predicted pattern have the right sense, scale, and
  spatial extent?
- **Data selection** — which stations are in the region where we expect signal?
- **Geometry refinement** — trial-and-error adjustment of fault geometry
  (strike, dip, depth) to improve visual agreement before formal optimization

---

## Example 2: Cascadia SSE — Subduction Zone Forward Model

Slow slip events on the Cascadia subduction interface require a **dipping fault**
geometry rather than a vertical strike-slip fault. The Okada model handles this
directly.

For the Juan de Fuca plate interface beneath western Oregon and Washington, a
typical SSE:
- Occurs at 25–40 km depth on the subduction interface
- Dips at ~10–15° eastward
- Slip of ~2–5 cm over 2–4 weeks
- Surface displacement of a few mm westward at coastal GNSS stations

```{figure} ../figures/10_cascadia_sse_forward.png
---
width: 700px
alt: Predicted surface displacement from a Cascadia slow slip event using the Okada forward model on a dipping subduction interface, compared to observed GNSS vectors showing westward motion.
---
Forward model prediction for a Cascadia SSE. The dipping interface produces an asymmetric surface displacement — coastal stations (above the slip patch) move westward and slightly upward; inland stations show little signal. This asymmetry, combined with the spatial pattern, will allow us to locate the slip patch in the inversion lecture. After Bartlow (2020).
```

The contrast between Ridgecrest (near-vertical, surface-rupturing, large slip)
and Cascadia SSE (shallow-dipping, deep, small slip) illustrates the range of
problems the same forward modeling framework can address.

---

# Limitations of the Standard Model

---

## What the Okada Model Ignores

The homogeneous elastic half-space is a powerful simplification, but it ignores
several physical effects that matter in some situations:

**Crustal layering:** Real crust has velocity and density gradients. Layered
earth models (e.g., using the propagator matrix approach of Savage 1998 or
the Zhu & Rivera 2002 code) can improve predictions in the near field, but
require knowledge of the velocity structure and are more computationally
expensive.

**Earth's curvature:** For large earthquakes or long-wavelength signals,
the flat-earth approximation introduces errors. Spherical earth models are
used for global applications.

**Viscoelastic relaxation:** The Okada model predicts the **instantaneous
elastic** response. Postseismic deformation due to viscous flow in the lower
crust or mantle requires a viscoelastic forward model (e.g., RELAX, PYLITH).
This is why the Li et al. (2018) Cascadia coupling model gives different
results from the elastic models — it accounts for ongoing viscoelastic
relaxation from past megathrust earthquakes.

**Topography:** The half-space assumes a flat free surface. In areas of
high relief, topographic corrections can be important.

**Pore fluid effects (poroelastic):** Fluid redistribution following an
earthquake modifies the short-term elastic response, particularly in the
near field and in fluid-saturated sedimentary basins.

---

## When Is the Simple Model Good Enough?

For most geodetic inversions of crustal earthquakes ($M < 8$, $z > 5$ km,
observation period weeks to months), the homogeneous elastic half-space with
the Okada formula is **good enough** — model errors are smaller than data
uncertainties. The biggest source of systematic error is usually **fault
geometry uncertainty** rather than elastic model simplification.

For subduction zone megathrusts, Cascadia coupling models, and long-term
interseismic studies, viscoelastic effects become important and the simple
model may introduce systematic bias.

👉 **The appropriate model depends on the question.** For coseismic slip
distributions of crustal earthquakes, use Okada. For interseismic coupling
on subduction zones where relaxation from past earthquakes is ongoing,
use a viscoelastic model.

---

# Looking Ahead

In the next lecture (The Inverse Problem) we will:

1. Set up the linear system $\mathbf{d} = \mathbf{G}\mathbf{s}$ formally
2. Understand why we cannot simply invert $\mathbf{G}$ — the system is
   underdetermined and noise-contaminated
3. Introduce regularization — the mathematical way to impose geological
   plausibility constraints
4. Derive the damped least-squares solution and understand what it optimizes
5. Introduce the resolution matrix — the tool for understanding what spatial
   scales of slip we can and cannot recover

In the lab, you will compute Green's function matrices for both the Ridgecrest
fault and the Cascadia subduction interface, predict surface displacements, and
compare them to real GNSS and InSAR data — building the forward model that the
next two labs will invert.

---

# Summary

- The **elastic half-space** is the standard model for the crust on seismic
  cycle timescales. It is homogeneous, isotropic, and governed by two elastic
  parameters ($\mu$ and $\nu$). Deformation is instantaneous, linear, and
  recoverable.

- A **Green's function** $G_{ij}$ gives the surface displacement at station $i$
  due to unit slip on fault patch $j$. Linearity means the total displacement
  is a superposition of Green's function contributions from all patches, each
  weighted by the local slip.

- The **Okada (1985)** model provides closed-form expressions for surface
  displacement in an elastic half-space due to a rectangular fault with uniform
  slip. Its inputs are strike, dip, rake, depth, length, width, and slip; its
  outputs are the three components of surface displacement at any observation
  point.

- **Depth** is the dominant control on the spatial scale of surface deformation
  — shallow sources produce sharp, localized signals; deep sources produce broad,
  smooth signals extending far from the fault.

- **Rake** controls which displacement component dominates — strike-slip produces
  horizontal four-lobed patterns; dip-slip produces asymmetric vertical signals.

- **Fault dip** introduces asymmetry between hanging wall and footwall — the
  hanging wall always moves more for dip-slip faults.

- Dividing the fault into $N$ sub-patches and assembling their Green's functions
  gives the matrix equation $\mathbf{d} = \mathbf{G}\mathbf{s}$, which is
  linear in slip. Different data types (GNSS, InSAR, HR-GNSS) all fit into the
  same framework by stacking their data vectors and corresponding Green's
  function rows.

- The **Savage–Burford** interseismic model and the **1D coseismic profile**
  from the seismic cycle lecture are both limiting cases of the Okada model —
  not separate theories.

- The homogeneous elastic half-space is appropriate for most crustal earthquake
  applications. Layered earth, viscoelastic relaxation, and poroelastic effects
  matter for long-wavelength signals, subduction zones, and postseismic studies.

---

# Additional Resources

> **Classic paper:** [Surface deformation due to shear and tensile faults in a half-space](https://doi.org/10.1785/BSSA0750041135)  
> Okada, Y. (1985). *Bulletin of the Seismological Society of America*, 75(4), 1135–1154. The original paper — worth reading for the elegant derivation and the comprehensive expression tables still used today.

> **Extension:** [Internal deformation due to shear and tensile faults in a half-space](https://doi.org/10.1785/BSSA0820021018)  
> Okada, Y. (1992). *Bulletin of the Seismological Society of America*, 82(2), 1018–1040. Extends the 1985 paper to subsurface displacements and strains.

> **Triangular elements:** [Algorithms for the calculation of exact displacements, strains, and stresses for triangular dislocation elements](https://doi.org/10.1016/j.cageo.2006.12.003)  
> Meade, B. J. (2007). *Computers & Geosciences*, 33(8), 1064–1075. The triangular dislocation formulation used in `cutde` and increasingly preferred for complex fault geometries.

> **Review:** [Geodetic imaging of fault systems](https://doi.org/10.1146/annurev-earth-040610-133304)  
> Bürgmann, R., & Dresen, G. (2008). Rheology of the lower crust and upper mantle. *Annual Review of Earth and Planetary Sciences* — useful background on when elastic models are and are not appropriate.

> **Software:** [cutde](https://github.com/cutde-org/cutde)  
> Python implementation of triangular dislocation elements (Meade 2007). Used in the InSAR lab and the forward modeling lab.

> **Software:** [okada85](https://pypi.org/project/okada85/)  
> Pure Python implementation of Okada (1985). Simple, well-documented, easy to understand.

> **Software:** [RELAX](https://geodynamics.org/resources/relax)  
> Viscoelastic postseismic deformation modeling — for when the elastic approximation is not sufficient.

---

# Sources

- Okada, Y. (1985). Surface deformation due to shear and tensile faults in a
  half-space. *Bulletin of the Seismological Society of America*, 75(4),
  1135–1154. https://doi.org/10.1785/BSSA0750041135
- Okada, Y. (1992). Internal deformation due to shear and tensile faults in a
  half-space. *Bulletin of the Seismological Society of America*, 82(2),
  1018–1040. https://doi.org/10.1785/BSSA0820021018
- Meade, B. J. (2007). Algorithms for the calculation of exact displacements,
  strains, and stresses for triangular dislocation elements in a uniform elastic
  half space. *Computers & Geosciences*, 33(8), 1064–1075.
  https://doi.org/10.1016/j.cageo.2006.12.003
- Savage, J. C. (1998). Displacement field for an edge dislocation in a layered
  half-space. *Journal of Geophysical Research*, 103(B2), 2439–2446.
- Liu, C., et al. (2019). Fault geometry and slip distribution of the 2019
  Ridgecrest earthquake sequence. *Geophysical Research Letters*, 46.
  https://doi.org/10.1029/2019GL084949
- Bartlow, N. M. (2020). A long-term view of episodic tremor and slip in the
  Pacific Northwest. *Geophysical Research Letters*, 47.
  https://doi.org/10.1029/2019GL085303
- Scholz, C. H. (2019). *The Mechanics of Earthquakes and Faulting* (3rd ed.).
  Cambridge University Press. https://doi.org/10.1017/9781316681473
