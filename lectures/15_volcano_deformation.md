# Volcano Deformation I: Inflation, Deflation, and the Mogi Source

## Purpose

The shape and size of a volcanic deformation signal contains information about the depth, geometry, and volume change of a magma body. Geodetic measurements — tilt, leveling, GNSS, and InSAR — have revealed a remarkable range of inflation and deflation signals at volcanoes worldwide, most interpretable with simple elastic source models.

In this lecture, we will:

- explain why magma influx or withdrawal causes surface deformation
- derive the Mogi point-source model and its surface displacement field
- connect source depth and volume change to measurable quantities
- derive surface tilt from the Mogi displacement field and identify where tilt is maximized
- describe how GNSS, tiltmeters, and InSAR each sample the same deformation field differently
- convert displacement to interferometric phase and read wrapped fringes
- survey real examples of volcanic inflation and deflation
- recognize the depth–volume trade-off that limits single-track inversions

The next lecture addresses dike intrusion. Here we focus exclusively on roughly axisymmetric inflation and deflation from pressurized reservoirs.

---

# Why Volcanoes Deform

Magma exerts pressure on its surroundings. When a magma body inflates — from new melt entering the reservoir, from exsolution of volatiles, or from thermal expansion — it pushes outward on the enclosing rock. The rock responds elastically: it stretches and bends, transmitting that pressure to the free surface. The result is an outward, upward displacement centered above the source.

The same process runs in reverse during deflation: draining of magma into an erupting vent, cooling and contraction, or escape of dissolved gases shrinks the reservoir and causes inward, downward motion of the overlying crust.

Deformation can also arise from hydrothermal fluid migration, collapse of volcanic edifices, gravitational spreading, and thermoelastic effects. This lecture concentrates on the deformation driven by pressurized magmatic sources.

> What features of a surface deformation pattern would tell you whether the source is shallow or deep?

```{figure} ../figures/15_plumbing.png
---
name: Plumbing
width: 800px
alt: Cross-section diagram showing a pressurized spherical source at depth d, with arrows indicating radial outward and upward surface displacements. The displacement field is axially symmetric.
---
Interpretation of seismogenic features at Mount St. Helens. (a) All earthquake locations along depth, including the locations of 7 events. (b) Physical features affecting earthquakes. The magma reservoir and high $V_p$ intrusives are traced from the Vp images of Kiser et al. (2018). The temporary melt storage zone is loosely based off the shallow magma storage zone from Lees (1992) and Waite and Moran (2009).  From [Hirao et al. 2025](10.1029/2025JB031278).
```

---

## The Elastic Half-Space

We model the crust as a **homogeneous, isotropic, elastic half-space**: a solid occupying all space below the plane $z = 0$, with the free surface at $z = 0$. A pressure source is buried at depth $d$.

This model is idealized. The crust is heterogeneous, partly viscoelastic, and riddled with faults and fluids. Nevertheless, elastic half-space models explain the first-order geometry of volcanic deformation at most volcanoes and serve as the standard starting point for source inversions.

The relevant elastic parameters are:

| Parameter | Symbol | Typical crustal value |
|---|---|---|
| Shear modulus | $\mu$ | 30 GPa |
| Poisson's ratio | $\nu$ | 0.25 |
| Bulk modulus | $K$ | $\mu(2+2\nu)/(3-6\nu)$ |

For $\nu = 0.25$, the Lamé parameters satisfy $\lambda = \mu$.

---

# The Mogi Point Source

## Derivation

Mogi (1958) derived the surface displacements due to a **small pressurized sphere of radius $a$** embedded at depth $d$ in an elastic half-space. The key simplification is that the sphere is small compared to its depth: $a \ll d$. In this limit, the sphere acts as a **point source** and the solution depends only on the **volume change** $\Delta V$, not on the separate values of $a$ and $\Delta p$.

The derivation follows from the solution for a center of dilatation (a nuclei of strain) in a half-space, as given in Segall (2010), Chapter 7. The key result is a displacement field that is axially symmetric about the vertical axis through the source.

## Surface Displacement Field

```{figure} ../figures/15_mogi_schematic.png
---
name: Mogi schematic
width: 420px
alt: Cross-section diagram showing a pressurized spherical source at depth d, with arrows indicating radial outward and upward surface displacements. The displacement field is axially symmetric.
---
Geometry of a spherical magma chamber. The chamber has radius a, with center at depth d
beneath the free surface, x3 = 0. r denotes the radial distance from the center of the magma chamber,
whereas ρ marks the distance from the center of symmetry along the free surface.
```

At a surface point at horizontal distance $\rho$ from the source directly above it, the displacements are (Segall, 2010, eq. 7.14):

$$
u_\rho(\rho) = \frac{(1-\nu)}{\pi} \frac{\Delta V \cdot \rho}{\left(\rho^2 + d^2\right)^{3/2}}
$$

$$
u_z(\rho) = \frac{(1-\nu)}{\pi} \frac{\Delta V \cdot d}{\left(\rho^2 + d^2\right)^{3/2}}
$$

