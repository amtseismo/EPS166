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
width: 600px
alt: Three panel figure with timeseries of the east, north, and vertical positions of GPS station CCCC.
---
East, North, and Vertical position of station CCCC.  Time series plots are provided for 24 hour and 5 minute sample rate solutions. Each blue dot is an individual estimate of site position, the plot axes are scaled automatically to accommodate the data time span and range of positions (which have been demeaned). Times of nearby earthquakes and known equipment change events are marked with gray and cyan vertical dashed lines, respectively. Information about the earthquake and equipment events are provided in a table below the time series on the station page, with links to the USGS earthquake pages for that event. A “nearby” earthquake is one that is within 10^(M/2 - 0.79) km of the station, where M is the magnitude of the event. This is an approximation of the radius of maximum influence of the event and does not guarantee that a significant offset will appear in the time series at that time, or will not appear for stations at greater distance. 
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

```{figure} ../figures/03_time_series_anatomy.png
---
width: 820px
alt: Synthetic GNSS position time series with trend, seasonal oscillation, coseismic step, postseismic decay, outlier, and data gap labeled.
---
Recommended visual: an annotated synthetic time series that introduces every component used later in the lecture. Keep the same colors for these components on subsequent slides.
```

---

## Superposition

The observed position is the sum of signals occurring at the same time:

$$
y(t)=\sum_{k=1}^{n}x_k(t)+\epsilon(t)
$$

Decomposition does not mean that the processes occurred separately. It means that we represent their combined effect with simpler model terms.

This is powerful—but the fitted terms are only physically meaningful if the model is appropriate and the terms can be distinguished by the data.

---

## Interseismic Velocity

A constant station velocity produces a linear trend:

$$
y(t)=a+vt
$$

where $a$ is position at the reference epoch and $v$ is station velocity.

Velocity is the slope of all relevant observations, not simply the difference between the first and last positions.

Short records can be biased by partial seasonal cycles, offsets, transients, or influential outliers.

```{figure} ../figures/03_velocity_slope.png
---
width: 760px
alt: GNSS position observations with a fitted linear trend whose slope is the station velocity.
---
Recommended visual: a single component with observations, fitted line, and a slope triangle labeled in mm/yr.
```

---

## Why Omitted Signals Bias Velocity

Suppose the true time series contains a trend and an offset:

$$
y(t)=a+vt+D H(t-t_e)+\epsilon(t)
$$

If we fit only a straight line, part of the step is absorbed into the slope.

Similarly, a record spanning a noninteger number of seasonal cycles can mistake part of an annual oscillation for long-term motion.

> **Prediction:** How would a positive offset near the middle of a record affect a line fit across the whole record?

```{figure} ../figures/03_omitted_offset_bias.png
---
width: 800px
alt: A stepped time series fit once with a straight line and once with a trend plus offset, producing different velocity estimates.
---
Recommended visual: side-by-side fits to the same synthetic data—line only versus line plus step—with the estimated velocities printed on the plots.
```

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

```{figure} ../figures/03_three_component_seasonality.png
---
width: 800px
alt: East north and up GNSS components showing annual and semiannual variations, with the larger vertical amplitude emphasized.
---
Recommended visual: three aligned components from a station with a clear seasonal signal. Plot at least two full years and use the same time axis.
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

```{figure} ../figures/03_tectonic_vs_equipment_offsets.png
---
width: 800px
alt: GNSS time series offsets annotated with an earthquake time and an antenna replacement time.
---
Recommended visual: two real or idealized offsets with vertical event markers—one earthquake and one equipment change—to demonstrate that shape alone does not identify cause.
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

The direction and magnitude of displacement vary across the network and constrain the earthquake slip distribution.

```{figure} ../figures/02_coseismic.png
---
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

```{figure} ../figures/03_transient_timescales.png
---
width: 800px
alt: Idealized step, ramp, exponential recovery, and inflation-deflation signals arranged by characteristic duration.
---
Recommended visual: idealized transient shapes on a shared time axis. Label the timescale and possible processes, while noting that the mapping is not unique.
```

---

## Postseismic Deformation

Common empirical representations include logarithmic and exponential decay:

$$
y_{log}(t)=A\log\left(1+\frac{t-t_e}{\tau}\right)H(t-t_e)
$$

$$
y_{exp}(t)=A\left[1-\exp\left(-\frac{t-t_e}{\tau}\right)\right]H(t-t_e)
$$

The decay time $\tau$ is nonlinear. One approach is to test a range of $\tau$ values, solve for the remaining coefficients at each value, and select the model with the best justified fit.

```{figure} ../figures/03_postseismic_decay_models.png
---
width: 780px
alt: Logarithmic and exponential postseismic displacement curves for several decay times.
---
Recommended visual: compare logarithmic and exponential functions, including how changing $\tau$ changes curvature. Avoid implying that curve shape alone identifies the underlying mechanism.
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

For fixed event times and fixed decay times, most coefficients can be estimated together by linear least squares.

```{figure} ../figures/03_combined_model_fit.png
---
width: 820px
alt: GNSS time series with the combined model overlaid and individual trend seasonal offset and transient contributions shown below.
---
Recommended visual: one complete fit above and the estimated contribution of each model term below. Use the same component colors introduced on the anatomy slide.
```

---

## Build the Model Incrementally

1. Plot all three components and inspect metadata.
2. Fit a trend and examine residuals.
3. Add justified annual and semiannual terms.
4. Add documented offsets.
5. Add transient terms only when supported by the observations.
6. Compare parameter estimates and residual structure between models.

