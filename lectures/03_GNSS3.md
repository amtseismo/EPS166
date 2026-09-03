# GNSS III: From Velocity to Tectonic Strain

## Purpose

GNSS stations measure motion at individual points. Tectonic strain describes how the distances and angles **between** those points change through time.

In this lecture, we will:

- distinguish translation, rotation, and strain
- construct a local velocity-gradient model from GNSS velocities
- interpret normal strain, shear strain, principal axes, and dilatation
- connect strain-rate estimates to tectonic processes
- recognize how reference frame, station geometry, and spatial scale affect the result

---

# What Do You See in the Western U.S. Velocity Field?

Before calculating anything, describe the pattern:

- Where are velocities largest?
- How do their directions change from California to Washington?
- Does the turning of the arrows necessarily mean that the crust is straining?

```{figure} figures/04_western_us_velocity_field.png
---
width: 580px
alt: North America-fixed horizontal GNSS velocity field across the western United States.
---
North America-fixed GNSS velocities used by Kreemer et al. (2022). Colors indicate speed. The field contains rigid translation, block rotation, elastic strain accumulation, and distributed deformation.
```

---

# Velocity Is Not Strain

A GNSS velocity describes the motion of one station:

$$
\mathbf v_i = (v_{E,i},v_{N,i}).
$$

Strain describes a **spatial gradient** in velocity. If neighboring stations have identical velocities, their separation does not change and the region has no internal strain.

> **Prediction:** Three stations all move northwest at 25 mm/yr. What happens to the triangle connecting them after 100 years?

---

# Strain Measures Change in Shape or Size

For a line with original length $L$, infinitesimal normal strain is

$$
\epsilon = \frac{\Delta L}{L}.
$$

For continuously moving crust, we usually estimate **strain rate**:

$$
\dot\epsilon = \frac{1}{L}\frac{dL}{dt}.
$$

- $\dot\epsilon>0$: extension
- $\dot\epsilon<0$: contraction
- strain is dimensionless; strain rate has units of time$^{-1}$

---

# A Velocity Field Contains Three Different Kinds of Motion

```{figure} figures/04_translation_rotation_strain.png
---
width: 900px
alt: Three triangles illustrating translation, rigid rotation, and strain.
---
Translation changes position, rotation changes orientation, and strain changes shape or size. Only the third contributes to the symmetric strain-rate tensor.
```

The phrase “rotational strain” is sometimes used informally, but rigid-body rotation is **not strain**: it preserves lengths and angles.

---

# Approximate the Local Velocity Field as Linear

Near the center of a small region,

$$
\mathbf v(\mathbf x) = \mathbf t + \mathbf L\mathbf x,
$$

where:

- $\mathbf t$ is translation of the region
- $\mathbf x$ is position relative to the network centroid
- $\mathbf L=\nabla\mathbf v$ is the horizontal velocity gradient

This approximation treats strain and rotation as uniform inside the selected network.

---

# Remove Translation First

For three stations, the GETSI construction begins with the network centroid:

$$
\bar{\mathbf x}=\frac{1}{3}\sum_i\mathbf x_i,
\qquad
\bar{\mathbf v}=\frac{1}{3}\sum_i\mathbf v_i.
$$

Subtracting $\bar{\mathbf v}$ places the original and translated triangle centroids together. The remaining relative velocities contain rotation and deformation.

> **Visualize:** Move a transparent triangle across the screen, then align its centroid with the starting triangle.

---

# Separate Rotation from Strain

The velocity gradient separates into symmetric and antisymmetric parts:

$$
\mathbf L =
\underbrace{\frac{1}{2}(\mathbf L+\mathbf L^T)}_{\text{strain rate }\dot{\boldsymbol\epsilon}}
+
\underbrace{\frac{1}{2}(\mathbf L-\mathbf L^T)}_{\text{rigid-body rotation }\mathbf W}.
$$

The symmetric part changes shape. The antisymmetric part rotates the region without deforming it.

---

# The Horizontal Strain-Rate Tensor

$$
\dot{\boldsymbol\epsilon}=
\begin{bmatrix}
\dot\epsilon_{EE} & \dot\epsilon_{EN}\\
\dot\epsilon_{EN} & \dot\epsilon_{NN}
\end{bmatrix}.
$$

- $\dot\epsilon_{EE}$: east–west extension or contraction
- $\dot\epsilon_{NN}$: north–south extension or contraction
- $\dot\epsilon_{EN}$: shear deformation

These components depend on the coordinate-axis orientation; the principal strain rates do not.

---

# GNSS Velocities Provide the Observations

For station $i$ at local coordinates $(x_i,y_i)$:

$$
v_{E,i}=t_E-\omega y_i+\dot\epsilon_{EE}x_i+\dot\epsilon_{EN}y_i,
$$

