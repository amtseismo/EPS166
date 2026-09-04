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

# The Western U.S. Velocity Field

Before calculating anything, describe the pattern:

- Where are velocities largest?
- How do their directions change from California to Washington?
- Does the turning of the arrows necessarily mean that the crust is straining?

```{figure} ../figures/03_western_us_velocity_field.jpg
---
width: 700px
alt: North America-fixed horizontal GNSS velocity field across the western United States.
---
North America-fixed horizontal GNSS velocities across the western United States. Color represents velocity magnitude; gray-outlined vectors are based on campaign measurements. The velocities have been corrected for postseismic viscoelastic deformation following large regional earthquakes. From [Kreemer and Young (2022)](https://pubs.geoscienceworld.org/ssa/srl/article/93/6/2990/615948/Crustal-Strain-Rates-in-the-Western-United-States).
```
---

## Why Does the PNW Velocity Field Show Broad Rotation?

The apparent turning reflects a superposition of:

- northwest Pacific–North America relative motion in California
- clockwise rotation and northward motion of the Oregon–Washington forearc
- northeastward elastic loading above the locked Cascadia megathrust
- distributed deformation through Walker Lane and the Basin and Range
- some intraplate motion associated with glacial isostatic adjustment

The curved pattern is not itself a map of strain. We must compare neighboring velocities and separate rigid rotation from shape change.

---

# Strain

**Strain** measures change in shape or size. For a line with original length $L$, infinitesimal normal strain is

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

$$
1\ \text{nanostrain/yr}=10^{-9}\ \text{yr}^{-1}.
$$

In geoscience we frequently consider nanostrain.  For a 100-km baseline:

$$
(100\ \text{nanostrain/yr})(100\ \text{km})=10\ \text{mm/yr}.
$$

> **Check:** What relative velocity across 50 km corresponds to 200 nanostrain/yr?

---

## Velocity Is Not Strain

A GNSS velocity describes the motion of one station:

$$
\mathbf v_i = (v_{E,i},v_{N,i}).
$$

Strain describes a **spatial gradient** in velocity. If neighboring stations have identical velocities, their separation does not change and the region has no internal strain.

> **Prediction:** Three stations all move northwest at 25 mm/yr. What happens to the triangle connecting them after 100 years?

---

## A Velocity Field Contains Three Kinds of Motion

```{figure} ../figures/03_translation_rotation_strain.png
---
width: 900px
alt: Three triangles illustrating translation, rigid rotation, and strain.
---
Translation changes position, rotation changes orientation, and deformation (aka strain) changes shape or size. Only the third contributes to the symmetric strain-rate tensor.
```

The phrase “rotational strain” is sometimes used informally, but rigid-body rotation is **not strain**: it preserves lengths and angles.

---

# Measuring Strain using Velocity

Near the center of a small region, approximate the horizontal velocity field as linear:

$$
\mathbf v(\mathbf x)
=
\mathbf v_0
+
(\nabla\mathbf v)\mathbf x,
$$

where:

- $\mathbf x$ is position relative to the network centroid,
- $\mathbf v_0$ is the velocity at the centroid and represents translation of the network, and
- $\nabla\mathbf v$ is the horizontal velocity-gradient tensor.

This approximation assumes that strain rate and rotation rate are uniform within the selected network.

---

## Separate Strain Rate from Rotation Rate

The velocity gradient contains both deformation and rigid-body rotation:

$$
\nabla\mathbf v
=
\underbrace{
\frac{1}{2}
\left[
\nabla\mathbf v+(\nabla\mathbf v)^T
\right]
}_{\text{symmetric: strain rate }\dot{\boldsymbol\epsilon}}
+
\underbrace{
\frac{1}{2}
\left[
\nabla\mathbf v-(\nabla\mathbf v)^T
\right]
}_{\text{antisymmetric: rotation rate }\dot{\boldsymbol\omega}}.
$$

- $\dot{\boldsymbol\epsilon}$ changes the shape or size of the region.
- $\dot{\boldsymbol\omega}$ rotates the region without deforming it.
- Both strain rate and rotation rate have units of inverse time.

---

## The Horizontal Strain-Rate Tensor