where $\rho$ is horizontal radial distance from the source epicenter, $u_\rho$ is horizontal radial displacement (positive outward), $u_z$ is vertical displacement (positive upward), $\Delta V$ is source volume change (positive = inflation), and $\nu$ is Poisson's ratio. Note that Segall uses $\rho$ for surface radial distance and reserves $r$ for the 3D distance from the center of the spherical cavity.

For $\nu = 0.25$:

$$
(1-\nu)/\pi \approx 0.239
$$

**The ratio of horizontal to vertical displacement at any surface point is:**

$$
\frac{u_\rho}{u_z} = \frac{\rho}{d}
$$

This is a key result: the horizontal and vertical displacements are equal when $\rho = d$, and horizontal motion exceeds vertical beyond that radius. This ratio provides a geometric constraint on source depth that is independent of $\Delta V$.

## Depth–Width Scaling

The vertical displacement peaks directly above the source (Segall, 2010, following eq. 7.14):

$$
u_z^{\max} = u_z(\rho=0) = \frac{(1-\nu)\,\Delta V}{\pi\, d^2}
$$

It falls to half its maximum value at a characteristic surface radius. Setting $u_z = u_z^{\max}/2$ and solving for $\rho$ gives (Segall, 2010):

$$
\rho_{1/2} = d\sqrt{2^{2/3} - 1} \approx 0.77\,d
$$

This is the **half-amplitude radius**. It is set entirely by the source depth and is independent of $\Delta V$.

This gives a practical workflow for first-order depth estimation from an interferogram:
1. Measure $\rho_{1/2}$ — the surface radial distance where the LOS signal is half its peak value.
2. Estimate depth: $d \approx \rho_{1/2} / 0.77$.
3. Estimate volume change from the peak displacement and the estimated depth.

```{figure} ../figures/15_mogi.png
---
name: Mogi profiles
width: 460px
alt: First-order approximation to surface displacements from a pressurized spherical magma chamber.
---
First-order approximation to surface displacements from a pressurized spherical magma chamber.
```

---

## What Controls What

| Observable | Primarily controlled by |
|---|---|
| Peak LOS displacement | $\Delta V / d^2$ |
| Width of deformation signal | $d$ |
| Ratio $u_\rho / u_z$ at any surface point | $\rho / d$ |
| Total displaced volume at surface | $\Delta V$ |
| Fringe count in interferogram | $\Delta V / d^2$ (peak LOS / cycle length) |
| Peak tilt amplitude | $\Delta V / d^3$ |

The peak amplitude and the width are **not independent** — both depend on $d$. A deep source with large $\Delta V$ can produce the same peak displacement as a shallow source with small $\Delta V$, but its signal will be broader. This trade-off is fundamental to volcanic source inversions and is discussed at the end of this lecture.

```{figure} ../figures/15_mogi_controls.png
---
name: mogi-controls
width: 100%
alt: Three-panel figure showing what controls a Mogi source deformation signal. Panel A shows profiles at three depths with the same volume change, demonstrating that depth controls signal width. Panel B shows profiles at three volume changes with the same depth, demonstrating that volume change controls amplitude only. Panel C overlays two sources with identical peak displacement but different depths, showing they are distinguishable only by signal width.
---
**What controls the Mogi deformation signal.** Panel A: depth $d$ controls signal width — increasing depth widens the profile and lowers the peak, with $\rho_{1/2} \approx 0.77\,d$. Panel B: volume change $\Delta V$ scales amplitude only — $\rho_{1/2}$ is completely unchanged as $\Delta V$ varies. Panel C: the depth–volume trade-off — Source A (shallow) and Source B (deep) produce the same peak displacement; only the signal width distinguishes them.
```

---

# Measuring Volcanic Deformation

The Mogi displacement field — $u_z(\rho)$ and $u_\rho(\rho)$ — produces signals in every geodetic measurement type. GNSS, tiltmeters, and InSAR each sample a different aspect of the same underlying field. Understanding how each instrument responds to a Mogi source is essential for interpreting volcanic monitoring data.

## GNSS at Volcanoes

GNSS time series record three-component displacement at each station. At a volcano, the east and north components combine into the horizontal radial displacement $u_\rho(\rho)$, while the vertical component gives $u_z(\rho)$ directly.

Continuous GNSS networks at volcanic summits trace the inflation–deflation cycle as integrated displacement: stations gradually move outward and upward during inflation, then sharply inward and downward when an eruption taps the reservoir. The ratio $u_\rho / u_z = \rho / d$ at a known station position provides an independent estimate of source depth from a single station pair.

**Comparison with other methods:**
- GNSS gives absolute, three-component displacement at a point, sampled typically at 1 Hz to daily
- Precision is ~1–3 mm horizontal, ~5 mm vertical for daily positions — slow volcanic signals accumulate above noise over weeks to months
- Real-time 1 Hz GNSS can resolve rapid co-eruptive deformation events

