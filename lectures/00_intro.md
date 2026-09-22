# A Deforming Earth

## Purpose

Earth's crust is never still. In this opening lecture we survey the full landscape of crustal deformation—what deforms, on what timescales, by how much, and with what tools we measure it.

In this lecture, we will:

- recognize the range of processes that deform Earth's crust
- connect deformation to the forces that drive it
- preview the observational methods and modeling approaches used in this course
- place each topic in the context of the 10-week arc ahead

---

# The Restless Crust

## Why Does the Crust Deform?

Earth's outermost layer is broken into tectonic plates that move relative to one another. Wherever plates interact—colliding, separating, or sliding past each other—the crust bends, stretches, shortens, and ruptures.

Deformation is not confined to plate boundaries. Volcanic systems inflate and deflate. Aquifers subside as groundwater is withdrawn. Ice sheets load and unload the lithosphere over glacial cycles. The crust also responds elastically to the weight of ocean tides.

> What do all of these processes have in common?

They produce displacement—measurable changes in position at Earth's surface. This course is about measuring and interpreting those displacements.

```{figure} ../figures/00_tectonic_plates.jpg
---
name: Global Plate Motions
width: 800px
alt: Global map of tectonic plates with arrows showing plate velocities.
---
Global tectonic plate boundaries and velocities. The diversity of plate interactions drives the full range of deformation styles covered in this course.
```

---

## Deformation Occurs Across Many Timescales

One of the central challenges—and pleasures—of geodesy is that the crust deforms on timescales ranging from seconds to millions of years. We use different tools to assess deformation at different timescales.  

| Timescale | Example process | 
|---|---|
| Seconds | Smaller earthquakes |
| Minutes to hours | Larger earthquakes and small slow-slip events |
| Days to weeks | Slow-slip events and postseismic afterslip |
| Months to years | Postseismic viscoelastic relaxation and volcanic unrest |
| Decades to centuries | Interseismic strain accumulation |
| Millennia | Glacial isostatic adjustment |
| Millions of years | Orogenesis, basin subsidence |

Modern geodetic instruments record deformation across many of these timescales simultaneously in a single continuous time series.

---

## Deformation Occurs Across Many Spatial Scales

```{figure} ../figures/00_folds.jpg
---
name: Folds
width: 800px
alt: Photos of centimeter-scale folds.
---
Centimeter-scale folds in a sheeted vein complex on Catalina Island, CA.
```

Spatial scale and temporal scale are coupled: rapid deformation tends to be localized; slow deformation can be broad and diffuse.


```{figure} ../figures/00_tsunami.mp4
---
name: Cascadia tsunami animation
width: 800px
alt: Animation of a Cascadia Subduction Zone tsunami.
---
Vertical seafloor uplift and seafloor normal velocity from a physics-based 3D dynamic rupture and seismic wave propagation computation (Glehman et al., 2025) of a magnitude 8.7 earthquake scenario spanning the full margin of the Cascadia subduction zone from [Henneking et al. (2026)](https://doi.org/10.1145/3712285.37717).
```

---

# The Seismic Cycle

## Faults Store and Release Elastic Strain

Most of Earth's seismicity occurs on faults—surfaces along which rocks slip. Between large earthquakes, tectonic loading accumulates elastic strain in the surrounding crust. When stress exceeds fault strength, that strain is released abruptly as an earthquake.

This cycle of accumulation and release—the **seismic cycle**—is a central organizing theme of the course.

$$
\text{interseismic loading} \longrightarrow \text{co-seismic rupture} \longrightarrow \text{postseismic relaxation} \longrightarrow \text{interseismic loading} \longrightarrow \cdots
$$

Each phase leaves a distinct signature in geodetic observations, and we will learn to read all of them.

```{figure} ../figures/00_seismic_cycle.webp
---
name: Seismic cycle cartoon
width: 800px
alt: Seismic cycle overview.
---
Simplified overview of the seismic cycle.
```

---

# How Do We Measure Crustal Deformation?

## The Geodetic Toolkit

This course uses four primary observational tools. Each measures surface displacement in a different way and is sensitive to different processes.

