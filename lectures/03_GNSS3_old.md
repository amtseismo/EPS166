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

```{figure} ../figures/03_western_us_velocity_field.jpg
---
width: 700px
alt: North America-fixed horizontal GNSS velocity field across the western United States.
---
Global Positioning System (GPS) horizontal velocity field used in this study. Colors represent the velocity. Vectors that have a gray outline are from campaign data, and the remaining velocities are derived from data analyzed by the Nevada Geodetic Lab (NGL). This velocity field is corrected for postseismic viscoelastic deformation following many large regional earthquakes (see Postseismic correction section and supplemental material). The red outline is California’ s Great Valley, within which we do not consider most GPS stations unless they appear stable and located on bedrock or at least not on sediments (as inferred from satellite images).  Image from [Kreemer and Young, Seismological Research Letters, 2022](https://pubs.geoscienceworld.org/ssa/srl/article/93/6/2990/615948/Crustal-Strain-Rates-in-the-Western-United-States)  
```

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

# Measuring Strain

A Velocity Field Contains Three Different Kinds of Motion

```{figure} ../figures/03_translation_rotation_strain.png
---
width: 900px
alt: Three triangles illustrating translation, rigid rotation, and strain.
---
Translation changes position, rotation changes orientation, and deformation (aka strain) changes shape or size. Only the third contributes to the symmetric strain-rate tensor.
```

The phrase “rotational strain” is sometimes used informally, but rigid-body rotation is **not strain**: it preserves lengths and angles.

---

## Approximate the Local Velocity Field as Linear

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

## Remove Translation First

For three stations, the GETSI construction begins with the network centroid:

$$
\bar{\mathbf x}=\frac{1}{3}\sum_i\mathbf x_i,
\qquad
\bar{\mathbf v}=\frac{1}{3}\sum_i\mathbf v_i.
$$

Subtracting $\bar{\mathbf v}$ places the original and translated triangle centroids together. The remaining relative velocities contain rotation and deformation.

> **Visualize:** Move a transparent triangle across the screen, then align its centroid with the starting triangle.

---

## Separate Rotation from Strain

The velocity gradient separates into symmetric and antisymmetric parts:

$$
\mathbf L =
\underbrace{\frac{1}{2}(\mathbf L+\mathbf L^T)}_{\text{strain rate }\dot{\boldsymbol\epsilon}}
+
\underbrace{\frac{1}{2}(\mathbf L-\mathbf L^T)}_{\text{rigid-body rotation }\mathbf W}.
$$

The symmetric part changes shape. The antisymmetric part rotates the region without deforming it.


# Using Velocities from a Triangle of GNSS Sites to Investigate Crustal Strain

EarthScope GPS Crustal Strain Curriculum

Adapted from the GETSI teaching activity *Using Velocities From a Triangle of GPS Sites to Investigate Crustal Strain*.

---

# A Simple Two-Dimensional Example

We begin with the locations and horizontal velocities of three non-collinear GNSS stations.

| Site | East coordinate | North coordinate | East velocity | North velocity |
|---|---:|---:|---:|---:|
| 1 | 518 | 243 | -1.0 | 1.2 |
| 2 | 523 | 244 | -1.0 | 0.8 |
| 3 | 520 | 248 | 0.4 | 0.2 |

The coordinate and velocity units must be internally consistent. In a real application, positions might be expressed in kilometers and velocities in millimeters per year.

---

# Locate Three Non-Collinear GNSS Stations

Three non-collinear stations define a triangle. Their relative motions allow us to estimate a uniform horizontal velocity gradient within that triangle.

```{figure} ../figures/03_strain_triangle_step_03.jpg
---
width: 620px
alt: Three GNSS stations plotted at different east and north coordinates on a rectangular grid.
---
The locations of the three GNSS stations in a local east-north coordinate system.
```

---

# Each Velocity Has East and North Components

At each station, GNSS provides an east-west component, $v_E$, and a north-south component, $v_N$.

