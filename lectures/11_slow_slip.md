# Slow Slip Events on Subduction Interfaces

## Purpose

Subduction zone faults do not spend all their time locked or freely sliding.
Between the seismogenic locked zone and the deep creeping region there is a
transition zone where the fault slips intermittently — slowly enough to produce
no felt shaking, but fast enough to shift GNSS stations by millimetres and
generate a distinctive seismic signal.

In this lecture, we will:

- explain where slow slip fits in the subduction seismic cycle and why it matters
  for seismic hazard
- describe the seismic observables — tremor and low-frequency earthquakes — and
  explain how they are related to fault slip
- place slow slip in a global context
- use scaling relations to characterise and compare individual events

---

# Discovering Tremor

Traditional earthquakes have impulsive, easily identifiable P and S waves. These arrivals occur at many stations across a network The timing of arrivals indicative of source location
The seismic signature of slow earthquakes is different, subtle, and was discovered accidentally...

```{figure} ../figures/11_earthquakes.png
---
name: Earthquake seismograms
width: 620px
alt: Example recording of an earthquake on several stations in the Pacific Northwest.
---
Example recording of an earthquake on several stations in the Pacific Northwest.  Each trace represents the motion of the ground in a particular direction at the location of the station.  An earthquake is visible as a set of p and s-waves recorded on each station that display clear moveout and amplitude decay.
```

Kazushige Obara saw something strange -- he documented “Small amplitude tremors that lasted from a few minutes to a few days”.  These signals were most apparent in the 1-10 Hz frequency band. The tremors were difficult to locate without P & S but crude methods put them at 35-45 km depth for 600 km along strike.  Individual tremors were not linked to slow earthquakes (yet).

```{figure} ../figures/11_tremors.png
---
name: Tremor seismograms
width: 600px
alt: Example recording of an tremor event on several stations in the Pacific Northwest.
---
Example recording of an earthquake on several stations in the Pacific Northwest.  Each trace represents the motion of the ground in a particular direction at the location of the station.  An the tremor simply looks like coherent noise (i.e. the same character seismogram recorded on many stations)
```
---

# Discovering Slow Slip

As you know from this class, GPS records are dominated by inter-seismic strain accumulation. Periodic slow earthquakes were first identified in Cascadia and manifest as transient, short-duration reversals in the long term trend. Visible synchronously across multiple stations in the network.

```{figure} ../figures/11_miller.jpeg
---
name: Tremor seismograms
width: 600px
alt: Example recording of an tremor event on several stations in the Pacific Northwest.
---
Time series for GPS stations along the Cascadia margin. Baseline lengths are from weekly station positions with respect to DRAO. (Inset) Time series shows daily
positions for Friday Harbor (SC02) for 2002 in the global reference, illustrating the onset of the latest of the slow earthquakes.  From [Miller et al. (2002)](https://doi.org/10.1126/science.1071193).
```

---

# Discovering Slow Slip AND Tremor

In 2003, Garry Rogers and Herb Dragert showed that GNSS stations along the
Pacific Northwest coast periodically reversed their long-term eastward motion
for two to three weeks before resuming. The reversals were simultaneous across
hundreds of kilometres of coastline and coincided with bursts of previously
unexplained seismic tremor beneath southern Vancouver Island and northern
Washington.

The implication was immediate: the deep subduction interface was creeping
episodically and silently — a new class of fault behaviour that had gone
unnoticed because it looked like nothing.

> What would you expect to see in a detrended east-component GNSS time series
> during a slow slip event? In which direction would the station move?