| Method | What it measures | Typical precision |
|---|---|---|
| **GNSS** | 3-D position of a point through time | mm to cm |
| **Seismology** | Ground motion from seismic waves | depends on magnitude and distance |
| **InSAR** | Range change between satellite and ground | ~cm, spatially dense |
| **LiDAR** | Surface elevation and topographic change from repeated laser surveys | cm to decimeter, depending on platform |
| **Leveling / tiltmeters** | Relative elevation and tilt changes | sub-mm |

No single tool is sufficient for all problems. Understanding what each measures—and what it cannot—is essential for interpreting results and combining datasets.

---

## From Observations to Models

Measurements alone do not explain deformation. We use **forward models** to predict what observations a given physical process should produce, and **inverse models** to infer the properties of that process from observations.

$$
\text{observations} \xrightarrow{\text{inverse}} \text{fault geometry, slip, magma source, \ldots}
$$

$$
\text{fault geometry, slip, \ldots} \xrightarrow{\text{forward}} \text{predicted surface displacement}
$$

In this course, we will build intuition for both directions, starting with the physics and ending with applications to real data.

---

# Course Road Map

## What We Will Cover

```{figure} ../figures/00_integrated_geophysics.png
---
name: Integrated Geophysics
width: 800px
alt: Schematic of geophysical observation techniques and geophysical processes.
---
Schematic of geophysical observation techniques and geophysical processes.
```

| Week | Topic | Dates |
| --- | --- | --- |
| Week 0 | A Deforming Earth | 9/23 |
| Week 1 | GNSS Positioning and Timeseries | 9/28 and 9/30 |
| Week 2 | Strain and the Seismic Cycle | 10/5 and 10/7 |
| Week 3 | Short and Long Timescale Seismology | 10/12 and 10/14 |
| Week 4 | InSAR | 10/19 and 10/21 |
| Week 5 | Forward and Inverse Modeling | 10/26 and 10/28 |
| Week 6 | Midterm and Slip Inversion | 11/2 and 11/4 |
| Week 7 | Mass Movements | 11/9 |
| Week 8 | Volcano Deformation and Magma Migration | 11/16 and 11/18 |
| Week 9 | Groundwater, Fluids, and Subsidence | 11/23 |
| Week 10 | Vertical Land Motion and Synthesis | 11/30 and 12/2 |

---

# A First Look at the Data: The Venezuela Earthquakes, June 2026

```{figure} ../figures/00_venezuela.jpg
---
width: 800px
alt: Ground displacement map derived from NISAR data showing intense deformation near Caracas and La Guaira, Venezuela following the June 24, 2026 earthquakes.
---
Ground displacement near Caracas and La Guaira, Venezuela following earthquakes on June 24, 2026. The map was derived from NISAR (NASA-ISRO Synthetic Aperture Radar) data acquired before and after the earthquakes. NASA Earth Observatory / Lauren Dauphin.
```

This image was made using **InSAR**—one of the tools we will learn in Week 4. 

> What questions does this image raise for you?

Keep them in mind. By mid-semester, you will be able to answer most of them.

---

# Course Summary

- Earth's crust deforms continuously in response to tectonic, volcanic, hydrologic, and atmospheric forcing.
- The seismic cycle—interseismic loading, co-seismic rupture, and postseismic relaxation—organizes much of what we observe.
- GNSS, seismology, InSAR, and related tools each provide a different window onto surface displacement.
- Forward and inverse modeling connect observations to physical parameters.
- This course follows the full chain: raw signals → processed observations → physical models → geophysical interpretation.

> The goal is not just to use these tools. It is to understand them well enough to know when to trust them—and when not to.

---

# Additional Resources

> **Textbook:** Segall, P. (2010). *Earthquake and Volcano Deformation*. Princeton University Press.  
> The primary reference for the modeling sections of this course.

> **Interactive:** [UNAVCO GPS Velocity Viewer](https://www.unavco.org/software/visualization/GPS-Velocity-Viewer/GPS-Velocity-Viewer.html)  
> Explore GNSS velocity fields from around the world. Try viewing different reference frames and notice how the apparent motion changes.
