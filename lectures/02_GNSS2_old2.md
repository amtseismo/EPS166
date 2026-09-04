# GNSS II: From Daily Positions to Deformation Time Series

<!--
LECTURE COMPLETION NOTES (not rendered as slides)

Added from Intro to GNSS, slides 69-91:
- a distinction between coordinate representations, datums, and kinematic reference frames
- time-series providers and the importance of processing choices
- raw/minimally corrected versus modeled products
- explicit superposition and model-fitting concepts
- Euler-pole removal for plate-fixed velocities
- a dedicated slow-slip/ALBH sequence

Content that was missing from both the draft and the source PDF, but is needed to
fully support the stated learning objectives:
- why omitted seasonal terms and offsets bias an estimated velocity
- the distinction between formal daily-position uncertainties and realistic
  velocity uncertainties when residuals are temporally correlated
- a concrete workflow for reading and evaluating a three-component time series

Intentionally omitted from the source PDF:
- detailed geoid and WGS84 dimensions, which fit better in GNSS I or a coordinate
  systems lecture than in a lecture on deformation time series
- pole-tide equations and the detailed seasonal-error table, because standard
  products already apply these geophysical corrections and the equations do not
  advance this lecture's learning objectives
- PCA-based postseismic estimation, which is too specialized for this lecture
- slides 92-99 on the second notebook and CRESCENT transient-catalog workshop,
  which are workshop logistics rather than lecture content

Remaining instructor need:
- Add screenshots or plots from the UNR station pages for the provider/product
  comparison and from ALBH for the slow-slip sequence. The source PDF figures can
  guide selection, but they should not be copied without confirming reuse rights.
-->

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

# What Is a GNSS Position Time Series?

A position time series records repeated estimates of a station's location.

Positions are usually plotted as changes relative to a reference position in three local components:

- east
- north
- up

Each point is commonly a daily position estimate with a formal uncertainty.

> **Ask:** What features can you identify before fitting a model?

---

# Three Different Ideas

These terms are related, but they are not interchangeable:

| Concept | What it defines | Example |
|---|---|---|
| Ellipsoid | A mathematical approximation to Earth's shape | WGS84 ellipsoid |
| Datum / coordinate system | How locations are represented on that surface | NAD83; latitude, longitude, height |
| Reference frame | The realized origin, orientation, scale, and their evolution through time | ITRF2020; stable North America |

For deformation, the critical question is: **relative to what frame is the station moving?**

---

# Reference Frames

A position or velocity has meaning only relative to a reference frame.

Possible frames include:

- an Earth-centered global frame such as ITRF
- a tectonic-plate-fixed frame
- a local or regional frame

In a global frame, a station records both rigid plate motion and deformation within the plate.

In a plate-fixed frame, predicted rigid plate motion is removed, emphasizing internal deformation.

---

## From Global to Plate-Fixed Velocity

Rigid plate motion predicted by an Euler pole is

$$
\mathbf{v}_{plate}=\boldsymbol{\omega}\times\mathbf{r}
$$

where $\boldsymbol{\omega}$ is the plate's angular velocity and $\mathbf{r}$ is the station position vector.

The plate-fixed residual velocity is

$$
\mathbf{v}_{relative}=\mathbf{v}_{ITRF}-\mathbf{v}_{plate}
$$

The observations have not changed—only the frame used to describe them has.

---

## Absolute and Relative Motion

If neighboring stations have the same velocity, they may be translating together without appreciable internal deformation.

If their velocities differ, the distances or orientations between the stations change.

Crustal deformation is therefore constrained primarily by **spatial variations in velocity**, not by the velocity of one station alone.

> **Think-pair-share:** Which velocity field—ITRF or plate-fixed—would make deformation within Cascadia easiest to see?

---

# Where Do Time Series Come From?

Common processing packages include GAMIT/GLOBK, GipsyX, Bernese, and PRIDE PPP-AR.

Public products are distributed by groups such as:

- Nevada Geodetic Laboratory (NGL/UNR)
- EarthScope
- JPL
- PANGA
- SOPAC