```{figure} ../figures/03_strain_triangle_step_04.jpg
---
width: 620px
alt: Three GNSS stations with separate blue arrows showing their east-west and north-south velocity components.
---
East-west and north-south velocity components at the three stations.
```

---

# Combine the Components into a Velocity Vector

The total horizontal velocity is

$$
\mathbf v_i = (v_{E,i},v_{N,i}),
\qquad
|\mathbf v_i|=\sqrt{v_{E,i}^2+v_{N,i}^2}.
$$

```{figure} ../figures/03_strain_triangle_step_05.jpg
---
width: 620px
alt: Three GNSS stations showing east and north components alongside the resulting diagonal velocity vectors.
---
The east and north components combine to form the total horizontal velocity at each station.
```

---

# The Three Stations Have Different Velocities

If all three velocity vectors were identical, the triangle would translate without changing shape. Differences among the vectors contain information about deformation and rotation.

```{figure} ../figures/03_strain_triangle_step_06.jpg
---
width: 620px
alt: Three GNSS stations with black arrows showing their total horizontal velocities.
---
Total horizontal velocities at the three stations.
```

---

# Connect the Stations to Define the Region

We approximate the deformation inside the triangle as spatially uniform.

```{figure} ../figures/03_strain_triangle_step_07.jpg
---
width: 620px
alt: A triangle connecting three GNSS stations, with a velocity arrow at each vertex.
---
The station triangle defines the region over which translation, rotation, and strain are estimated.
```

---

# Find the Triangle's Centroid

For three stations, the centroid is the mean station position:

$$
\bar{\mathbf x}=\frac{1}{3}\sum_{i=1}^{3}\mathbf x_i.
$$

```{figure} ../figures/03_strain_triangle_step_08.jpg
---
width: 620px
alt: A GNSS station triangle with construction lines drawn from each vertex to a central intersection marking the centroid.
---
The centroid provides a convenient origin for describing the triangle's motion and deformation.
```

---

# Move the Coordinate Origin to the Centroid

Define local positions relative to the centroid:

$$
\mathbf x_i'=\mathbf x_i-\bar{\mathbf x}.
$$

This translation of the coordinate origin simplifies the calculation but does not change station separations or the physical deformation.

```{figure} ../figures/03_strain_triangle_step_09.jpg
---
width: 620px
alt: GNSS station triangle plotted in a local coordinate system whose east and north axes intersect at the triangle centroid.
---
The same station triangle expressed using a local coordinate origin at its centroid.
```

---

# Use a Circle to Visualize Deformation

Imagine a circle painted on the ground near the center of the undeformed triangle. Translation moves the circle, rotation turns it, and strain changes it into an ellipse.

```{figure} ../figures/03_strain_triangle_step_10.jpg
---
width: 620px
alt: A circle inscribed near the center of a triangular GNSS network.
---
A conceptual circle provides a visual marker for separating translation, rotation, and strain.
```

---

# The Mean Station Velocity Is the Translation

The translational velocity of the triangle is the average of the three station velocities:

$$
\bar{\mathbf v}=\frac{1}{3}\sum_{i=1}^{3}\mathbf v_i.
$$

```{figure} ../figures/03_strain_triangle_step_11.jpg
---
width: 620px
alt: GNSS station triangle containing a circle and an arrow from the centroid representing the mean station velocity.
---
The mean velocity vector represents translation of the triangle as a whole.
```

---

# The Triangle Translates and Changes Shape

Applying the observed velocities moves each vertex to a new position. The centroid-to-centroid vector equals the mean translational velocity.

```{figure} ../figures/03_strain_triangle_step_12.jpg
---
width: 620px
alt: Original and displaced GNSS station triangles with an arrow connecting their centroids and a circle moving with the triangle.
---
The observed station velocities produce translation together with changes in the triangle's shape and orientation.
```

---

# Remove the Common Translation

Subtract the mean velocity from every station:

$$
\mathbf v_i'=\mathbf v_i-\bar{\mathbf v}.
$$

The original and displaced centroids then coincide.

```{figure} ../figures/03_strain_triangle_step_13.jpg
---
width: 620px
alt: Original and displaced station triangles being aligned by subtracting the arrow connecting their centroids.
---
Removing the mean velocity eliminates translation while preserving relative motion among the stations.
```

---

# Centering Exposes Relative Motion

Once the centroids are aligned, the remaining differences reflect a combination of rigid-body rotation and strain.

```{figure} ../figures/03_strain_triangle_step_14.jpg
---
width: 620px
alt: Original and deformed station triangles superimposed at a common centroid with residual velocity arrows at their vertices.
---
The centered triangles reveal changes in shape and orientation that were obscured by their common translation.
```

---

# Residual Velocities Change the Triangle's Shape

The residual vectors $\mathbf v_i'$ describe how each station moves relative to the network as a whole.

```{figure} ../figures/03_strain_triangle_step_15.jpg
---
width: 620px
alt: Superimposed original and deformed triangles with centered circles and residual vectors at the vertices.
---
After translation is removed, the remaining station velocities contain deformation and rigid-body rotation.
```

---

# Strain Turns the Circle into an Ellipse

The major and minor axes of the ellipse are the principal strain directions. In the diagram, red marks the major axis and blue marks the minor axis.

```{figure} ../figures/03_strain_triangle_step_16.jpg
---
width: 620px
alt: Circle deformed into an ellipse inside superimposed station triangles, with red major and blue minor principal axes.
---
A circle becomes an ellipse under homogeneous horizontal strain; its axes show the principal strain directions.
```

---

# Principal Axes Remain Perpendicular

Along the principal directions, deformation is purely extensional or contractional and there is no shear component. The two principal axes therefore remain perpendicular.

```{figure} ../figures/03_strain_triangle_step_17.jpg
---
width: 620px
alt: Original circle and strain ellipse with perpendicular red and blue axes shown before and after deformation.
---
The principal axes identify mutually perpendicular directions of maximum and minimum horizontal strain.
```

---

# Shape Change and Rotation Occur Together

Reversing the relative motion shows that the strain ellipse differs from the original circle in both shape and orientation.

```{figure} ../figures/03_strain_triangle_step_18.jpg
---
width: 620px
alt: Superimposed original and deformed triangles with a circle, strain ellipse, and two orientations of the principal axes.
---
The deformation contains a symmetric shape change and an angular change in orientation.
```

---

# Rotation Is Measured by an Angular Change

The angle $\Omega$ records the rigid-body rotation of the local velocity field. Rotation changes orientation but does not, by itself, change lengths or angles within the material.

```{figure} ../figures/03_strain_triangle_step_19.jpg
---
width: 620px
alt: Original and deformed triangles with two red principal-axis lines separated by an angle labeled omega.
---
The angular difference between the original and rotated axes represents the rigid-body rotation component.
```

---

# Begin with the Undeformed Triangle

The complete construction starts with the original triangle, the conceptual circle, and the measured velocity at each station.

```{figure} ../figures/03_strain_triangle_step_20.jpg
---
width: 620px
alt: Undeformed GNSS station triangle containing a circle, with a velocity vector at each vertex.
---
Initial station geometry and observed horizontal velocities.
```

---

# Apply the Station Velocities

Each vertex follows its own velocity vector. Differences among the vectors cause the triangle to translate, rotate, and change shape.

```{figure} ../figures/03_strain_triangle_step_21.jpg
---
width: 620px
alt: GNSS station triangle with multiple arrows illustrating motion of each vertex toward its displaced position.
---
Applying the station velocities produces a displaced and deformed triangle.
```

---

# The Final Geometry Records Strain and Rotation

After the common translation is removed, the final triangle and strain ellipse show the internal deformation of the network.