The symmetric part of the velocity gradient is

$$
\dot{\boldsymbol\epsilon}
=
\begin{bmatrix}
\dot\epsilon_{EE} & \dot\epsilon_{EN}\\
\dot\epsilon_{EN} & \dot\epsilon_{NN}
\end{bmatrix},
$$

where

$$
\dot\epsilon_{EE}=\frac{\partial v_E}{\partial x},
\qquad
\dot\epsilon_{NN}=\frac{\partial v_N}{\partial y},
$$

and

$$
\dot\epsilon_{EN}
=
\frac{1}{2}
\left(
\frac{\partial v_E}{\partial y}
+
\frac{\partial v_N}{\partial x}
\right).
$$

- $\dot\epsilon_{EE}$: east–west extension or contraction
- $\dot\epsilon_{NN}$: north–south extension or contraction
- $\dot\epsilon_{EN}$: shear strain rate

These components depend on the orientation of the coordinate axes; the principal strain rates do not.

---

## GNSS Velocities Provide the Observations

Near the center of a small region, we approximate the velocity field as

$$
\mathbf v(\mathbf x)
=
\mathbf v_0 +
(\nabla\mathbf v)\mathbf x.
$$

The six unknowns are:

- two translation rates: $v_{0E}$ and $v_{0N}$
- one rigid-body rotation rate: $\omega$
- three strain-rate components:  
  $\dot\epsilon_{EE}$, $\dot\epsilon_{NN}$, and $\dot\epsilon_{EN}$

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

# Principal Strain Rates

The two principal strain rates are obtained directly from the horizontal strain-rate tensor:

$$
\dot\epsilon_{1,2}
=
\frac{\dot\epsilon_{EE}+\dot\epsilon_{NN}}{2}
\pm
\sqrt{
\left(\frac{\dot\epsilon_{EE}-\dot\epsilon_{NN}}{2}\right)^2
+\dot\epsilon_{EN}^{,2}
}.
$$

By convention, $\dot\epsilon_1\geq\dot\epsilon_2$. The corresponding eigenvectors give the two perpendicular principal directions.

```{figure} ../figures/03_strain_ellipse.png
---
width: 520px
alt: A circle deformed into an ellipse with perpendicular major and minor principal axes.
---
A circle becomes an ellipse under general homogeneous strain. Along the principal axes, deformation is purely extensional or contractional, with no shear component.
```

---

## The Eigenvectors Give the Principal Directions

The orientation $\theta$ of the maximum principal strain-rate axis, measured counterclockwise from east, satisfies

$$
\theta
=
\frac{1}{2}\operatorname{atan2}
\left(2\dot\epsilon_{EN},\dot\epsilon_{EE}-\dot\epsilon_{NN}\right).
$$

The second principal axis is perpendicular to the first. In practice, numerical routines such as `numpy.linalg.eigh` return both eigenvalues and eigenvectors.

> **Key point:** The eigenvalues tell us how fast the crust stretches or contracts; the eigenvectors tell us the directions in which those rates occur.

---

## The Signs Describe the Style of Deformation

- $\dot\epsilon_1>0$ and $\dot\epsilon_2>0$: extension in all horizontal directions
- $\dot\epsilon_1<0$ and $\dot\epsilon_2<0$: contraction in all horizontal directions
- $\dot\epsilon_1>0$ and $\dot\epsilon_2<0$: extension in one direction and contraction in the other
- one principal strain rate near zero: approximately uniaxial deformation

The principal rates are the maximum and minimum normal strain rates. They do not, by themselves, uniquely identify the responsible fault or tectonic process.

```{figure} ../figures/03_principal_strain.png
---
width: 800px
alt: Circles deforming under extension, contraction, and combined extension and contraction, with principal strain axes indicated.
---
Possible deformation patterns described by the signs of the maximum and minimum principal strain rates. Open arrows indicate extension and filled arrows indicate contraction. Adapted from the GETSI GPS Triangle Strain Calculator materials.
```

---

## Other Useful Quantities Follow from the Principal Rates

**Dilatation (areal strain rate)**

$$
\dot\epsilon_A
=\dot\epsilon_{EE}+\dot\epsilon_{NN}
=\dot\epsilon_1+\dot\epsilon_2.
$$

