# GNSS II: From Daily Positions to Deformation Time Series

## Purpose

GNSS processing produces estimates of station position through time. These time series contain tectonic motion together with seasonal variations, abrupt offsets, transient deformation, outliers, and noise.

In this lecture, we will:

- interpret east, north, and vertical position time series
- examine how reference frames affect apparent motion
- decompose a time series into physically meaningful components
- estimate interseismic velocity and coseismic displacement
- recognize seasonal, postseismic, and slow-slip signals
- use residuals to evaluate whether a model adequately represents the data

---

## Learning Objectives

By the end of this lecture, you should be able to:

- explain why a GNSS position or velocity requires a reference frame
- interpret east, north, and vertical displacement components
- identify trends, seasonal signals, offsets, transients, outliers, and noise
- construct a linear time-series decomposition model
- explain how an unmodeled offset or seasonal signal can bias velocity
- estimate the displacement associated with an earthquake
- interpret model residuals and formal uncertainties
- distinguish an abrupt offset from gradual transient deformation

---

## Materials

### Primary lecture material

- *Intro to GNSS*, slides 69–72: global and local reference frames
- *Intro to GNSS*, slides 73–78: time-series products and the need for modeling
- *Intro to GNSS*, slides 79–89: decomposition, trends, seasonal terms, offsets, postseismic deformation, and residuals
- *Intro to GNSS*, slides 90–91: slow slip and the ALBH example

### Laboratory source

- CRESCENT *GNSS Time Series* notebook, §§5–9, streamlined
- *GNSS Time Series Decomposition* notebook, §§2.1–2.4, as an alternative El Mayor case study

---

# What Is a GNSS Position Time Series?

A position time series records repeated estimates of a station's location.

Positions are usually expressed as changes relative to a reference position in three local components:

- east
- north
- up

Each daily estimate also has an uncertainty.

> **Source note:** Intro to GNSS slides 73–76; CRESCENT Time Series §5.

---

# Reference Frames

A position or velocity has meaning only relative to a reference frame.

Possible frames include:

- an Earth-centered global frame such as ITRF
- a tectonic-plate-fixed frame
- a local or regional frame

In a global frame, a station records both rigid plate motion and deformation within the plate.

In a plate-fixed frame, the predicted rigid motion of that plate is removed, emphasizing internal deformation.

> **Source note:** Intro to GNSS slides 69–72.

---

## Absolute and Relative Motion

If neighboring stations have the same velocity, they may be translating together without appreciable internal deformation.

If their velocities differ, the distances or orientations between the stations change.

Crustal deformation is therefore constrained primarily by **spatial variations in velocity**, not by the velocity of one station alone.

---

# Anatomy of a GNSS Time Series

A GNSS time series may contain:

- a long-term interseismic trend
- annual and semiannual signals
- earthquake or equipment offsets
- postseismic deformation
- slow-slip events
- outliers and data gaps
- measurement and processing noise

A useful conceptual model is:

$$
y(t)=\text{trend}+\text{seasonal}+\text{offsets}+\text{transients}+\text{noise}
$$

> **Source note:** Intro to GNSS slides 75–83.

---

# Interseismic Velocity

A constant station velocity produces a linear trend:

$$
y(t)=a+vt
$$

where:

- $a$ is the position at the reference epoch
- $v$ is station velocity

Velocity is the slope of the time series, not simply the difference between its first and last observations.

Short records can produce biased velocities if they contain:

- only part of a seasonal cycle
- an unmodeled earthquake offset
- postseismic deformation
- a few influential outliers

> **Source note:** Intro to GNSS slides 77–84; El Mayor notebook §2.1.

---

# Seasonal Deformation

GNSS stations commonly exhibit annual and semiannual motion caused by:

- hydrologic loading
- snow accumulation and melting
- atmospheric loading
- thermoelastic deformation
- site-specific or processing effects

A common model is:

$$
y_{seasonal}(t)=
A_1\cos(2\pi t)+B_1\sin(2\pi t)
+A_2\cos(4\pi t)+B_2\sin(4\pi t)
$$

The vertical component commonly has the largest seasonal amplitude.

> **Source note:** Intro to GNSS slide 85; CRESCENT Time Series §8; El Mayor notebook §2.4.

---

# Abrupt Offsets

An abrupt position change can be represented using a step function:

$$
y_{step}(t)=D H(t-t_e)
$$

Possible causes include:

- coseismic displacement
- antenna or receiver changes
- monument repair
- processing changes
- station disturbance

An offset is not automatically tectonic. Its timing should be compared with earthquake and station-maintenance records.

> **Source note:** Intro to GNSS slides 86–87; El Mayor notebook §2.2.

---

## Coseismic Displacement

The three-component coseismic displacement vector is:

$$
\mathbf{D}=
\begin{bmatrix}
D_E \\
D_N \\
D_U
\end{bmatrix}
$$

The horizontal displacement magnitude is:

$$
D_H=\sqrt{D_E^2+D_N^2}
$$

The direction and magnitude of this vector vary spatially around the fault and constrain the earthquake slip distribution.

---

# Transient Deformation

Not all deformation is linear or instantaneous.

Transient signals include:

- postseismic deformation
- slow-slip events
- volcanic inflation and deflation
- groundwater withdrawal and recharge

A postseismic transient may be represented with a logarithmic or exponential decay.

For example:

$$
y_{post}(t)=A\log\left(1+\frac{t-t_e}{\tau}\right)
$$

Different mechanisms can produce similar temporal behavior, so the functional form does not uniquely identify the physical process.

> **Source note:** Intro to GNSS slides 88 and 90; El Mayor notebook §2.3.

---

# A Combined Decomposition Model

A basic model used in the CRESCENT notebook is:

$$
y(t)=a+vt+
A_1\cos(2\pi t)+B_1\sin(2\pi t)
+A_2\cos(4\pi t)+B_2\sin(4\pi t)
+\sum_j D_jH(t-t_j)+\epsilon(t)
$$

The model contains:

- reference position
- linear velocity
- annual and semiannual variations
- specified coseismic steps
- residuals

Transient terms can be added when required by the observations.

> **Source note:** Intro to GNSS slides 79–83; CRESCENT Time Series §§6–7.

---

# Residuals and Model Evaluation

Residuals are the differences between observations and predictions:

$$
r_i=y_i-\hat{y}_i
$$

Residuals should be inspected for:

- remaining trends
- unresolved seasonal structure
- undocumented offsets
- transient signals
- changes in variance
- large outliers

A small residual does not guarantee that every model term has a physical interpretation.

> **Source note:** Intro to GNSS slide 89.

---

# GNSS II Summary

GNSS time series contain tectonic and nontectonic signals superimposed on measurement noise.

Time-series decomposition separates long-term velocity, seasonal motion, abrupt offsets, and transient deformation.

Reference-frame choice affects reported position and velocity, while residuals reveal signals not captured by the assumed model.

The fitted velocities from many stations form the velocity field used to estimate tectonic strain.

---

## Laboratory

Students will analyze one real three-component GNSS time series.

Recommended core workflow:

- load and plot the station data
- identify gaps, outliers, seasonal signals, and offsets
- fit a linear trend
- add annual and semiannual terms
- add one known earthquake offset
- compare the inferred velocity between models
- plot and interpret residuals

### Recommended case choice

Use **El Mayor** if the goal is a visually clear progression from interseismic trend to coseismic offset and postseismic deformation.

Use **ALBH** if the goal is to prepare directly for the later Cascadia slow-slip material.

For a 50-minute lab, El Mayor is probably the cleaner teaching case. The CRESCENT notebook's slow-slip detection, multi-station analysis, spectral analysis, and complete network workflow should be reserved for later exercises or instructor demonstrations.