```{figure} ../figures/11_rogers_dragert_2003.jpg
---
name: Rogers Dragert 2003
width: 600px
alt: Blue circles are daily east position time series of a GPS site near Victoria. The green line is the long term eastward motion of the site (with respect to North America), and the red saw-tooth line shows the motion of the site between events is faster than the long-term motion. The bottom black line shows the number of hours of tremor activity observed on southern Vancouver Island.
---
Top panels: east-component position time series at Pacific Northwest GNSS stations showing episodic westward reversals of ~5 mm over
two to three weeks. Bottom panel: tremor amplitude recorded at a broadband
seismograph station. The spatial coherence of the reversals and their coincidence
with tremor identified these as slow slip events on the deep subduction interface.
[Rogers and Dragert (2003)](https://doi.org/10.1126/science.1086153)
```

---

# The Subduction Seismic Cycle

The Cascadia interface can be divided into three depth zones with fundamentally
different frictional behaviour.

```{figure} ../figures/11_cascadia_xsection.jpg
---
name: Cascadia cross-section
width: 820px
alt: Cross-section of the Cascadia subduction zone showing the locked seismogenic
  zone at 0 to 25 km depth, the slow-slip zone at 25 to 45 km depth, and the
  freely creeping zone below 45 km.
---
Schematic cross-section of the Cascadia subduction zone (not to scale). The Juan
de Fuca plate subducts beneath North America at ~40 mm/yr. The locked zone
accumulates elastic strain that is released in Mw 9 megathrust earthquakes. Slow
slip occurs in the transition zone immediately downdip. GNSS stations on the
overriding plate record both interseismic loading and slow-slip transients.
```

| Zone | Depth | Behaviour |
|------|-------|-----------|
| **Locked** | 0–25 km | Elastic strain accumulates; releases in Mw 9 megathrust rupture |
| **Slow-slip transition** | 25–45 km | Episodic creep; generates tremor and millimetre-scale surface displacement |
| **Freely creeping** | > 45 km | Stable sliding; no stress accumulation |

**Hazard connection.** Slow slip occurs in the transition zone immediately
downdip of the locked patch. Each slip episode transfers stress updip onto the
locked zone, moving it incrementally closer to the stress level at which it will
fail. Slow slip does not trigger the megathrust earthquake — the loading rate is
far too slow and the stress increment too small — but it is a persistent part of
the same loading cycle.

**Inter-event behaviour.** Between slow slip events, GNSS stations continue to
move eastward as interseismic locking drags the overriding plate. This
inter-event velocity differs slightly from the long-term time-averaged velocity
because slow slip contributes to the full record. When measuring the secular rate
from a GNSS time series that spans multiple events, the fitted slope absorbs both
components. In the lab you will remove this combined trend before isolating the
displacement of a single event.

---

# Slow Slip Is Worldwide

Slow slip events have now been documented on nearly every well-instrumented
subduction zone. The properties differ — recurrence intervals range from days
to years, depths from 15 to 60 km — but the fundamental phenomenon is the same.

```{figure} ../figures/11_global_sse_map.png
---
name: Global SSE map
width: 820px
alt: World map showing subduction zones with documented slow slip events including
  Cascadia, Hikurangi, Nankai, Mexico, Alaska, Costa Rica, and Japan.
---
Global distribution of regions with modern deep slow slip and tremor along with exhumed blueschist and eclogite
facies subduction complexes. 
```

| Region | Recurrence | Duration | Notes |
|--------|-----------|----------|-------|
| Cascadia (N. Washington–S. Vancouver Is.) | ~14 months | 2–6 weeks | Very well-instrumented record |
| Hikurangi, New Zealand | weeks to years | days to months | Multiple depth ranges |
| Nankai, Japan | 6 months–6 years | days to weeks | Another very well-instrumented record |
| Mexico (Guerrero) | ~4 years | months | Very large events |
| San Andreas | days-months | hours-days | Episodic and more continuous events |

---

# Seismic Tremor

## What is tectonic tremor?

Tectonic tremor is a low-amplitude, emergent, non-impulsive seismic signal
lasting minutes to hours. It has no clear P or S wave arrivals and no
identifiable first motion. In the frequency domain it is bandlimited to roughly
1–8 Hz, well below the dominant frequency of a comparable magnitude earthquake.