Positive dilatation indicates increasing area; negative dilatation indicates decreasing area.

**Maximum engineering shear strain rate**

$$
\dot\gamma_{\max}=|\dot\epsilon_1-\dot\epsilon_2|.
$$

Maximum engineering shear occurs along directions oriented $45^\circ$ from the principal axes. The maximum tensorial shear strain rate is one-half this value.

---

# Worked Example: Strain from Three GNSS Stations

We will follow three stations through the complete GETSI graphical construction:

1. combine east and north velocity components
2. remove their common translation
3. identify changes in shape
4. separate strain from rigid-body rotation

Adapted from the GETSI teaching activity *Using Velocities From a Triangle of GPS Sites to Investigate Crustal Strain*.

---

## A Simple Two-Dimensional Example

We begin with the locations and horizontal velocities of three non-collinear GNSS stations.

| Site | East coordinate | North coordinate | East velocity | North velocity |
|---|---:|---:|---:|---:|
| 1 | 518 | 243 | -1.0 | 1.2 |
| 2 | 523 | 244 | -1.0 | 0.8 |
| 3 | 520 | 248 | 0.4 | 0.2 |

The coordinate and velocity units must be internally consistent. In a real application, positions might be expressed in kilometers and velocities in millimeters per year.

---

## Locate Three Non-Collinear GNSS Stations

Three non-collinear stations define a triangle. Their relative motions allow us to estimate a uniform horizontal velocity gradient within that triangle.

```{figure} ../figures/03_strain_triangle_step_01.jpg
---
width: 620px
alt: Three GNSS stations plotted at different east and north coordinates on a rectangular grid.
---
The locations of the three GNSS stations in a local east-north coordinate system.
```

---

## Each Velocity Has East and North Components

At each station, GNSS provides an east-west component, $v_E$, and a north-south component, $v_N$.

```{figure} ../figures/03_strain_triangle_step_02.jpg
---
width: 620px
alt: Three GNSS stations with separate blue arrows showing their east-west and north-south velocity components.
---
East-west and north-south velocity components at the three stations.
```

---

## Combine the Components into a Velocity Vector

The total horizontal velocity is

$$
\mathbf v_i = (v_{E,i},v_{N,i}),
\qquad
|\mathbf v_i|=\sqrt{v_{E,i}^2+v_{N,i}^2}.
$$

```{figure} ../figures/03_strain_triangle_step_03.jpg
---
width: 620px
alt: Three GNSS stations showing east and north components alongside the resulting diagonal velocity vectors.
---
The east and north components combine to form the total horizontal velocity at each station.
```

---

## The Three Stations Have Different Velocities

If all three velocity vectors were identical, the triangle would translate without changing shape. Differences among the vectors contain information about deformation and rotation.

```{figure} ../figures/03_strain_triangle_step_04.jpg
---
width: 620px
alt: Three GNSS stations with black arrows showing their total horizontal velocities.
---
Total horizontal velocities at the three stations.
```

---

## Connect the Stations to Define the Region

We approximate the deformation inside the triangle as spatially uniform.

```{figure} ../figures/03_strain_triangle_step_05.jpg
---
width: 620px
alt: A triangle connecting three GNSS stations, with a velocity arrow at each vertex.
---
The station triangle defines the region over which translation, rotation, and strain are estimated.
```

---

## Find the Triangle's Centroid

For three stations, the centroid is the mean station position:

$$
\bar{\mathbf x}=\frac{1}{3}\sum_{i=1}^{3}\mathbf x_i.
$$

```{figure} ../figures/03_strain_triangle_step_06.jpg
---
width: 620px
alt: A GNSS station triangle with construction lines drawn from each vertex to a central intersection marking the centroid.
---
The centroid provides a convenient origin for describing the triangle's motion and deformation.
```

---

## Move the Coordinate Origin to the Centroid

Define local positions relative to the centroid:

$$
\mathbf x_i'=\mathbf x_i-\bar{\mathbf x}.
$$

This translation of the coordinate origin simplifies the calculation but does not change station separations or the physical deformation.