```{figure} ../figures/15_volcano_gnss.jpg
---
name: Volcano GNSS
width: 520px
alt: Summit inflation at Mauna Loa, as indicated by GPS measurements between June 2004 and April 2005.
---
Summit inflation at Mauna Loa, as indicated by GPS measurements between June 2004 and April 2005.
```

---

## Tiltmeters

A tiltmeter measures the **rotation of the surface element from horizontal** — the slope of the deformed surface at a point. Tilt is expressed in microradians (µrad); 1 µrad corresponds to a 1 mm change in height over 1 km, or equivalently a tilt of about 0.2 arcseconds.

**Instrument types:**
- **Borehole tiltmeters** (e.g., Sacks-Evertson): installed at depth (30–200 m), thermally isolated, resolution ~0.001 µrad. Preferred for long-term monitoring.
- **Surface broadband tiltmeters**: lower installation cost, noisier, but sufficient for large volcanic signals (tens to hundreds of µrad)
- **Electronic levels (bubble tiltmeters)**: simple, robust, used in campaign surveys and remote deployments

Tiltmeters respond rapidly — sub-second sampling is routine — and can resolve transient inflation signals that GNSS or InSAR would miss at their daily or repeat-pass cadence.

### Tilt from the Mogi Source

The tilt at surface point $\rho$ is the negative radial gradient of the vertical displacement:

$$
\tau(\rho) = -\frac{\partial u_z}{\partial \rho}
$$

Differentiating the Mogi vertical displacement:

$$
\tau(\rho) = \frac{3(1-\nu)\,\Delta V}{\pi} \cdot \frac{d\,\rho}{\left(\rho^2 + d^2\right)^{5/2}}
$$

This can be written compactly in terms of the displacement components themselves:

$$
\tau(\rho) = \frac{3\rho}{\rho^2 + d^2}\,u_z(\rho) = \frac{3d}{\rho^2 + d^2}\,u_\rho(\rho)
$$

The second equality is especially useful: **tilt is directly proportional to horizontal displacement**, scaled by the geometric factor $3d/(\rho^2+d^2)$. Both $u_z$ and $u_\rho$ from the Mogi model determine tilt without any additional parameters.

The tilt is **zero directly above the source** ($\rho = 0$, by axial symmetry) and decays to zero far away. Setting $d\tau/d\rho = 0$ gives the location of peak tilt:

$$
\rho_{\tau,\max} = \frac{d}{2}
$$

The maximum tilt signal occurs at **half the source depth**, not at the summit.

```{figure} ../figures/15_tilt_profile.png
---
name: mogi-tilt-profile
width: 600px
alt: Plot showing normalised tilt tau (dashed green) and normalised vertical displacement u_z (solid blue) vs surface radial distance rho for a Mogi source with d = 6.5 km. Tilt is zero at rho=0, rises to a peak at rho = d/2 = 3.2 km, then decays. Vertical displacement peaks at rho=0 and decays monotonically.
---
Tilt profile for a Mogi source ($d$ = 6.5 km), normalised to respective peak values. Tilt is zero at the source epicenter — the surface is flat directly above the source by symmetry — peaks at $\rho = d/2$, then decays. Vertical displacement peaks at $\rho = 0$ and falls monotonically. A tiltmeter placed at $\rho \approx d/2$ from the summit epicenter sits at the sweet spot for maximum sensitivity to reservoir pressure changes.
```

> A tiltmeter is located 1.5 km from the summit of a volcano. Mogi inversion of GNSS data places the reservoir at 3 km depth. Is the tiltmeter close to, at, or beyond the peak tilt radius? What does this imply for its sensitivity to small pressure changes?

### Tilt Signals at Kīlauea

The HVO tiltmeter network at Kīlauea — including borehole instruments at UWD, UWE, and SDH — provides the most detailed continuous record of volcanic deformation in the world. Because the Halemaʻumaʻu reservoir sits at ~1–3 km depth, tiltmeters on the caldera rim (at $\rho \approx 1$–$2$ km) are near the peak tilt radius and show signals of tens to hundreds of µrad per year.

During the 2008–2018 summit lava lake activity, tiltmeters resolved **Deflation-Reinflation (DRE) events**: episodes lasting hours to days in which the summit deflated as lava lake level surged, then gradually reinflated. These had amplitudes of only a few µrad but were reproduced daily, invisible to InSAR but clear in hourly tiltmeter records. The same geometry — rapid deflation tied to eruption, slow inter-eruption inflation — plays out over years in the GNSS record and over weeks in interferograms, illustrating how the three measurement types span a continuous range of temporal resolution.

```{figure} ../figures/15_kilauea_tilt.png
---
name: Kīlauea tilt DRE
width: 760px
alt: Tiltmeter data from Kīlauea.
---
Ground tilt associated with episodic eruptions at Kīlauea. Top panel, two years of summit tilt spanning episodic fountaining at Maunaulu in 1969, as measured by a watertube tiltmeter at Uēkahuna  bluff.  Middle panel, an ideal aerosmith measurement of summit ground tilt during the initial years (1984-1986) of the Puʻuʻōʻō eruption that span a period of episodic fountaining. Bottom panel, electronic borehole tiltmeter record from December 2024 until April 2025 showing strong deflationary tilt associated with the sixteen (so far) eruptive episodes, numbered on the graph.  Data from USGS Hawaiian Volcano Observatory.
```

