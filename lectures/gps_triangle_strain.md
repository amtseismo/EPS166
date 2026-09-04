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

# Source

> **Teaching material:** EarthScope/GETSI, *Using Velocities From a Triangle of GPS Sites to Investigate Crustal Strain*, EarthScope GPS Crustal Strain Curriculum Team. Original presentation version dated September 9, 2012; contact information updated by EarthScope.