Tremor was first observed in volcanic settings and dismissed as noise. When it
appeared in Cascadia it was eventually recognised as a distinct tectonic signal
because:

- it is spatially coherent across the network
- its location tracks the deep subduction interface
- its occurrence is temporally correlated with GNSS reversals

```{figure} ../figures/11_tremor_earthquake.gif
---
name: Tremor seismogram
width: 400px
alt: The seismic record of an earthquake consists of an initial P wave and bigger S wave, with vibrations tapering off in less than a minute. Tremors are a constant rumbling, like a continuous 0.5 magnitude earthquake, that can go on for 20 minutes or more. (Robert Nadeau/UC Berkeley).
---
The seismic record of an earthquake consists of an initial P wave and bigger S wave, with vibrations tapering off in less than a minute. Tremors are a constant rumbling, like a continuous 0.5 magnitude earthquake, that can go on for 20 minutes or more. (Robert Nadeau/UC Berkeley).
```

---

## Tremor detection and location

Tremor is detected using envelope correlation across arrays of broadband or
short-period seismographs. Because there are no impulsive arrivals to pick,
travel-time-based location methods cannot be applied directly. The PNSN uses
a network-averaged envelope approach; more precise locations use waveform
backprojection or matched-filter techniques.

Tremor locations in Cascadia form a narrow band parallel to the trench at
depths of 25–45 km, coinciding with the inferred position of the subduction
interface.

```{figure} ../figures/11_tremor_catalog.mp4
---
name: Tremor locations
width: 820px
alt: Video of showing time-latitude diagram of PNSN tremor detections in Cascadia with time-dependent detections.
---
PNSN tremor catalog for northern Cascadia. Left: map view showing tremor locations Right:
time-latitude diagram showing tremor detections over multiple years. Each vertical
cluster of dots is an individual slow slip episode; the along-strike extent and
propagation pattern are visible within events. This movie made by Aaron Wech from Alaska Volcano Observatory shows 171,197 tremors in the Cascadia Subduction Zone from 2012.1.3 to 2016.1.9 (15 days/second). 
```

---

## Tremor as a proxy for slow slip

Tremor cannot directly measure fault slip. It tells us *when* and *roughly where*
the fault is moving; it does not tell us *how much*.

| Observable | What it gives you |
|-----------|-------------------|
| Tremor | Timing, rough location, real-time availability |
| GNSS | Displacement amplitude, spatial distribution, depth sensitivity |

The two datasets are complementary. Tremor is detected automatically in real
time and can define event boundaries within hours. GNSS processing takes days
to weeks and requires careful handling of secular and seasonal signals, but it
directly constrains the moment release and slip distribution needed for
seismic hazard assessment.

In this lab you will use tremor to identify and date the event, then use
GNSS to quantify it.

> Why might tremor give slightly different start and end dates than a GNSS
> analysis of the same event?

```{figure} ../figures/11_bartlow.gif
---
name: Tremor and slow slip
width: 600px
alt: Video of showing progression of slow slip from inversion of GNSS data and tremor in 2009 slow slip event.
---
Slip rate on the plate interface, averaged over two day intervals, during the 2009 slow slip event in Cascadia. Tremor epicenters are plotted in black for the same two-day intervals. The plate interface mesh is shown between 10 and 60 km depth. Note that not all of the modeled days are shown. [Bartlow et al. (2011)](https://doi.org/10.1029/2011GL048714)
```

---

# Low-Frequency Earthquakes

## What are LFEs?

Low-frequency earthquakes (LFEs) are small, repeating earthquakes embedded
within tectonic tremor. Unlike regular earthquakes, their waveforms are
depleted in high-frequency energy above ~8 Hz, suggesting a rupture process
that is slower or on a weaker material than the surrounding crust.

Shelly et al. (2007) showed that tremor in southwest Japan could be
decomposed into a superposition of repeating LFE sources, each occurring on
a small patch of the subduction interface. The same result was subsequently
demonstrated for Cascadia. Tremor is not simply noise — it is a swarm of
small overlapping earthquakes.