---

## InSAR: Mapping the Full Deformation Field

InSAR complements GNSS and tilt by imaging the **spatial pattern** of deformation across the entire volcanic edifice — something point measurements cannot do. A single interferogram spanning a few weeks to years captures the bulls-eye pattern of Mogi inflation over a 50–100 km scene with ~10–30 m pixel spacing.

### From Displacement to Interferometric Phase

InSAR measures the change in radar range (line-of-sight distance) between the ground and satellite between two acquisitions. A change in range $\delta r$ produces a phase change:

$$
\Delta\phi = -\frac{4\pi}{\lambda}\,\delta r
$$

where $\lambda$ is the radar wavelength. One full fringe ($2\pi$ of phase) corresponds to a half-wavelength of LOS motion:

$$
\delta r_{\text{cycle}} = \frac{\lambda}{2}
$$

Note: $\rho$ is reserved throughout this lecture for horizontal surface distance from the Mogi source epicenter, following Segall (2010).

| Sensor | Wavelength | LOS per fringe |
|---|---|---|
| ERS, Sentinel-1 (C-band) | 5.6 cm | 2.8 cm |
| ALOS-2 (L-band) | 23.8 cm | 11.9 cm |
| TerraSAR-X (X-band) | 3.1 cm | 1.6 cm |

Interferograms of volcanic inflation are often **rewrapped** at a fixed LOS increment (commonly 2.8 cm or 10 cm) for display, so the number of fringes represents the total LOS change divided by the display cycle.

## Line-of-Sight Projection

The radar LOS unit vector from ground to satellite depends on the satellite look geometry. For a satellite with incidence angle $\theta$ (from vertical) and look azimuth $\alpha$ (satellite-to-ground direction, measured clockwise from north):

$$
\hat{\ell} = \begin{pmatrix} -\sin\theta\sin\alpha \\ -\sin\theta\cos\alpha \\ \cos\theta \end{pmatrix}
$$

in east, north, up coordinates. The LOS displacement (positive = toward satellite) is:

$$
\delta r = \hat{\ell} \cdot \mathbf{u} = -\sin\theta\sin\alpha\,u_E - \sin\theta\cos\alpha\,u_N + \cos\theta\,u_z
$$

For typical incidence angles (25°–45°), the **vertical component dominates** the LOS signal by roughly $\cos\theta \approx 0.7$–$0.9$, making the vertical displacement the main observable. The horizontal component contributes through $\sin\theta \approx 0.4$–$0.7$ times the projection of horizontal motion onto the look direction.

**An important consequence:** ascending and descending passes measure different LOS projections. Combining both constrains the three-component displacement field and helps separate horizontal from vertical motion.

```{figure} ../figures/15_los.png
---
name: LOS geometry
width: 680px
alt: Diagram showing satellite look direction, incidence angle theta, and the projection of a 3D displacement vector onto the LOS unit vector. For ascending and descending geometries.
---
Panels A and B show what an interferogram would look like for a simple expanding spherical magma chamber from an ascending and descending orbital perspective. The star shows the true center of the inflating magma source. The arrow and bar denote satellite flight direction and look direction respectively. Each fringe represents approximately 1.55 cm. Panels C and D show the same event in a cross-section view. The black lines and arrows show the displacement as viewed by the SAR satellite in its line-of-sight (LOS), while the grey lines and arrows show the ground displacement physically occurring. The key in panel C gives the scale of the arrows. Notice in the ascending case, the deformation pattern is shifted and skewed west while the descending case shows the opposite.
```

## Wrapped Interferograms: Reading the Fringes

A wrapped interferogram displays the LOS phase modulo $2\pi$, producing the characteristic **bull's-eye** fringe pattern for a Mogi source. The standard color cycle used in volcanology (cyan → yellow → magenta → cyan) represents one full LOS cycle.

To read a wrapped interferogram:
1. Count complete color cycles from the edge of the signal to the center. Each complete cycle = one LOS increment.
2. The innermost fringe marks the region of maximum LOS change.
3. The spatial width of the pattern indicates source depth.
4. For inflation, fringes increase toward the center. For deflation, they also increase toward the center — only the **sign convention** (which way fringes cycle) distinguishes inflation from deflation. Check which direction fringes cycle relative to the satellite convention.

> An ascending Sentinel-1 interferogram (C-band, $\lambda$ = 5.6 cm, 10 cm per displayed cycle) shows 6 complete fringes centered on a volcano. What is the peak LOS displacement?

---

## Instrument placement

Different measurements sample the deformation field at different characteristic radii:

| Signal | Peaks at |
|---|---|
| Vertical displacement $u_z$ | $\rho = 0$ (directly above source) |
| Horizontal displacement $u_\rho$ | $\rho = d/\sqrt{2} \approx 0.71\,d$ |
| Surface tilt $\tau$ | $\rho = d/2$ |
| Half-amplitude of $u_z$ | $\rho_{1/2} \approx 0.77\,d$ |

A tiltmeter placed at $\rho = d/2$ from the epicenter is at the **sweet spot** for maximum tilt signal. GNSS directly above the source maximizes vertical sensitivity. These different sampling geometries make co-located networks more informative than any single instrument type.

---

# Volcanic Inflation: Examples

## Okmok Volcano, Alaska: Inflation, Deflation, and Re-inflation (1992–1998)

Okmok volcano, a broad shield with a 10-km-wide caldera on Umnak Island in the Aleutian chain, erupted in February 1997. Lu et al. (2000) used ERS-1/ERS-2 C-band SAR interferometry (λ = 5.66 cm, one fringe = 2.83 cm LOS) to document the **complete deformation cycle** before, during, and after the eruption — one of the earliest and most complete such records from InSAR.

**Pre-eruptive inflation (1992–1995).** Interferograms spanning 1992–1993 show more than four fringes (≥12 cm of uplift) centered on the caldera floor. A second interferogram spanning 1993–1995 adds ~7 cm of additional range change, giving a total of ~18 cm of pre-eruptive LOS uplift. The deformation is centered roughly on the caldera and is broadly consistent with a shallow Mogi source.

**Co-eruptive deflation (1995–1997).** The eruption itself produced the most dramatic signal: **more than 50 fringes** (>140 cm of LOS subsidence) in the interferogram spanning October 1995 to September 1997, which brackets the February–April 1997 eruption. The concentric fringe pattern is centered on the caldera, offset ~5 km from the eruptive vent (Cone A), implying significant lateral magma transport during the eruption. Best-fit Mogi inversion places the deflationary source at **2.7 km depth** beneath the caldera center, with an inferred magma chamber volume change of **0.048 km³**. From this, the volume of erupted material is estimated at 0.055 km³, corresponding to an average lava flow thickness of ~7.4 m — consistent with field measurements.

**Post-eruptive re-inflation (1997–1998).** Within a year of the eruption, ~10 cm of re-inflation is observed in a subsequent interferogram, indicating ongoing magma resupply at the same shallow source location.

```{figure} ../figures/15_okmok_1997.png
---
name: okmok-1997
width: 760px
alt: Deformation interferogram spanning October 9, 1995 to September 9, 1997, which brackets the February 1997 eruption of Okmok volcano. Each fringe represents a 2.83-cm deformation along the satellite look direction. A zoomed portion of the interferogram with dense fringes, outlined by the white box, is shown in the lower left corner.
---
Deformation interferogram spanning October 9, 1995 to September 9, 1997, which brackets the February 1997 eruption of Okmok volcano. Each fringe represents a 2.83-cm deformation along the satellite look direction. A zoomed portion of the interferogram with dense fringes, outlined by the white box, is shown in the lower left corner. From [Lu et al. 2000]( https://doi.org/10.1029/2000JB900034).

```

---

## Large-amplitude Inflation at Sierra Negra, Galápagos (1992–1999)

Sierra Negra, on Isabela Island in the western Galápagos, has the largest caldera by area in the archipelago (59.8 km²) and is one of the most volcanically active. ERS interferograms document **~1.6 m of near-vertical LOS uplift** between 1992 and 1997, one of the largest pre-eruptive inflation signals ever observed by InSAR (Amelung et al., 2000). The inflation was interrupted by a **trapdoor faulting event** in 1997–1998, in which the pre-existing fault system inside the south moat of the caldera slipped by up to 1.5 m — discovered through InSAR and confirmed by field survey. After the faulting event, Sierra Negra resumed uplift, adding ~30 cm of LOS displacement between September 1998 and March 1999.

Sierra Negra is particularly important as a teaching example because the data are **inconsistent with a spherical Mogi source**. Yun et al. (2006) combined ascending and descending ERS-2 interferograms spanning the 1998–1999 uplift episode to decompose the LOS measurements into separate vertical and horizontal components. The ratio of maximum horizontal to maximum vertical surface displacement is ~0.3. A Mogi point source predicts a ratio of ~0.4; a sill-like source predicts a lower ratio consistent with the observations. A spherical or stock-like source is therefore ruled out. Nonlinear inversion using a 3-D boundary element method with a uniform-pressure boundary condition recovers a **horizontal sill at ~2 km depth**, restricted to the inner caldera and bounded by the sinuous ridge, with an estimated excess magma pressure of 4.5 MPa.

This case illustrates two important points beyond Okmok: (1) the combination of ascending and descending interferograms provides enough information to discriminate source geometry; and (2) the ratio $u_\rho / u_z$ — the same geometric ratio that appears in the Mogi solution — is a direct diagnostic of whether the source is equidimensional or sill-like, even before any inversion is performed.

