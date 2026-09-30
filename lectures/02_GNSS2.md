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

# What Is a GNSS Position Time Series?

A position time series records repeated estimates of a station's location.

Positions are usually plotted as changes relative to a reference position in three local components:

- east
- north
- up

Each point is commonly a daily position estimate with a formal uncertainty.

> What features can you identify?

```{figure} ../figures/02_CCCC_timeseries.png
---
name: CCCC Timeseries
width: 600px
alt: Three panel figure with timeseries of the east, north, and vertical positions of GPS station CCCC.
---
East, North, and Vertical position of station CCCC. Each blue dot is an individual estimate of site position, the plot axes are scaled automatically to accommodate the data time span and range of positions (which have been demeaned). Times of nearby earthquakes and known equipment change events are marked with gray and cyan vertical dashed lines, respectively. Information about the earthquake and equipment events are provided in a table below the time series on the station page, with links to the USGS earthquake pages for that event. A “nearby” earthquake is one that is within 10^(M/2 - 0.79) km of the station, where M is the magnitude of the event. This is an approximation of the radius of maximum influence of the event and does not guarantee that a significant offset will appear in the time series at that time, or will not appear for stations at greater distance. 
```

---

## Reference Frames: What Is Held Fixed?

A GNSS velocity describes motion **relative to a chosen reference frame**.

- In a global Earth-centered frame, an entire tectonic plate may appear to move.
- In a plate-fixed frame, the average motion of that plate is removed.
- The remaining velocities make deformation near plate boundaries easier to see.

The station has not physically changed its motion—we have changed what we treat as stationary.

**When interpreting a GNSS velocity map, always check the reference frame.**

```{figure} ../figures/02_rf_comparison.png
---
name: Reference Frame Comparison
width: 760px
alt: Comparison of the same GNSS velocity field in a global IGS20 reference frame and a North America-fixed reference frame.
---
The same GNSS velocities shown in two reference frames. Removing the overall motion of the North American plate emphasizes deformation near its boundaries.
```
---

## Know the Source and Product

Groups including NGL/UNR, EarthScope, JPL, PANGA, and SOPAC distribute GNSS time series. The same observations can yield slightly different positions because providers make different processing, frame, and filtering choices.

| Product | Appropriate use |
|---|---|
| Position solution, with trend and geophysical signals retained | Fit your own deformation model |
| Detrended or cleaned, with specified terms removed | Inspect residual or transient behavior |
| Plate-fixed, with predicted rigid plate motion removed | Examine deformation within a plate |

Do not remove a signal twice. Record the **provider, product, frame, processing version, and access date**.

```{figure} ../figures/02_product_levels.png
---
name: CCCC Comparison
width: 800px
alt: GNSS station CCCC shown as a position solution and "cleaned and detrended".
---
Comparison of two different CCCC solutions: raw and "cleaned and detrended".
```

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

## Superposition

The observed position is the sum of signals occurring at the same time:

$$
y(t)=\sum_{k=1}^{n}x_k(t)+\epsilon(t)
$$

We represent the combined effect of different processes with simple model terms.

This is powerful—but the fitted terms are only physically meaningful if the model is appropriate and the terms can be distinguished by the data.

---

## Interseismic Velocity

A constant station velocity produces a linear trend:

$$
y(t)=a+vt
$$

where $a$ is position at the reference epoch and $v$ is station velocity. In practice, time is centered on the mean epoch so that the estimated offset $a$ refers to the midpoint of the record rather than year zero, which reduces numerical covariance between $a$ and $v$.

Velocity is the slope of all relevant observations, not simply the difference between the first and last positions.

Velocities are typically reported in mm/yr; tectonic rates range from a few mm/yr in stable interiors to tens of mm/yr near active plate boundaries. 

Short records can be biased by partial seasonal cycles, offsets, transients, or influential outliers.

---

## Why Omitted Signals Bias Velocity

Suppose the true time series contains a trend and an offset:

$$
y(t)=a+vt+D H(t-t_e)+\epsilon(t)
$$

If we fit only a straight line, part of the step is absorbed into the slope.

Similarly, a record spanning a noninteger number of seasonal cycles can mistake part of an annual oscillation for long-term motion.

> **Prediction:** How would a positive offset near the middle of a record affect a line fit across the whole record?

A positive offset near the middle inflates the slope before the step and deflates it after; fitting a single line across the full record biases the velocity upward.