```{figure} ../figures/11_lfe_tremor.png
---
name: LFE waveform
width: 820px
alt: Waveform comparison between a regular small earthquake and a low-frequency
  earthquake of similar magnitude, showing the depletion of high-frequency energy
  in the LFE.
---
Waveform comparison between a regular small earthquake (top) and an LFE (bottom)
recorded at the same station. Both have similar surface amplitudes but the LFE
waveform has depleted high-frequency content, giving it a characteristic
emergent, low-pass-filtered appearance. P and S arrivals are discernible in the
LFE after stacking many repetitions. [Thomas et al. (2025)](https://doi.org/10.1126/sciadv.adz2832)
```

---

## LFE families and fault structure

An LFE *family* is a set of events that originate from the same small fault
patch and produce nearly identical waveforms. Because the source location is
fixed, families act as repeating probes of a specific point on the fault.

Individual LFEs are too small to locate reliably in the ambient noise. The
standard approach is to stack hundreds or thousands of events from the same
family to build a high-SNR template, then use matched-filter detection to
find all occurrences of that template in the continuous record.

LFE families in Cascadia are distributed along the transition zone at the same
depths as tremor, confirming that tremor is a direct expression of slip on the
interface.

```{figure} ../figures/11_lfes_probe.png
---
name: LFE families
width: 820px
alt: Schematic of LFE family locations within the subduction zone.
---
Summary schematic of the geophysical view of slow slip and tremor (SST), informed by geophysical imaging, source seismology, and geodesy. Earthquake ruptures in the seismogenic zone, and low frequency earthquakes (LFE) and very low frequency earthquakes in the SST zone release seismic energy (red patches). The plate interface away from the seismic patches slips by aseismic creep, often in episodic slow slip events. Slow slip in the SST zone (grey) is illuminated by tremors. LFE source patches are clustered in families that are sometimes aligned in the plate convergence direction. Fluid pressure is likely high along much of the plate interface and reaches lithostatic levels in the SST zone under the mantle wedge corner and forearc crust.
```

---

## LFEs and slip velocity

```{figure} ../figures/11_lfe_map_svi.png
---
name: LFE families
width: 500px
alt: Map of southern Vancouver Island LFEs from Bostock et al. 2013.
---
Map of southern Vancouver Island LFEs from Bostock et al. (7). LFE locations are indicated by circles
color coded by depth. Stations used in the Bostock et al. (7) study are shown as triangles. Stations used in (B) are annotated with station names. [Thomas et al. (2025)](https://doi.org/10.1126/sciadv.adz2832)
```

The rate at which LFEs occur — events per hour from a given family — scales
with the local slip velocity of the fault. When the fault creeps faster, LFEs
from that patch occur more frequently.

This makes LFE rate a high-temporal-resolution record of fault slip velocity,
complementary to the lower-temporal-resolution but amplitude-sensitive GNSS
record. During a slow slip event, LFE rates spike by one to two orders of
magnitude above the inter-event background.

```{figure} ../figures/11_tracking_slip.png
---
name: LFEs in space and time.
width: 820px
alt: LFEs tracking slip in space and in time.
---
(A) LFEs from the Bostock et al. (7) catalog are plotted as a function of date and along-­ strike distance (Fig. 1A)
color coded by magnitude. Gray circles indicate tremor locations from the catalog of Wech and Creager (3). The main front propagates southward at ~5 km/day, and sec-
ondary fronts manifest as vertically oriented groups of events closely spaced in time (four are marked with arrows). The direction of propagation of the main front and the
along-­ strike location of LFE 141 are marked. The horizontal and vertical gray boxes outline the regions shown in (B) and (C), respectively. hr, hour. (B) LFEs in family 141
plotted as a function of time and magnitude. The gray line shows cumulative moment in newton-­ meters. (C) Zoom-­ in of the region outlined by the yellow box in (A) show-
ing a secondary front illuminated by both LFEs and tremor on 14 September that propagates at a speed of ~12 km/hour.
```