```{figure} ../figures/03_strain_triangle_step_07.jpg
---
width: 620px
alt: GNSS station triangle plotted in a local coordinate system whose east and north axes intersect at the triangle centroid.
---
The same station triangle expressed using a local coordinate origin at its centroid.
```

---

## Use a Circle to Visualize Deformation

Imagine a circle painted on the ground near the center of the undeformed triangle. Translation moves the circle, rotation turns it, and strain changes it into an ellipse.

```{figure} ../figures/03_strain_triangle_step_08.jpg
---
width: 620px
alt: A circle inscribed near the center of a triangular GNSS network.
---
A conceptual circle provides a visual marker for separating translation, rotation, and strain.
```

---

## The Mean Station Velocity Is the Translation

The translational velocity of the triangle is the average of the three station velocities:

$$
\bar{\mathbf v}=\frac{1}{3}\sum_{i=1}^{3}\mathbf v_i.
$$

```{figure} ../figures/03_strain_triangle_step_09.jpg
---
width: 620px
alt: GNSS station triangle containing a circle and an arrow from the centroid representing the mean station velocity.
---
The mean velocity vector represents translation of the triangle as a whole.
```

---

## The Triangle Translates and Changes Shape

Applying the observed velocities moves each vertex to a new position. The centroid-to-centroid vector equals the mean translational velocity.

```{figure} ../figures/03_strain_triangle_step_10.jpg
---
width: 620px
alt: Original and displaced GNSS station triangles with an arrow connecting their centroids and a circle moving with the triangle.
---
The observed station velocities produce translation together with changes in the triangle's shape and orientation.
```

---

## Remove the Common Translation

Subtract the mean velocity from every station:

$$
\mathbf v_i'=\mathbf v_i-\bar{\mathbf v}.
$$

The original and displaced centroids then coincide.

```{figure} ../figures/03_strain_triangle_step_11.jpg
---
width: 620px
alt: Original and displaced station triangles being aligned by subtracting the arrow connecting their centroids.
---
Removing the mean velocity eliminates translation while preserving relative motion among the stations.
```

---

## Centering Exposes Relative Motion

Once the centroids are aligned, the remaining differences reflect a combination of rigid-body rotation and strain.

```{figure} ../figures/03_strain_triangle_step_12.jpg
---
width: 620px
alt: Original and deformed station triangles superimposed at a common centroid with residual velocity arrows at their vertices.
---
The centered triangles reveal changes in shape and orientation that were obscured by their common translation.
```

---

## Residual Velocities Change the Triangle's Shape

The residual vectors $\mathbf v_i'$ describe how each station moves relative to the network as a whole.

```{figure} ../figures/03_strain_triangle_step_13.jpg
---
width: 620px
alt: Superimposed original and deformed triangles with centered circles and residual vectors at the vertices.
---
After translation is removed, the remaining station velocities contain deformation and rigid-body rotation.
```

---

## In This Example, Strain Turns the Circle into an Ellipse

The major and minor axes of the ellipse are the principal strain directions. In the diagram, red marks the major axis and blue marks the minor axis.

If strain were equal in all directions, the circle would change size but remain circular.

```{figure} ../figures/03_strain_triangle_step_14.jpg
---
width: 620px
alt: Circle deformed into an ellipse inside superimposed station triangles, with red major and blue minor principal axes.
---
A circle becomes an ellipse under homogeneous horizontal strain; its axes show the principal strain directions.
```

---

## Principal Axes Remain Perpendicular

Along the principal directions, deformation is purely extensional or contractional and there is no shear component. The two principal axes therefore remain perpendicular.

```{figure} ../figures/03_strain_triangle_step_15.jpg
---
width: 620px
alt: Original circle and strain ellipse with perpendicular red and blue axes shown before and after deformation.
---
The principal axes identify mutually perpendicular directions of maximum and minimum horizontal strain.
```

---

## Shape Change and Rotation Occur Together

Reversing the relative motion shows that the strain ellipse differs from the original circle in both shape and orientation.

```{figure} ../figures/03_strain_triangle_step_16.jpg
---
width: 620px
alt: Superimposed original and deformed triangles with a circle, strain ellipse, and two orientations of the principal axes.
---
The deformation contains a symmetric shape change and an angular change in orientation.
```