---

## Seasonal Deformation

GNSS stations commonly exhibit annual and semiannual motion caused by:

- hydrologic and snow loading
- atmospheric and nontidal ocean loading
- thermoelastic deformation
- site-specific or processing effects

A common model is, with $t$ measured in years:

$$
y_{seasonal}(t)=A_1\cos(2\pi t)+B_1\sin(2\pi t)
+A_2\cos(4\pi t)+B_2\sin(4\pi t)
$$

The vertical component commonly has the largest seasonal amplitude.

```{figure} ../figures/02_CCCC.png
---
name: CCCC
width: 820px
alt: GNSS position time series with trend, seasonal oscillation, coseismic step, postseismic decay, outliers, and data gaps.
---
CCCC time series that shows clear seasonal deformation.
```

---

## Abrupt Offsets

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

```{figure} ../figures/02_abrupt_offsets.png
---
name: Abrupt offsets
width: 820px
alt: GNSS position time series with trend, seasonal oscillation, coseismic step, postseismic decay, outliers, and data gaps.
---
GPS station coordinate time series of the station G016 for the east, north and up component. The vertical dashed lines mark potential earthquake discontinuities from the NGL discontinuity database. Light red lines mark discontinuities causing a station coordinate displacement smaller than ten millimeters in one of the components, while dark red lines mark discontinuities causing a station coordinate displacement equal to or larger than ten millimeters in one of the components. From [Crocetti et al. 2021](https://doi.org/10.3390/rs13193906).
```

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

The direction and magnitude of displacement vary across the network and constrain the earthquake slip distribution.  A simple practical estimate compares mean positions in short windows immediately before and after the event; the result depends on window length and on any remaining model misfit.

```{figure} ../figures/02_coseismic.png
---
name: Coseismic displacements from Japanese earthquake
width: 780px
alt: Map of horizontal GNSS coseismic displacement vectors surrounding an earthquake in Japan.
---
On January 13, 2025 an M6.8 earthquake struck off the southeast shore of Japan. The epicenter was very near another large earthquake (M 7.1) that occurred in April 2024. The January event could be seen as an aftershock since it occurred after, and was substantially smaller than, the April event. However, since it was not much smaller in magnitude than the April event, it could be seen as the second of a doublet, which ruptured the same segment of the plate boundary between the Philippine Sea and Eurasian tectonic plates. The largest displacement was a little over 5 cm at continuously recording station J095.
```

---

## Transient Deformation

Not all deformation is linear or instantaneous.

Transient signals include:

- postseismic deformation
- slow-slip events
- volcanic inflation and deflation
- groundwater withdrawal and recharge

Different physical mechanisms can produce similar temporal behavior. A fitted functional form does not uniquely identify the mechanism.

```{figure} ../figures/02_transient_deformation.jpg
---
name: Volcano Deformation
width: 800px
alt: Idealized step, ramp, exponential recovery, and inflation-deflation signals arranged by characteristic duration.
---
(a) Maps of Etna volcano with the Global Navigation Satellite System (GNSS) (red circles) and tilt (yellow squares) permanent networks; the blue triangle highlights the area whose variation is shown in Figure (c), while the black circle indicates the ECP tilt station. VdB indicates the Valle del Bove area. The inset at the left bottom shows the location of Mt. Etna in southern Italy; (b) Tilt recorded on the N14°E component of ECP station during the fountain sequence tilt series: F1-F15 shows changes associated with the first 15 fountains also characterized by a general lowering trend ending with the last two episodes (F16 and F17). The inset at the left bottom shows the summit crater of Mt. Etna (De Beni et al., 2015). SEC, South East Crater; NSEC, New SEC; (c) Daily variation of the area recorded at an intermediate altitude triangle (EDAM-EMEG-EINT) indicated by the blue triangle in Figure (a). Positive variations indicate inflations, while negative variations are measured during deflations of the volcanic edifice, due to volcanic activity; (d) N-S daily components of the EINT and EDAM GNSS stations (blue and gray circles, respectively), on the southern and northern flanks of Mt. Etna, respectively. E-W daily component of the EMEG station (red circles), located on the western flank. Red rectangles indicate short and episodic interruptions of the inflation due to summit eruptive activity. The orange rectangles highlight the deflation produced by the 17 lava fountains. The vertical black lines indicate the start of each phase characterized by a different ground deformation pattern, recognized on the basis of the changes in the slope of the time series. Black arrows indicate inflation, while the red arrow indicates the deflation of volcanic edifice. From [Bruno et al. 2022](https://doi.org/10.1029/2021GL095195)
```