---

# Slow Slip and the Next M9

A common and understandable question: does slow slip *cause* the next
megathrust earthquake, or could it somehow *prevent* it?

**What slow slip does.** Each slip episode in the transition zone transfers a
small increment of stress updip onto the locked patch. Over many cycles, this
contributes to the stress budget that will ultimately be released in a Mw 9
rupture. In that sense, slow slip is part of the loading process.

**What slow slip does not do.** There is no evidence that any individual
slow slip event significantly advances or retards the timing of the next
megathrust earthquake. The stress increment per episode is small compared to
the total stress drop in a Mw 9, and no Cascadia slow slip event has preceded
anomalous seismicity or triggered rupture on the locked zone. Slow slip in the
transition zone may actually relieve some of the stress in that region, but it
does not reduce stress on the locked patch above it.

**The practical implication.** Slow slip recurrence is not a useful clock for
the M9. The ~14-month cycle tells us about frictional properties of the
transition zone, not about the state of the locked zone. Probabilistic hazard
assessments for Cascadia treat slow slip as background loading, not as a
precursory signal.

> If slow slip loads the locked zone with each episode, why is it not
> considered a useful predictor of the next megathrust rupture?

---

# Scaling

## Slow events on the moment-duration diagram

Regular earthquakes obey a well-known scaling: seismic moment scales with the
cube of rupture duration because rupture propagates at a roughly constant
fraction of the shear wave speed. All regular earthquakes fall close to the
same line in log(M₀)–log(T) space regardless of size.

Slow slip events do not follow this line. They have far more moment per unit
duration than a regular earthquake of equivalent rupture length would, or
equivalently, far longer duration per unit moment. On the moment-duration plot,
slow events define a separate, shallower trend — the "slow earthquake" scaling.

$$
M_0 \sim T^1 \quad \text{(slow events)} \qquad M_0 \sim T^3 \quad \text{(regular earthquakes)}
$$

The difference reflects a fundamentally slower slip velocity: the fault moves
at mm to cm per day rather than metres per second.

```{figure} ../figures/11_ide_scaling.png
---
name: Moment duration scaling
width: 600px
alt: Log-log plot of seismic moment versus characteristic duration for slow
  earthquakes including LFEs, VLFs, SSEs, and ETS events, showing M0 proportional
  to t scaling distinct from regular earthquakes.
---
Comparison between seismic moment and the characteristic duration of various slow
earthquakes. LFE (red), VLF (orange), and SSE (green) occur in the Nankai trough
while ETS (light blue) occur in the Cascadia subduction zone. These follow a
scaling relation of M₀ ∝ t for slow earthquakes. Purple circles are silent
earthquakes. Black symbols are slow events listed in the bottom half of Table 1.
(a) Slow slip in Italy, representing a typical event (circle) and proposed
scaling (line). (b) VLF earthquakes in the accretionary prism of the Nankai
trough. (c) Slow slip and creep in the San Andreas Fault. (d) Slow slip beneath
Kilauea volcano. (e) Afterslip of the 1992 Sanriku earthquake. Typical scaling
relation for shallow interplate earthquakes is also shown by a thick blue line.
[Ide et al. (2007)](https://doi.org/10.1038/nature05780).
```
---

## Duration and magnitude in Cascadia

Michel et al. (2019) compiled a catalog of Cascadia SSEs and showed that
event duration and moment magnitude scale predictably within the slow-event
population.