Different providers can process the same observations and obtain slightly different positions because they use different models, reference-frame realizations, ambiguity-resolution methods, and filtering choices.

> **Practical rule:** Record the provider, product, frame, processing version, and access date.

---

# Know Which Product You Downloaded

A provider may distribute several versions of the same station time series.

| Product | May include | Appropriate use |
|---|---|---|
| Minimally modeled | Standard tidal/loading corrections and known equipment offsets | Fit your own physical model |
| Detrended or cleaned | Trend, offsets, outliers, or common-mode signal removed | Inspect residual or transient behavior |
| Plate-fixed | Predicted rigid plate motion removed | Examine deformation within a plate |

Do not remove a signal twice. Read the product documentation before interpreting the result.

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

---

# Superposition

The observed position is the sum of signals occurring at the same time:

$$
y(t)=\sum_{k=1}^{n}x_k(t)+\epsilon(t)
$$

Decomposition does not mean that the processes occurred separately. It means that we represent their combined effect with simpler model terms.

This is powerful—but the fitted terms are only physically meaningful if the model is appropriate and the terms can be distinguished by the data.

---

# Interseismic Velocity

A constant station velocity produces a linear trend:

$$
y(t)=a+vt
$$

where $a$ is position at the reference epoch and $v$ is station velocity.

Velocity is the slope of all relevant observations, not simply the difference between the first and last positions.

Short records can be biased by partial seasonal cycles, offsets, transients, or influential outliers.

---

# Why Omitted Signals Bias Velocity

Suppose the true time series contains a trend and an offset:

$$
y(t)=a+vt+D H(t-t_e)+\epsilon(t)
$$

If we fit only a straight line, part of the step is absorbed into the slope.

Similarly, a record spanning a noninteger number of seasonal cycles can mistake part of an annual oscillation for long-term motion.

> **Prediction:** How would a positive offset near the middle of a record affect a line fit across the whole record?

---

# Seasonal Deformation

GNSS stations commonly exhibit annual and semiannual motion caused by:

- hydrologic and snow loading
- atmospheric and nontidal ocean loading
- thermoelastic deformation
- site-specific or processing effects

A common model is:

$$
y_{seasonal}(t)=A_1\cos(2\pi t)+B_1\sin(2\pi t)
+A_2\cos(4\pi t)+B_2\sin(4\pi t)
$$

The vertical component commonly has the largest seasonal amplitude.

---

# Abrupt Offsets

An abrupt position change can be represented using a Heaviside step function:

$$
y_{step}(t)=D H(t-t_e)
$$

Possible causes include:

- coseismic displacement
- antenna or receiver changes
- monument repair or disturbance
- processing changes

An offset is not automatically tectonic. Compare its timing with earthquake catalogs and station-maintenance records.

---

## Coseismic Displacement

The three-component coseismic displacement vector is

$$
\mathbf{D}=\begin{bmatrix}D_E \\ D_N \\ D_U\end{bmatrix}
$$

and the horizontal magnitude is

$$
D_H=\sqrt{D_E^2+D_N^2}
$$

The direction and magnitude of displacement vary across the network and constrain the earthquake slip distribution.

---

# Transient Deformation

Not all deformation is linear or instantaneous.

Transient signals include:

- postseismic deformation
- slow-slip events
- volcanic inflation and deflation
- groundwater withdrawal and recharge

Different physical mechanisms can produce similar temporal behavior. A fitted functional form does not uniquely identify the mechanism.

---

# Postseismic Deformation

Common empirical representations include logarithmic and exponential decay:

$$
y_{log}(t)=A\log\left(1+\frac{t-t_e}{\tau}\right)
$$

$$
y_{exp}(t)=A\left[1-\exp\left(-\frac{t-t_e}{\tau}\right)\right]
$$

The decay time $\tau$ is nonlinear. One approach is to test a range of $\tau$ values, solve for the remaining coefficients at each value, and select the model with the best justified fit.

---

# A Combined Decomposition Model