```{figure} ../figures/03_strain_triangle_step_22.jpg
---
width: 620px
alt: Deformed station triangle centered on a strain ellipse with red major and blue minor principal axes; original station positions remain marked outside the triangle.
---
The final centered geometry summarizes the triangle's strain and rotation relative to its original configuration.
```

---

# Key Takeaways

- The average station velocity describes translation of the network.
- Differences among station velocities describe rotation and strain.
- Rigid rotation changes orientation without changing shape.
- The principal strain rates describe extension or contraction along perpendicular axes.
- A three-station solution represents uniform deformation averaged over the triangle.

> In real GNSS data, station geometry, measurement uncertainty, reference frame, and spatial scale all influence the interpretation.

---

## The Horizontal Strain-Rate Tensor

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

## GNSS Velocities Provide the Observations

For station $i$ at local coordinates $(x_i,y_i)$:

$$
v_{E,i}=t_E-\omega y_i+\dot\epsilon_{EE}x_i+\dot\epsilon_{EN}y_i,
$$

$$
v_{N,i}=t_N+\omega x_i+\dot\epsilon_{EN}x_i+\dot\epsilon_{NN}y_i.
$$

The six unknowns are two translations, one rotation rate, and three independent strain-rate components.

---

## Why Use Three Stations?

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

## Principal Strain Rates 

The eigenvalues of $\dot{\boldsymbol\epsilon}$ are the principal strain rates $\dot\epsilon_1$ and $\dot\epsilon_2$. Their eigenvectors give the corresponding directions.

```{figure} figures/04_strain_ellipse.png
---
width: 560px
alt: A circle deformed into an ellipse with major and minor principal axes.
---
A circle becomes an ellipse under homogeneous strain. Along the principal axes, deformation is purely extensional or contractional, with no shear component.
```

---

## Principal Strain Rates

By convention,

$$
\dot\epsilon_1 \geq \dot\epsilon_2.
$$

The signs of the two principal strain rates describe the deformation:

- $\dot\epsilon_1>0$ and $\dot\epsilon_2>0$: extension in both directions
- $\dot\epsilon_1<0$ and $\dot\epsilon_2<0$: contraction in both directions
- $\dot\epsilon_1>0$ and $\dot\epsilon_2<0$: extension in one direction and contraction in the other
- one principal strain rate near zero: approximately uniaxial deformation

The principal axes identify the directions of maximum extension and contraction. They do not, by themselves, uniquely identify the responsible fault or tectonic process.

```{figure} ../figures/03_principal_strain_patterns.png
---
width: 800px
alt: Circles deforming into ellipses under extension, contraction, and combined extension and contraction, with principal strain axes indicated.
---
Possible deformation patterns described by the signs of the maximum and minimum principal strain rates. Open arrows indicate extension and filled arrows indicate contraction. Adapted from the GETSI GPS Triangle Strain Calculator materials.

---

## Other Useful Quantities

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

**Maximum engineering shear strain rate**

$$
\dot\gamma_{\max}=|\dot\epsilon_1-\dot\epsilon_2|.
$$

Maximum shear occurs along directions oriented $45^\circ$ from the principal strain axes.

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

# Source

> **Teaching material:** EarthScope/GETSI, *Using Velocities From a Triangle of GPS Sites to Investigate Crustal Strain*, EarthScope GPS Crustal Strain Curriculum Team. Original presentation version dated September 9, 2012; contact information updated by EarthScope.

- Kreemer, C., Hammond, W. C., and Blewitt, G. (2022), *Crustal Strain Rates in the Western United States and Their Relationship with Earthquake Rates*, **Seismological Research Letters**, 93, 2990–3006.
- Kreemer et al. velocity dataset: [doi:10.7910/DVN/BICMWB](https://doi.org/10.7910/DVN/BICMWB).
- GETSI/EarthScope, *Infinitesimal Strain Analysis Using GPS Data* teaching materials.
- Savage et al. (2001), method underlying the supplied GETSI `calcstrain.m` implementation.
