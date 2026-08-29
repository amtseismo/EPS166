# GNSS III: From Station Velocities to Tectonic Strain

## Purpose

Individual GNSS stations measure motion at particular locations. Tectonic deformation is revealed by how velocity changes across a network.

In this lecture, we will:

- construct and interpret horizontal velocity vectors
- compare global and plate-fixed velocity fields
- distinguish translation and rotation from internal deformation
- identify extension, contraction, and shear
- introduce the velocity-gradient and strain-rate tensors
- interpret principal strain rates and strain ellipses
- compare strain in convergent, extensional, and strike-slip environments

---

## Learning Objectives

By the end of this lecture, you should be able to:

- calculate horizontal speed and direction from east and north velocity components
- explain how reference-frame choice affects a velocity map
- distinguish rigid translation and rotation from strain
- qualitatively identify extension, contraction, and shear from a velocity field
- explain how spatial velocity gradients describe deformation
- distinguish the symmetric strain-rate tensor from rigid rotation
- interpret principal strain axes, dilation, maximum shear, and a strain ellipse
- identify limitations of estimating uniform strain from a three-station triangle

---

## Materials

### Primary lecture material

- GETSI Unit 3: velocity components, reference frames, and qualitative interpretation
- GETSI Unit 4: infinitesimal strain, station triangles, principal strains, and strain ellipses
- *Intro to GNSS*, slides 69–72: reference-frame review
- CRESCENT *GNSS Time Series* notebook, §§15b–15c: network velocities and ITRF-to-North-America-fixed transformation

### Laboratory source

- Adapted GETSI Unit 4
- Three-station velocity triangles
- GETSI strain calculator or a Python equivalent

---

# From Time-Series Slopes to Velocity Vectors

For each station, the fitted horizontal trends provide:

$$
v_E=\frac{dE}{dt}
$$

$$
v_N=\frac{dN}{dt}
$$

Together they form a horizontal velocity vector:

$$
\mathbf{v}=
\begin{bmatrix}
v_E \\
v_N
\end{bmatrix}
$$

The horizontal speed is:

$$
|\mathbf{v}|=\sqrt{v_E^2+v_N^2}
$$

A velocity arrow shows:

- direction through its orientation
- speed through its length
- uncertainty through an error ellipse

> **Source note:** GETSI Unit 3; CRESCENT Time Series §15b.

---

# Velocity Fields and Reference Frames

An ITRF velocity field includes the absolute motion of the tectonic plate.

A plate-fixed velocity is obtained by subtracting the velocity predicted for rigid plate rotation:

$$
\mathbf{v}_{fixed}=\mathbf{v}_{ITRF}-\mathbf{v}_{plate}
$$

This changes the apparent translation of the network but should not change its internal deformation.

> **Source note:** Intro to GNSS slides 69–72; CRESCENT Time Series §15c. The Euler-pole equations are useful as an optional derivation rather than a required calculation.

---

# Translation, Rotation, and Strain

Motion within a small region can be separated into:

- translation
- rigid-body rotation
- strain

Translation and rotation move a region without changing its shape.

Strain changes distances, angles, shape, or area.

---

## Translation

If all stations have the same velocity, the network translates without internal deformation.

The station triangle changes position but retains its size and shape.

---

## Rigid Rotation

During rigid rotation:

- velocity varies with position
- the network changes orientation
- distances and angles within the network remain unchanged

Rotation is therefore not the same as strain.

---

## Extension and Contraction

In one dimension, strain rate is the spatial gradient of velocity:

$$
\dot{\epsilon}_{xx}=\frac{\partial v_x}{\partial x}
$$

If neighboring points move apart, the region extends.

If neighboring points move together, the region contracts.

Strain rate has units of inverse time and is commonly reported as nanostrain per year.

---

## Shear

Shear changes angles within a region.

In a velocity field, shear may appear as:

- opposite motion across a strike-slip fault
- parallel motion at different speeds
- systematic variation in velocity direction across a zone

---

# The Velocity-Gradient Tensor

For a two-dimensional velocity field:

$$
\mathbf{L}=
\begin{bmatrix}
\frac{\partial v_x}{\partial x} & \frac{\partial v_x}{\partial y} \\
\frac{\partial v_y}{\partial x} & \frac{\partial v_y}{\partial y}
\end{bmatrix}
$$

The velocity gradient can be divided into symmetric and antisymmetric components:

$$
\mathbf{L}=\dot{\boldsymbol{\epsilon}}+\mathbf{W}
$$

where:

$$
\dot{\boldsymbol{\epsilon}}=
\frac{1}{2}(\mathbf{L}+\mathbf{L}^T)
$$