The goal is not the most complicated model. It is the simplest model that captures the signals relevant to the question.

```{figure} ../figures/03_incremental_model_building.png
---
width: 820px
alt: Successive fits to a GNSS time series showing trend only, trend plus seasonal terms, and trend plus seasonal terms and offsets.
---
Recommended visual: three successive fits with their residuals. Use this to ask which remaining structure justifies the next model term.
```

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

```{figure} ../figures/03_residual_diagnostics.png
---
width: 820px
alt: Residual time series illustrating remaining seasonality, an undocumented step, changing variance, and an isolated outlier.
---
Recommended visual: four compact residual examples, each with one diagnostic feature labeled. Ask students what model or metadata check each pattern motivates.
```

---

## Network-Common Signals

Not every coherent signal is tectonic. Reference-frame errors, orbit or clock errors, and broad environmental loading can appear at many stations simultaneously.

Comparing neighboring stations helps distinguish:

- local monument or equipment problems
- regional deformation
- network-wide common-mode error

Regional filtering can reduce common-mode noise, but it can also remove spatially broad deformation if applied without care.

```{figure} ../figures/03_common_mode_network.png
---
width: 820px
alt: Several nearby GNSS time series sharing one coherent fluctuation while one station also contains a local offset.
---
Recommended visual: aligned time series from several nearby stations with a shared signal shaded and one station-specific anomaly marked.
```

---

# Uncertainty Is More Than Error Bars

Daily formal uncertainties describe precision under the assumptions of the position solution.

GNSS residuals are commonly correlated through time because of monument motion, environmental effects, reference-frame errors, and processing artifacts.

If a velocity fit assumes independent residuals when the noise is correlated, its uncertainty is usually too small.

> **Key distinction:** A good fit describes the observations; a realistic uncertainty describes how confidently we know the parameters.

```{figure} ../figures/03_white_vs_colored_noise.png
---
width: 800px
alt: Two residual series with similar scatter but different temporal correlation and different velocity uncertainty.
---
Recommended visual: contrast white and temporally correlated residuals with similar RMS. Report the larger slope uncertainty for the correlated case.
```

---

# Slow-Slip Events

In Cascadia, slow-slip events were recognized when GNSS stations showed temporary reversals of their long-term motion at the same time as tectonic tremor.

In a detrended time series, a slow-slip event appears as displacement accumulated over days to weeks rather than an instantaneous step.

Between events, stations resume their inter-ETS motion. The inter-ETS slope can differ from the long-term slope because repeated slow slip contributes to the full time series.

```{figure} ../figures/03_slow_slip_cartoon.png
---
width: 800px
alt: Detrended GNSS time series showing repeated gradual reversals during slow-slip events and approximately linear inter-event segments.
---
Recommended visual: an idealized Cascadia east-component time series with SSE intervals shaded and inter-ETS slopes labeled. Follow it immediately with the real ALBH example.
```

---

# Example: ALBH in Cascadia

Use the raw and detrended east-component time series for station ALBH.

Ask students to identify:

1. the long-term interseismic trend in the raw series
2. why the transients are difficult to see before detrending
3. the direction and duration of individual reversals
4. the approximately steady inter-ETS segments
5. variation in displacement among slow-slip events

```{figure} ../figures/03_albh_raw_detrended.png
---
width: 820px
alt: Raw and detrended east-component GNSS position time series for station ALBH, with slow-slip events visible as temporary reversals.
---
Raw and detrended east-component time series for ALBH. Recommended source: reproduce from the documented provider data used in the laboratory, then mark several slow-slip intervals and cite the data provider and processing version.
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

```{figure} ../figures/03_step_vs_transient_sampling.png
---
width: 800px
alt: An abrupt step and a gradual ramp sampled continuously and across a data gap.
---
Recommended visual: show how a data gap makes a ramp indistinguishable from a step. This directly motivates checking nearby stations and metadata.
```

---

# GNSS II Summary

- A position or velocity is meaningful only in a specified reference frame.
- GNSS time series superimpose long-term motion, seasonal signals, offsets, transients, and noise.
- Unmodeled signals can bias velocity and displacement estimates.
- Residuals test model adequacy; correlated noise affects parameter uncertainty.
- Slow slip is most visible after long-term and seasonal signals are removed.
- Velocities from many stations form the field used to estimate tectonic strain.

```{figure} ../figures/03_positions_to_strain.png
---
width: 800px
alt: Workflow from three-component station positions through time-series models to a regional velocity field and crustal strain.
---
Recommended visual: close the lecture with the analysis chain—positions, modeled time series, velocity vectors, and strain field—previewing the next use of GNSS observations.
```

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

```{figure} ../figures/03_lab_target_output.png
---
width: 820px
alt: Example laboratory output with three GNSS components, nested models, slow-slip event window, and residuals.
---
Recommended visual: show students the expected final product without supplying the numerical answer—three components, nested model comparison, shaded slow-slip interval, and nearby-station residuals.
```

---

# Additional Resources

> **GNSS Data:** [Nevada Geodetic Laboratory GPS Network Map](https://geodesy.unr.edu/NGLStationPages/gpsnetmap/GPSNetMap.html)  
> Explore GNSS station locations, position time series, and velocities from the Nevada Geodetic Laboratory.

> **Regional GNSS Data:** [Pacific Northwest Geodetic Array (PANGA)](https://www.panga.org/)  
> Access GNSS station information, position time series, velocity fields, and other geodetic products for Cascadia and the Pacific Northwest.