```{figure} ../figures/15_sierra_negra.png
---
name: sierra-negra
width: 740px
alt: Four-panel figure showing ascending and descending ERS-2 interferograms of Sierra Negra caldera and the decomposed vertical and horizontal surface displacement components. The vertical component shows a broad symmetric uplift of ~23 cm; the horizontal (easting) component is small (~7 cm maximum), with the ratio indicating a sill rather than a spherical source.
---
Interferograms from ascending (a) and descending (b) orbits with temporal baselines of 1998/10/31–1999/02/13 and 1998/11/05–1999/
02/18, respectively. One color cycle represents 5-cm change of range in LOS direction of satellite. Interferometric displacements can be
separated into vertical (c) and horizontal (d) components using the imaging geometries of the two orbits.

```

---

## Cryptic Inflation at South Sister, Oregon (1998–2001)

Inflation was discovered at South Sister in Oregon's Cascade Range using InSAR when no other monitoring was in place (Wicks et al., 2002). The uplift — roughly 10 cm over three years — was centered not on the summit but ~5 km to the west, suggesting a source at ~6.5 km depth that had not been recognized as geologically active. No eruption followed, but the discovery highlighted the ability of InSAR to detect geologic hazards at unmonitored systems.

```{figure} ../figures/15_sisters.jpg
---
name: South Sister
width: 700px
alt: ERS interferogram showing 10 cm of uplift at a site 5 km west of South Sister volcano, Oregon. The bulls-eye is offset from any known volcanic vent.
---
ERS interferogram (1998–2001) showing ~10 cm of LOS uplift ~5 km west of South Sister, Oregon (Wicks et al., 2002). The source was inferred at ~6.5 km depth. This case illustrates that InSAR can discover new hazards at apparently dormant systems.
```

---

## Ongoing Inflation at Domuyo, Argentina (2014–present)

Domuyo, in northern Patagonia, is a large silicic system with no historic eruptions. ALOS-2 and Sentinel-1 InSAR data from 2014 onward show ongoing inflation at ~12 cm/yr LOS, adding up to ~60 cm of range change over four years (Lundgren et al., 2020). The deformation source is modeled as an **oblate ellipsoidal sill** (not a Mogi sphere) at ~6.5 km depth — a good example of how the choice of source model matters. This interferogram is used in the accompanying laboratory.

```{figure} ../figures/03_domuyo_alos2.png
---
name: Domuyo ALOS-2
width: 760px
alt: 3x3 grid of ALOS-2 L-band wrapped interferograms of Domuyo volcano, Argentina, spanning 2015-2018. Each panel shows an elliptical bulls-eye of inflation fringes centered on the volcano. The longest baseline interferogram (bottom center, Feb 2015 to Apr 2018) shows ~5 color cycles indicating approximately 50 cm of LOS uplift.
---
ALOS-2 ascending interferograms (Path 34) of Domuyo volcano, Argentina, from Lundgren et al. (2020), Sci. Rep. 10, 11642 (CC BY 4.0). Re-wrapped at 10 cm per color cycle. The longest-baseline interferogram (bottom center, 2015–2018) shows ~5 fringes, corresponding to ~50 cm of LOS uplift at the peak. Source depth is ~6.5 km. Used in the accompanying laboratory.
```

---

# Volcanic Deflation

## Characteristics of Deflation Signals

Deflation and inflation produce identical fringe patterns in a wrapped interferogram. The two are distinguished only by the **direction of fringe cycling** relative to the satellite convention:

- **Inflation**: LOS shortens (ground moves toward satellite) → fringes cycle in the inflation direction (depends on sign convention of the processor)
- **Deflation**: LOS lengthens (ground moves away from satellite) → fringes cycle in the opposite direction

In practice, the fastest way to determine inflation vs. deflation is to compare the sign of the **unwrapped LOS displacement** at the deformation peak: positive (toward satellite) = inflation; negative (away from satellite) = deflation.

> A wrapped interferogram shows a bulls-eye centered on a caldera. How would you determine whether it represents inflation or deflation?

---

# Inflation–Deflation Cycles

## Kīlauea, Hawaiʻi

Kīlauea is among the best-instrumented volcanoes on Earth, and its deformation record is one of the most complete in volcanology. The HVO network of tiltmeters, continuous GNSS, and InSAR has captured **repeating cycles of summit inflation followed by co-eruptive deflation** tied directly to eruptions at the summit and along the rift zones.

The inflation–deflation pattern reflects a relatively shallow (<5 km) magma reservoir beneath Halemaʻumaʻu crater. During quiescence, magma accumulates and the summit inflates. When an eruption begins — either at the summit or fed by dike intrusion into the East or Southwest Rift Zone — the reservoir depressurizes rapidly and the summit deflates.