---

## Postseismic Deformation

Common empirical representations include logarithmic and exponential decay.  Velocity-strengthening afterslip follows a logarithmic decay

$$
y_{log}(t)=c+a\ln\left(1+\frac{t}{\tau}\right).
$$

While postseismic relaxation follows an exponential decay

$$
y_{exp}(t)=c+a\left[1-\exp\left(-\frac{t}{\tau}\right)\right].
$$

The decay time $\tau$ is nonlinear. One approach is to test a range of $\tau$ values, solve for the remaining coefficients at each value, and select the model with the best justified fit.

```{figure} ../figures/02_postseismic.png
---
name: Postseismic
width: 780px
alt: Logarithmic and exponential postseismic displacement curves for several decay times.
---
Postseismic time-series for the 18 analyzed stations. Note that the time-series are vertically displaced (see Table 1 for coseismic offset values). Solid and dashed lines are best-fit logarithmic and exponential functions, respectively (The relaxation predictions are not shown for newly installed stations BSIM, LEWK, LHWA, and UMLH, because the additional constant velocity that is solved for those stations differs between the two models and changes the appearance of the time-series.): (a) east direction, (b) north direction, and (c) up direction. [Kreemer et al. 2006](https://doi.org/10.1029/2005GL025566)
```

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

For fixed event times and fixed decay times, coefficients are estimated by weighted least squares, with each observation weighted by $1/\sigma_i$, so that noisier epochs contribute less to the fit.

---

## Build the Model Incrementally

1. Plot all three components and inspect metadata.
2. Fit a trend and examine residuals.
3. Add justified annual and semiannual terms.
4. Add documented offsets.
5. Add transient terms only when supported by the observations.
6. Compare parameter estimates and residual structure between models.

The goal is not the most complicated model. It is the simplest model that captures the signals relevant to the question.

---

## Residuals and Model Evaluation

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

## Network-Common Signals

Not every coherent signal is tectonic. Reference-frame errors, orbit or clock errors, and broad environmental loading can appear at many stations simultaneously.

Comparing neighboring stations helps distinguish:

- local monument or equipment problems
- regional deformation
- network-wide common-mode error

Regional filtering can reduce common-mode noise, but it can also remove spatially broad deformation if applied without care.

```{figure} ../figures/02_common_mode.png
---
name: Common mode
width: 820px
alt: Several nearby GNSS time series sharing one coherent fluctuation while one station also contains a local offset.
---
Example of common mode noise shared across the network and the application of stack filtering to remove it.
```

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

Between events, stations resume their inter-ETS motion. The slope between slow slip events can differ from the long-term slope because repeated slow slip contributes to the full time series.

```{figure} ../figures/02_ALBH.png
---
name: SSEs in ALBH
width: 820px
alt: Raw and detrended east-component GNSS position time series for station ALBH, with slow-slip events visible as temporary reversals.
---
Raw and detrended east-component GNSS position time series for station ALBH, with slow-slip events visible as temporary reversals.
```

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

# Laboratory

Students will analyze ALBH using the CRESCENT GNSS time-series dataset:

- inspect the raw east, north, and up positions
- compare trend-only and trend-plus-seasonal models
- determine how model choice changes velocity and residuals
- isolate the 2015–2016 Cascadia slow-slip event
- estimate its three-component displacement
- test whether the transient is coherent at nearby stations

For a 50-minute lab, automated transient detection, postseismic grid searches, Euler-pole estimation, block rotations, and spectral-noise analysis are intentionally omitted. They can become later or optional exercises.

```

---

# Additional Resources

> **GNSS Data:** [Nevada Geodetic Laboratory GPS Network Map](https://geodesy.unr.edu/NGLStationPages/gpsnetmap/GPSNetMap.html)  
> Explore GNSS station locations, position time series, and velocities from the Nevada Geodetic Laboratory.

> **Regional GNSS Data:** [Pacific Northwest Geodetic Array (PANGA)](https://www.panga.org/)  
> Access GNSS station information, position time series, velocity fields, and other geodetic products for Cascadia and the Pacific Northwest.