---

## The Velocity Field Can Also Contain Rigid Rotation

After translation is removed, the residual velocity field can still contain both deformation and rigid-body rotation.

Rigid rotation changes the orientation of the triangle without changing its internal lengths or angles. It is distinct from the orientation of the principal strain axes.

```{figure} ../figures/03_strain_triangle_step_17.jpg
---
width: 620px
alt: Original and deformed triangles with two red principal-axis lines separated by an angle labeled omega.
---
The angle $\Omega$ represents the rigid-body rotation of the triangle. The red and blue axes describe the orientation of the strain ellipse and should not be interpreted as rotation by themselves.
```
---

## Recap: Begin with the Undeformed Triangle

The complete construction starts with the original triangle, the conceptual circle, and the measured velocity at each station.

```{figure} ../figures/03_strain_triangle_step_18.jpg
---
width: 620px
alt: Undeformed GNSS station triangle containing a circle, with a velocity vector at each vertex.
---
Initial station geometry and observed horizontal velocities.
```
---

## Recap: Apply the Station Velocities

Each vertex follows its own velocity vector. Differences among the vectors cause the triangle to translate, rotate, and change shape.

```{figure} ../figures/03_strain_triangle_step_19.jpg
---
width: 620px
alt: GNSS station triangle with multiple arrows illustrating motion of each vertex toward its displaced position.
---
Applying the station velocities produces a displaced and deformed triangle.
```
---

## The Final Geometry Records Strain and Rotation

After the common translation is removed, the final triangle and strain ellipse show the internal deformation of the network.

```{figure} ../figures/03_strain_triangle_step_20.jpg
---
width: 620px
alt: Deformed station triangle centered on a strain ellipse with red major and blue minor principal axes; original station positions remain marked outside the triangle.
---
The final centered geometry summarizes the triangle's strain and rotation relative to its original configuration.
```
---

## What Did the Graphical Construction Show?

- The average station velocity describes translation of the network.
- Differences among station velocities describe rotation and strain.
- Rigid rotation changes orientation without changing shape.
- The principal strain rates describe extension or contraction along perpendicular axes.
- A three-station solution represents uniform deformation averaged over the triangle.

> In real GNSS data, station geometry, measurement uncertainty, reference frame, and spatial scale all influence the interpretation.

---

## The Answer Depends on the Region You Sample

```{figure} ../figures/04_spatial_scale.png
---
width: 650px
alt: Small and large station triangles sampling a spatially variable velocity field.
---
A small triangle can resolve localized deformation but is sensitive to individual stations. A large triangle is more stable but averages across structures and may mix tectonic regimes.
```

> **Prediction:** How might a triangle spanning both Cascadia and the Basin and Range differ from one confined to the coastal forearc?

---

# From One Triangle to a Regional Strain-Rate Field

The three-station example estimates one strain-rate tensor averaged over one triangle. To construct a regional field, we repeat the same underlying calculation across many neighboring stations or fit a continuous velocity-gradient field to all of the velocities.

At each location:

1. estimate the local velocity-gradient tensor $\mathbf L$
2. retain its symmetric part $\dot{\boldsymbol\epsilon}$
3. calculate $\dot\epsilon_1$, $\dot\epsilon_2$, and their directions
4. map quantities derived from those principal strain rates

Kreemer and Young (2022) use a more robust implementation: triangle-based estimates help identify outliers, followed by a smooth, continuous tensor field fit to the GNSS velocities.

---

# A Geodetic Strain-Rate Field for the Western U.S.

```{figure} ../figures/03_geodetic_strain_rate.png
---
width: 800px
alt: Four maps of the western United States showing geodetic strain-rate magnitude, dilatation, shear rate, and velocity-model misfit.
---
Geodetic strain-rate field. (a) Second invariant of the tensor, $\sqrt{\dot\epsilon_1^2+\dot\epsilon_2^2}$; (b) dilatation rate, $\dot\epsilon_1+\dot\epsilon_2$; (c) shear rate, $\min(|\dot\epsilon_1|,|\dot\epsilon_2|)$ when $\dot\epsilon_1$ and $\dot\epsilon_2$ have opposite signs and zero otherwise; and (d) misfit, $\sqrt{[(v_E^{obs}-v_E^{mod})^2+(v_N^{obs}-v_N^{mod})^2]/2}$, between observed and modeled velocities. Figure 2 from [Kreemer and Young (2022)](https://doi.org/10.1785/0220220153).
```