The three measurement types each reveal a different face of the same cycle. **Tiltmeters** on the caldera rim (within ~1–2 km of the epicenter, near the peak tilt radius $\rho = d/2$ for a ~2 km deep source) resolve the fastest events: hourly DRE oscillations, lava lake surges, and minute-scale precursors to vent collapses. **GNSS** stations integrate those rapid signals into the multi-year uplift and subsidence record, directly mapping $u_z$ and $u_\rho$ and providing the depth estimate via their ratio. **InSAR** captures the cumulative spatial field — the bulls-eye pattern — at whatever time span the interferogram spans, confirming that the deformation is symmetric and reservoir-like.

```{figure} ../figures/03_kilauea_gnss.png
---
name: Kīlauea GNSS
width: 760px
alt: Several years of vertical and horizontal GNSS time series from stations on the Kīlauea caldera rim, showing repeated cycles of gradual inflation punctuated by rapid co-eruptive deflation steps tied to eruption events at the summit and rift zones.
---
GNSS time series from stations on the Kīlauea caldera rim showing repeated inflation–deflation cycles. Gradual inter-eruption inflation is punctuated by rapid co-eruptive deflation. The amplitude and duration of each cycle reflect the volume of magma erupted relative to the supply rate from the mantle source. Data from USGS Hawaiian Volcano Observatory.
```

The 2018 lower East Rift Zone eruption provides the most dramatic recent example. As the eruption drained the shallow summit reservoir, the caldera floor subsided by roughly **500 m** over several weeks — one of the largest volcanic collapses observed in the modern instrumental record. InSAR captured this in extraordinary detail, with hundreds of centimeters of subsidence producing extremely dense fringe patterns that required special unwrapping strategies.

```{figure} ../figures/03_kilauea_2018.png
---
name: Kīlauea 2018 collapse
width: 760px
alt: Sentinel-1 interferogram of the Kīlauea summit showing dense concentric fringes from the 2018 caldera collapse, with hundreds of centimeters of subsidence. Time series panel shows the step-wise nature of the collapse progression over weeks of episodic events.
---
Sentinel-1 interferogram of the Kīlauea summit area during the 2018 lower East Rift Zone eruption. Each step in the caldera collapse corresponded to a discrete subsidence event tied to the eruption rhythm. Total subsidence exceeded 500 m, making this one of the largest instrumentally recorded volcanic collapses. After Neal et al. (2019) and Anderson et al. (2019).
```

The Kīlauea record is pedagogically valuable for several reasons. The **timescale is rapid** — days to months rather than years — making it possible to watch the full inflation–deflation cycle evolve in near real time. The source geometry is well-constrained from decades of inversions (shallow reservoir at ~1–3 km depth, well-approximated by a Mogi source for the inflation phase). And all three measurement types operate simultaneously, so students can compare what tiltmeters, GNSS, and InSAR see from the same source event. The 2018 collapse required more complex models for the collapse mechanics, but the pre-collapse inflation and much of the co-collapse subsidence are well-described by Mogi geometry.

> Compare the Kīlauea inflation–deflation cycle (months timescale, shallow source, eruption-driven) to the Domuyo case (multi-year timescale, 6.5 km depth, no eruption). What does the timescale of a deformation cycle tell you about the depth and permeability of the magmatic system?

Inflation–deflation cycles are also documented at:
- **Campi Flegrei** (Italy): decadal cycles with ~1.8 m of inflation in 1982–1984 prompting mass evacuation; linked to hydrothermal and magmatic pressure changes
- **Yellowstone** caldera (Wyoming): decimeter-scale cycles driven by hydrothermal fluid migration and episodic magma replenishment
- **Fernandina** (Galápagos): multiple eruption–deflation cycles documented by InSAR, with rapid co-eruptive subsidence similar in character to Kīlauea

---

# Limitations of the Mogi Model

The Mogi source is powerful precisely because it has only three free parameters (depth, volume change, and horizontal position), but its simplicity has costs:

**Geometric limitations.** Real magma bodies are not spherical point sources. Sills, dikes, laccolith-like bodies, and irregular reservoirs all produce deformation patterns that may differ from the Mogi prediction. A sill source at the same depth produces a broader, flatter LOS profile than a sphere.

**Assumption of homogeneity.** A layered crust, elastic–viscoelastic rheology, and topographic relief all modify the displacement field. Viscoelastic models typically require larger volume changes to produce the same surface deformation, so Mogi-derived $\Delta V$ estimates from elastic models may underestimate the true volume change.

**Point-source approximation.** The approximation $a \ll d$ breaks down for large magma bodies or shallow sources. McTigue (1987) derived a finite-sphere correction that is important when the source radius is a significant fraction of its depth.

The next lecture addresses dike intrusion geometries, which produce distinctly asymmetric deformation patterns that cannot be explained by the Mogi model.

---

# Volcano Deformation I Summary