$$
v_{N,i}=t_N+\omega x_i+\dot\epsilon_{EN}x_i+\dot\epsilon_{NN}y_i.
$$

The six unknowns are two translations, one rotation rate, and three independent strain-rate components.

---

# Why Does the GETSI Calculator Use Three Stations?

Three stations provide six horizontal velocity observations:

$$
3\ \text{stations}\times2\ \text{components}=6\ \text{observations}.
$$

That is exactly enough to solve for six model parameters.

But an exact solution has no redundancy:

- one anomalous station affects every parameter
- a narrow or nearly collinear triangle is poorly conditioned
- the result is an average over the triangle, not a point measurement

---

# Principal Strain Rates Reveal the Natural Axes

The eigenvalues of $\dot{\boldsymbol\epsilon}$ are the principal strain rates $\dot\epsilon_1$ and $\dot\epsilon_2$. Their eigenvectors give the corresponding directions.

```{figure} figures/04_strain_ellipse.png
---
width: 560px
alt: A circle deformed into an ellipse with major and minor principal axes.
---
A circle becomes an ellipse under homogeneous strain. Along the principal axes, deformation is purely extensional or contractional, with no shear component.
```

---

# Other Useful Quantities

**Dilatation (areal strain rate)**

$$
\dot\epsilon_A=\dot\epsilon_{EE}+\dot\epsilon_{NN}
=\dot\epsilon_1+\dot\epsilon_2.
$$

**Maximum engineering shear strain rate**

$$
\dot\gamma_{max}=|\dot\epsilon_1-\dot\epsilon_2|.
$$

Positive dilatation indicates increasing area; negative dilatation indicates decreasing area.

---

# How Large Is a Nanostrain per Year?

$$
1\ \text{nanostrain/yr}=10^{-9}\ \text{yr}^{-1}.
$$

For a 100-km baseline:

$$
(100\ \text{nanostrain/yr})(100\ \text{km})=10\ \text{mm/yr}.
$$

> **Check:** What relative velocity across 50 km corresponds to 200 nanostrain/yr?

---

# Why Does the PNW Velocity Field Show Broad Rotation?

The apparent turning reflects a superposition of:

- northwest Pacific–North America relative motion in California
- clockwise rotation and northward motion of the Oregon–Washington forearc
- northeastward elastic loading above the locked Cascadia megathrust
- distributed deformation through Walker Lane and the Basin and Range
- some intraplate motion associated with glacial isostatic adjustment

The curved pattern is not itself a map of strain. We must compare neighboring velocities and separate rigid rotation from shape change.

---

# The Answer Depends on the Region You Sample

```{figure} figures/04_spatial_scale.png
---
width: 650px
alt: Small and large station triangles sampling a spatially variable velocity field.
---
A small triangle can resolve localized deformation but is sensitive to individual stations. A large triangle is more stable but averages across structures and may mix tectonic regimes.
```

> **Prediction:** How might a triangle spanning both Cascadia and the Basin and Range differ from one confined to the coastal forearc?

---

# From Numbers to a Tectonic Interpretation

Do not interpret a strain ellipse in isolation. Ask:

1. What reference frame and corrections were used?
2. Which faults or plate boundaries lie inside the station network?
3. Are the principal axes consistent with fault-normal contraction, extension, or strike-slip shear?
4. Is rotation coherent with a crustal block, or produced by a local velocity gradient?
5. Does the conclusion persist when the station geometry changes?

---

# Lab: PNW Guidance, Northern California Application

In the lab you will:

1. map the Kreemer et al. (2022) North America-fixed velocity field
2. calculate translation, rotation, and strain for a prescribed PNW triangle
3. interpret the principal strain rates and their tectonic meaning
4. repeat the analysis near the northern San Andreas fault system
5. perturb one station and evaluate the sensitivity to network geometry

The goal is not merely to obtain a tensor—it is to decide what the tensor can and cannot tell us about the tectonics.

---

# GNSS Strain Summary

- Absolute velocity is not strain; **spatial variation in velocity** produces strain.
- Translation, rigid rotation, and strain are distinct components of a local velocity field.
- Principal strain rates describe the magnitude and orientation of maximum extension and contraction.
- A three-station solution is intuitive but exactly determined and geometry-dependent.
- Tectonic interpretation requires the station map, reference frame, spatial scale, and regional fault geometry.

---

# Sources

- Kreemer, C., Hammond, W. C., and Blewitt, G. (2022), *Crustal Strain Rates in the Western United States and Their Relationship with Earthquake Rates*, **Seismological Research Letters**, 93, 2990–3006.
- Kreemer et al. velocity dataset: [doi:10.7910/DVN/BICMWB](https://doi.org/10.7910/DVN/BICMWB).
- GETSI/EarthScope, *Infinitesimal Strain Analysis Using GPS Data* teaching materials.
- Savage et al. (2001), method underlying the supplied GETSI `calcstrain.m` implementation.