$$
\begin{aligned}
y(t)=\;&a+vt \\
&+A_1\cos(2\pi t)+B_1\sin(2\pi t) \\
&+A_2\cos(4\pi t)+B_2\sin(4\pi t) \\
&+\sum_j D_jH(t-t_j)+T(t)+\epsilon(t)
\end{aligned}
$$

The model contains a reference position, velocity, seasonal variations, specified steps, optional transient terms $T(t)$, and residuals.

For fixed event times and fixed decay times, most coefficients can be estimated together by linear least squares.

---

# Build the Model Incrementally

1. Plot all three components and inspect metadata.
2. Fit a trend and examine residuals.
3. Add justified annual and semiannual terms.
4. Add documented offsets.
5. Add transient terms only when supported by the observations.
6. Compare parameter estimates and residual structure between models.

The goal is not the most complicated model. It is the simplest model that captures the signals relevant to the question.

---

# Residuals and Model Evaluation

Residuals are the differences between observations and predictions:

$$
r_i=y_i-\hat{y}_i
$$

Inspect residuals for:

- remaining trends or seasonal structure
- undocumented offsets or transients
- changes in variance
- large outliers and data gaps

Small residuals do not guarantee that every fitted term has a physical interpretation.

---

# Uncertainty Is More Than Error Bars

Daily formal uncertainties describe precision under the assumptions of the position solution.

GNSS residuals are commonly correlated through time because of monument motion, environmental effects, reference-frame errors, and processing artifacts.

If a velocity fit assumes independent residuals when the noise is correlated, its uncertainty is usually too small.

> **Key distinction:** A good fit describes the observations; a realistic uncertainty describes how confidently we know the parameters.

---

# Slow-Slip Events

In Cascadia, slow-slip events were recognized when GNSS stations showed temporary reversals of their long-term motion at the same time as tectonic tremor.

In a detrended time series, a slow-slip event appears as displacement accumulated over days to weeks rather than an instantaneous step.

Between events, stations resume their inter-ETS motion. The inter-ETS slope can differ from the long-term slope because repeated slow slip contributes to the full time series.

---

# Example: ALBH in Cascadia

Use the raw and detrended east-component time series for station ALBH.

Ask students to identify:

1. the long-term interseismic trend in the raw series
2. why the transients are difficult to see before detrending
3. the direction and duration of individual reversals
4. the approximately steady inter-ETS segments
5. variation in displacement among slow-slip events

> **Instructor figure needed:** Raw and detrended ALBH east-component time series, following Intro to GNSS slide 91.

---

# Abrupt Offset or Gradual Transient?

| Feature | Abrupt offset | Gradual transient |
|---|---|---|
| Timescale | One epoch or data gap | Days to years |
| Time-series shape | Step | Ramp or curved evolution |
| Examples | Earthquake; antenna change | Slow slip; postseismic deformation |
| Useful evidence | Event and maintenance records | Coherent evolution at nearby stations |

Sampling gaps can make a gradual transient appear abrupt, so interpretation should use station metadata and the surrounding network.

---

# GNSS II Summary

- A position or velocity is meaningful only in a specified reference frame.
- GNSS time series superimpose long-term motion, seasonal signals, offsets, transients, and noise.
- Unmodeled signals can bias velocity and displacement estimates.
- Residuals test model adequacy; correlated noise affects parameter uncertainty.
- Slow slip is most visible after long-term and seasonal signals are removed.
- Velocities from many stations form the field used to estimate tectonic strain.

---

## Laboratory

Students will analyze one real three-component GNSS time series:

- load and plot the station data
- identify gaps, outliers, seasonal signals, and offsets
- fit a linear trend
- add annual and semiannual terms
- add one known earthquake offset
- compare the inferred velocity between models
- plot and interpret residuals

Use **El Mayor** for a clear progression from interseismic trend to coseismic offset and postseismic deformation. Use **ALBH** to prepare directly for Cascadia slow-slip material.

For a 50-minute lab, El Mayor is the cleaner teaching case. Reserve multi-station slow-slip detection, spectral analysis, and network-wide processing for later exercises.