describes strain rate, and

$$
\mathbf{W}=
\frac{1}{2}(\mathbf{L}-\mathbf{L}^T)
$$

describes rigid rotation.

The main conceptual point is that only the symmetric component changes shape or area.

---

# Principal Strain Rates

The horizontal strain-rate tensor is:

$$
\dot{\boldsymbol{\epsilon}}=
\begin{bmatrix}
\dot{\epsilon}_{xx} & \dot{\epsilon}_{xy} \\
\dot{\epsilon}_{xy} & \dot{\epsilon}_{yy}
\end{bmatrix}
$$

Its eigenvectors give the principal strain directions, and its eigenvalues give the principal strain rates:

- $\dot{\epsilon}_1$: maximum principal strain rate
- $\dot{\epsilon}_2$: minimum principal strain rate

Positive values commonly represent extension and negative values contraction, but the calculator's sign convention must be checked.

---

## Dilation

Dilation is the rate of area change:

$$
\dot{\Delta}=\dot{\epsilon}_{xx}+\dot{\epsilon}_{yy}
=\dot{\epsilon}_1+\dot{\epsilon}_2
$$

Positive dilation indicates increasing area; negative dilation indicates decreasing area.

---

## Maximum Shear

Maximum shear is related to the difference between the principal strain rates:

$$
\dot{\gamma}_{max}=\dot{\epsilon}_1-\dot{\epsilon}_2
$$

A region can have strong shear even when its total area changes very little.

---

# Strain Ellipses

Imagine a circle embedded in the crust before deformation.

After deformation, the circle becomes an ellipse.

The ellipse shows:

- the direction of maximum extension
- the direction of maximum contraction
- the relative magnitudes of the principal strains

The strain ellipse represents internal deformation but not translation.

> **Source note:** GETSI Unit 4.

---

# Estimating Strain from Three Stations

Three non-collinear stations define a triangle.

A two-dimensional linear velocity field contains six unknowns:

- two translation terms
- four velocity-gradient terms

Three stations provide six horizontal velocity observations:

- three east velocities
- three north velocities

The observations are therefore sufficient to solve for a uniform velocity gradient across the triangle.

---

## Assumptions and Limitations

The three-station method assumes:

- velocities vary linearly across the triangle
- strain is uniform within the triangle
- station velocities and coordinates are accurate
- the triangle does not span unrelated deformation regimes

The result is an average over the triangle and depends on:

- station spacing
- triangle geometry
- velocity uncertainty
- spatial complexity of the actual deformation

> **Source note:** GETSI Unit 4.

---

# Tectonic Examples

## Cascadia Convergence

Expected pattern:

- margin-normal contraction
- landward motion of the overriding plate near the coast
- decreasing velocity toward the continental interior
- elastic strain accumulation above the locked megathrust

---

## Basin and Range Extension

Expected pattern:

- stations moving apart
- positive dilation
- principal extension approximately perpendicular to normal faults
- broadly distributed deformation

---

## San Andreas Strike-Slip Deformation

Expected pattern:

- velocity primarily parallel to the plate boundary
- velocity gradient across the fault system
- large maximum shear
- relatively limited net area change

> **Source note:** GETSI Unit 4 tectonic cases.

---

# GNSS III Summary

A velocity field combines measurements from many GNSS stations.

Shared station motion may represent translation, while spatial differences in motion describe rotation and strain.

The symmetric velocity gradient defines strain rate; the antisymmetric component describes rigid rotation.

Principal strain rates, dilation, maximum shear, and strain ellipses summarize the style and orientation of deformation.

Three-station triangles provide a simple estimate of average strain and allow comparisons among convergent, extensional, and strike-slip environments.

---

## Laboratory

Use an adapted version of GETSI Unit 4.

### 50-minute structure

- **0–8 minutes:** instructor demonstrates one simple velocity triangle and the strain-calculator output
- **8–15 minutes:** groups inspect the station locations and velocity vectors for their assigned region
- **15–27 minutes:** groups enter coordinates and velocities and calculate strain
- **27–37 minutes:** groups interpret translation, rotation, principal strains, dilation, shear, and the strain ellipse
- **37–45 minutes:** groups compare Cascadia, Basin and Range, and San Andreas results
- **45–50 minutes:** whole-class synthesis connecting strain patterns to faults and expected earthquake behavior

Each group should complete one tectonic case rather than all three.

The CRESCENT network-velocity and North-America-fixed maps from §§15b–15c can be shown at the start of the lab to connect the triangle exercise to a modern regional velocity field.