- Magma inflation pressurizes the surrounding elastic crust, producing a surface displacement field that is outward and upward and centered above the source.
- The Mogi (1958) point source predicts axially symmetric displacements: $u_z \propto d\,(\rho^2+d^2)^{-3/2}$ and $u_\rho \propto \rho\,(\rho^2+d^2)^{-3/2}$, where $\rho$ is horizontal surface distance.
- Source depth controls signal width; volume change and depth together control amplitude. The half-amplitude radius $\rho_{1/2} \approx 0.77d$ is a direct depth estimator.
- Surface tilt $\tau = -\partial u_z/\partial\rho = (3d/(\rho^2+d^2))\,u_\rho$ is directly computable from the Mogi displacements. It is zero above the source, peaks at $\rho = d/2$, and is the fastest-responding observable.
- GNSS, tiltmeters, and InSAR all sample the same Mogi deformation field at different spatial and temporal scales: tilt resolves hourly transients, GNSS integrates displacement over years, InSAR maps the full spatial pattern.
- Volcanic inflation and deflation have been documented at dozens of volcanoes worldwide. InSAR has revealed unrest at previously unmonitored systems.

---

# Laboratory

Students will implement the Mogi forward model in Python and use it to explore the relationship between source parameters and observable deformation:

- implement the Mogi displacement equations and verify the depth–width scaling relationship
- derive and plot the tilt profile; confirm that maximum tilt is at $\rho = d/2$ and that tilt is proportional to horizontal displacement
- generate and display synthetic wrapped interferograms
- explore how incidence angle and look direction affect the LOS signal
- invert a digitized radial LOS profile from an ALOS-2 interferogram of Domuyo volcano to recover source depth and volume change rate

---

# Additional Resources

> **Textbook:** Segall, P. (2010). *Earthquake and Volcano Deformation*. Princeton University Press.  
> Chapter 7 derives the Mogi source and several related source models from first principles. The clearest textbook treatment of elastic volcano source models.

> **Original paper:** Mogi, K. (1958). Relations between the eruptions of various volcanoes and the deformations of the ground surfaces around them. *Bull. Earthquake Res. Inst. Univ. Tokyo*, 36, 99–134.  
> The 1958 paper that introduced the point-source model still widely used today.

> **Review:** Lisowski, M. (2007). Analytical volcano deformation source models. In *Volcano Deformation*, D. Dzurisin (Ed.), Springer-Praxis. Pp. 279–304.  
> A thorough survey of Mogi, sill, dike, and finite-sphere source models with worked examples.

> **InSAR at volcanoes:** Dzurisin, D. (2007). *Volcano Deformation: Geodetic Monitoring Techniques*. Springer-Praxis.  
> Comprehensive treatment of all geodetic methods applied to volcanic unrest — tiltmeters, leveling, GNSS, and InSAR — including many case studies and instrument descriptions.

> **Kīlauea tilt and DRE events:** Cervelli, P. F., & Miklius, A. (2003). The shallow magmatic system of Kīlauea Volcano. In *The Pu'u 'Ō'ō–Kūpaianaha Eruption of Kīlauea Volcano, Hawai'i*, USGS Professional Paper 1676. — Describes the summit tiltmeter network and its record of inflation–deflation events tied to eruption cycles.

> **Kīlauea tilt and lava lake:** Patrick, M. R., et al. (2015). Identifying and monitoring collapse features at Kīlauea summit using tiltmeters. *JGR Solid Earth*, 120, 2273–2292. — DRE events, lava lake dynamics, and what tilt reveals about the shallow plumbing system.

> **Okmok:** Lu, Z., Masterlark, T., Power, J., Dzurisin, D., & Wicks, C. (2002). Subsurface imaging of the magma plumbing structure at Okmok volcano, Alaska, using InSAR. *JGR*, 107, ECV 3-1.

> **Kīlauea 2018:** Neal, C. A., et al. (2019). The 2018 rift eruption and summit collapse of Kīlauea Volcano. *Science*, 363, 367–374. — The definitive overview of the 2018 events, with geodetic, seismic, and observational data.

> **Kīlauea 2018 geodesy:** Anderson, K. R., et al. (2019). Magma reservoir failure and the onset of caldera collapse at Kīlauea Volcano in 2018. *Science*, 366, eaaz1822. — Modeling of the collapse dynamics from InSAR and GNSS.

> **Kīlauea InSAR:** Poland, M. P., Miklius, A., & Montgomery-Brown, E. K. (2014). Magma supply, storage, and transport at shield-stage Hawaiian volcanoes. In *Characteristics of Hawaiian Volcanoes*, USGS Professional Paper 1801. — Comprehensive treatment of Kīlauea's deformation record and reservoir structure.

> **South Sister:** Wicks, C. W., et al. (2002). Uplift, thermal unrest and magma intrusion at the South Sister volcano, Oregon. *Science*, 318, 1333–1336.

> **Domuyo:** Lundgren, P., et al. (2020). The dynamics of large silicic systems from satellite remote sensing observations: the intriguing case of Domuyo volcano, Argentina. *Sci. Rep.*, 10, 11642. (CC BY 4.0)

> **Interactive lab tool:** A browser-based Mogi explorer and Domuyo inverse problem is available at the course website. Use it to build intuition before the Python laboratory.