```{figure} ../figures/11_michel_duration.png
---
name: Michel duration Mw
width: 500px
alt: Log-log plot of seismic moment versus duration for Cascadia slow slip events
  compared to cubic scaling of regular earthquakes, showing slow slip follows a
  linear moment-duration relationship.
---
Moment–duration scaling for Cascadia slow slip events. Blue shaded boxes outline
the domain defined by minimum and maximum estimates of SSE duration and moment
release; blue filled circles represent the mean values. Green and orange filled
circles show the expected moment–duration distribution for M₀ ∝ T³ and M₀ ∝ T
respectively, after accounting for the temporal filter effect. The dashed line
shows cubic scaling of regular earthquakes for comparison.
[Michel et al. (2019)](https://doi.org/10.1038/s41586-019-1673-6).

```

Longer events release more moment, as expected for a process whose rate is
set by slip velocity rather than rupture propagation speed. The scatter about
the trend reflects differences in slip velocity and fault area across events.

---

## Defining event boundaries

Moment magnitude requires knowing when the event started and ended. This is
less straightforward than it appears.

**Start.** Tremor rate rises sharply above the inter-event background over
one to two days. The onset is usually well-defined. GNSS stations begin their
reversal within the same window.

**End.** Tremor rate decays gradually. There is always some background tremor
between events at slightly greater depths, and secondary activations are
common. The return of GNSS stations to their pre-event trajectory is a cleaner
criterion but requires careful modeling of the secular trend.

**Practical approach.** Use the tremor event rate to identify the onset;
define the end as the day the 7-day rate first returns to its inter-event
level and remains there. Accept a few days of uncertainty and report it. In
the lab you will make this determination from the PNSN tremor catalog and
examine how it affects the GNSS offset measurement.

---

# Summary

- Slow slip occurs in the frictional transition zone immediately downdip of the
  locked seismogenic zone.
- Each episode transfers a small stress increment updip onto the locked patch;
  it is part of the loading cycle but is not a useful predictor of the next
  Mw 9.
- Tectonic tremor is a superposition of low-frequency earthquakes from
  repeating sources on the transition zone interface.
- Tremor gives real-time timing and location; GNSS gives displacement
  amplitude and spatial distribution. Both are needed for a complete picture.
- LFE rate scales with fault slip velocity, providing a high-resolution record
  of when and where the fault is moving.
- Slow events follow M₀ ∝ T scaling, distinct from regular earthquakes.
- Event boundaries are defined primarily from tremor rate, with GNSS providing
  an independent check on timing and amplitude.

---

# Laboratory

Students will apply the full observational pipeline to the 2024 northern
Cascadia slow slip event:

- identify the event in the PNSN tremor catalog and determine start and end
  dates from the event rate time series
- extract GNSS displacement offsets at network stations using pre- and
  post-event window averages, with and without a common-mode filter
- build the Green's function matrix relating updip fault slip to surface
  displacement using an elastic half-space model
- invert for the slip distribution using regularised least squares and
  examine the effect of regularisation choices on the result
- compute the seismic moment and plot the result on the Michel et al. (2019)
  duration-magnitude diagram

---

# Additional Resources

> **PNSN Tremor Catalog:** [https://pnsn.org/tremor](https://pnsn.org/tremor)  
> Real-time tremor detections for the Pacific Northwest with interactive maps
> and downloadable catalogs.

> **Rogers and Dragert (2003):** *Episodic Tremor and Slip on the Cascadia
> Subduction Zone: The Chatter of Silent Slip.* Science, 300, 1942–1943.  
> The original discovery paper.

> **Shelly, Beroza, and Ide (2007):** *Non-volcanic tremor and low-frequency
> earthquake swarms.* Nature, 446, 305–307.  
> Demonstrates that tremor is composed of repeating LFEs.

> **Michel et al. (2019):** *Creep along the southern Cascadia subduction zone
> from GPS, seismic, and aseismic tremor data.* Journal of Geophysical Research:
> Solid Earth, 124, 6630–6650.  
> Source of the duration–magnitude scaling used in the lab.

> **Ide et al. (2007):** *A scaling law for slow earthquakes.* Nature, 447,
> 76–79.  
> Establishes the M₀ ∝ T scaling for slow events.