---

## How Do the Principal Strain Rates Produce These Maps?

Every map cell contains a strain-rate tensor and therefore two principal rates, $\dot\epsilon_1$ and $\dot\epsilon_2$.

- **Large tensor magnitude:** deformation is rapid, regardless of style.
- **Positive dilatation:** the surface area is increasing.
- **Negative dilatation:** the surface area is decreasing.
- **Large shear rate:** extension and contraction occur simultaneously along perpendicular axes.
- **Large velocity misfit:** the smooth model does not reproduce the observations well.

> **Note:** The shear-rate measure used in this figure is $\min(|\dot\epsilon_1|,|\dot\epsilon_2|)$ when the principal rates have opposite signs. It is different from the maximum engineering shear strain rate, $|\dot\epsilon_1-\dot\epsilon_2|$.

> **Interpret:** Where is deformation concentrated? How does the broad contraction in Cascadia differ from the narrow deformation along the San Andreas fault system?

---

## Toward a Tectonic Interpretation

Do not interpret a strain ellipse in isolation. Ask:

1. What reference frame and corrections were used?
2. Which faults or plate boundaries lie inside the station network?
3. Are the principal axes consistent with fault-normal contraction, extension, or strike-slip shear?
4. Is rotation coherent with a crustal block, or produced by a local velocity gradient?
5. Does the conclusion persist when the station geometry changes?

> **Important:** A strain pattern is not a unique indicator of fault type. The same principal strain axes may be compatible with strike-slip, normal, or reverse faulting depending on fault orientation, crustal properties, and pre-existing structures.

---

# GNSS III Strain Summary

- Absolute velocity is not strain; **spatial variation in velocity** produces strain.
- Translation, rigid rotation, and strain are distinct components of a local velocity field.
- Principal strain rates describe the magnitude and orientation of maximum extension and contraction.
- A three-station solution is intuitive but exactly determined and geometry-dependent.
- Tectonic interpretation requires the station map, reference frame, spatial scale, and regional fault geometry.

---

# Laboratory

In the lab you will:

1. map the Kreemer et al. (2022) North America-fixed velocity field
2. calculate translation, rotation, and strain for a prescribed PNW triangle
3. interpret the principal strain rates and their tectonic meaning
4. repeat the analysis near the northern San Andreas fault system
5. perturb one station and evaluate the sensitivity to network geometry

The goal is not merely to obtain a tensor—it is to decide what the tensor can and cannot tell us about the tectonics.

---

# Additional Resources

> **Teaching Activity:** [GETSI: GPS and Infinitesimal Strain Analysis](https://serc.carleton.edu/getsi/teaching_materials/gps_strain/unit4.html)  
> Teaching materials for calculating and interpreting strain from the velocities of three GNSS stations.

> **Calculator Guide:** [GPS Strain and Earthquakes: Explanation of Strain Calculator Output](../figures/03_gps_strain_calculator_handout.pdf)  
> A guide to interpreting the translation, rotation, principal strain, shear, and dilatation values produced by the GPS Triangle Strain Calculator.

> **Research Article:** [Crustal Strain Rates in the Western United States and Their Relationship with Earthquake Rates](https://doi.org/10.1785/0220220153)  
> Kreemer and Young’s regional analysis connecting GNSS velocities, crustal strain rates, and earthquake occurrence.

> **Velocity Dataset:** [Western U.S. GNSS Velocity Field](https://doi.org/10.7910/DVN/BICMWB)  
> GNSS velocities used by Kreemer and Young (2022) to construct the western U.S. geodetic strain-rate model.

> **Methods Paper:** [Strain Accumulation and Rotation in the Eastern California Shear Zone](https://doi.org/10.1029/2000JB000127)  
> Savage et al. (2001), describing the strain and rotation methodology underlying the supplied `calcstrain.m` implementation.
