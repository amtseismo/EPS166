# Subsidence: Causes and Consequences

## Purpose

TIn tectonically quiet regions, the ground is not static.  Subsidence is gradual downward motion of the ground.  It can be observed easily using modern geodetic tools is often non-tectonic.  This lecture focuses on subsidence driven by fluid withdrawal, sediment compaction, and surface loading.

In this lecture, we will:

- derive the physical basis for compaction-driven subsidence through Terzaghi's effective
  stress principle
- distinguish elastic from inelastic compaction and connect each to its geodetic signature
- survey the range of natural and anthropogenic drivers that produce subsidence
- interpret GNSS vertical time series and InSAR velocity maps in the context of groundwater
  extraction and aquifer-system mechanics
- examine three case studies — the Central Valley, the Mississippi River Delta, and Mexico
  City / Jakarta — in terms of their driving mechanisms, observed signals, and societal
  consequences
- frame subsidence as a compound hazard when combined with sea level rise

---

# Compaction

## Terzaghi's Effective Stress Principle

Subsidence driven by fluid withdrawal is governed by a single unifying principle. When a
porous medium is loaded, the applied stress is shared between the grain skeleton and the
pore fluid:

$$
\sigma = \sigma' + u
$$

- $\sigma$: total stress (overburden load; does not change as fluids are withdrawn)
- $\sigma'$: effective stress — the stress carried by the grain skeleton
- $u$: pore fluid pressure

When groundwater is pumped, pore pressure $u$ decreases. Total stress $\sigma$ remains
constant because the overburden does not change. Therefore effective stress $\sigma'$ must
increase:

$$
\Delta\sigma' = -\Delta u
$$

An increase in effective stress compresses the grain skeleton. For fine-grained materials
like clay, this compaction can be large and permanent. This is the master equation linking
groundwater extraction to surface deformation.

```{figure} ../figures/13_subsidence_terzaghi_schematic.png
---
name: Terzaghi effective stress
width: 680px
alt: Schematic showing total stress, pore pressure, and effective stress before and after
     groundwater withdrawal, with grain-to-grain contact forces indicated.
---
Illustration of the division of total stress in to effective stress and pore water pressure.  Panel (a) shows a saturated soil element carrying a total vertical stress of $\sigma_z$.  This total stress is carried by both the pore water pressure, $u$, and the effective stress, $\sigma'_z$.  Panel (b) is a close-up of an interparticle contact.  The effective stress is the portion carried by the interparticle contact forces.
```

---

## Elastic vs. Inelastic Compaction

Not all compaction is equal. The behavior of an aquifer system depends on whether the
material being compressed is coarse-grained (sands and gravels) or fine-grained (silts and
clays):

**Elastic compaction** — coarse-grained aquifer sands and gravels:
- Compresses under increased effective stress; recovers when pore pressure rebounds
- Relatively stiff; small strains per unit of head change
- Produces a seasonal signal in GNSS and InSAR that tracks head fluctuations

**Inelastic compaction** — fine-grained clays and silts (aquitards):
- Once effective stress exceeds the **preconsolidation stress** $\sigma'_c$, the clay
  structure irreversibly rearranges; deformation is permanent
- Fine-grained layers drain slowly — compaction lags the pumping signal by months to years

The preconsolidation stress records the maximum effective stress the clay has ever
experienced. Once that threshold is crossed, permanent compaction begins. Critically, this
is a one-way door: heads can recover, but the clay does not expand to its original
thickness.

```{figure} ../figures/13_compaction.png
---
name: Elastic and inelastic compaction
width: 700px
alt: Two-panel schematic showing head decline in an aquifer system alongside the resulting
     surface displacement, with seasonal elastic bounce and secular inelastic trend labeled.
---
When long-term pumping lowers ground-water levels and raises stresses on an aquitard layer beyond the preconsolidation-stress thresholds of that layer, the aquitards compact and the land surface subsides permanently.
```
👉 The geodetic signature is the key diagnostic: **seasonal reversible signal = elastic
response; secular irreversible trend = inelastic compaction.** InSAR and GNSS can
distinguish these without any hydrogeologic model.

---

# Causes of Subsidence

## Groundwater Extraction and Reduced Recharge

This is the dominant anthropogenic driver in most of the cases we will examine. The
mechanism is Terzaghi's: pumping reduces pore pressure, effective stress on the grain
skeleton increases, and the skeleton compacts. The magnitude of compaction depends on
whether the material is coarse-grained (elastic, recoverable) or fine-grained (inelastic,
permanent) — the distinction developed in the previous section.

Reduced recharge accelerates the same process by limiting head recovery. Its causes are
multiple and increasingly interconnected:

- **Drought** — reduced precipitation directly limits infiltration and stream recharge
- **Changing precipitation patterns** — a warming climate shifts the timing and form of
  precipitation; snowpack loss reduces the spring recharge pulse that historically
  sustained Central Valley aquifer heads
- **Impervious surfaces** — urban expansion replaces permeable soil with pavement and
  rooftops, routing precipitation to storm drains rather than aquifers
- **Managed recharge competition** — in heavily allocated systems, surface water that
  could recharge aquifers is instead diverted for irrigation or municipal use

Groundwater extraction and reduced recharge are not independent: drought forces more
pumping, which accelerates head decline, which triggers more inelastic compaction — a
positive feedback with no natural brake unless policy intervenes.

```{figure} ../figures/13_drought.jpg
---
name: GNSS and drought
width: 800px
alt: Land subsidence at a GPS station in the Central Valley plotted with changes in groundwater levels at a nearby well. 
---
Land subsidence at a GPS station in the Central Valley plotted with changes in groundwater levels at a nearby well. 
```

---

## Sediment Starvation and Natural Compaction

River deltas are naturally subsiding. The young Holocene sediments that build deltas —
clays, silts, sands, and peats deposited over the past few thousand years — are still
consolidating under their own weight. This natural compaction is the baseline against which
all anthropogenic drivers must be compared.

The natural system compensates through **sediment delivery**: annual floods deposit fresh
material across the delta surface, raising it at roughly the rate it subsides. This
balance maintained deltas near sea level for millennia.

Dam construction breaks the balance. Reservoirs trap the coarse and fine sediment load
that would otherwise reach the coast. The delta continues to compact naturally but no
longer receives the replenishment that kept pace with it. The result is a surface that
falls progressively below sea level — not because anything new is happening, but because
something old has stopped.

```{figure} ../figures/13_dam_impacts.jpeg
---
name: Sediment starvation schematic
width: 680px
alt: Schematic diagram showing adverse effects of river dams.
---
Sediment budget of a river delta before and after upstream dam construction. In the
natural state, sediment delivery offsets natural compaction and the surface remains near
sea level. After dam closure, the sediment flux to the coast collapses; compaction
continues unimpeded and the delta surface falls. The Mississippi, Nile, Mekong, and
Indus deltas all show this pattern.
```

👉 Sediment starvation is irreversible on human timescales. Even if a dam were removed,
the sediment stored in its reservoir would take decades to centuries to remobilize and
reach the coast. This distinguishes it from groundwater-driven subsidence, where policy
interventions can at least halt further inelastic compaction.

---

## Oxidation of Organic Soils

Peat and other organic-rich soils behave fundamentally differently from mineral soils.
When organic soils are drained — for agriculture, urban development, or flood control —
they do not simply compact mechanically. They **oxidize**: microbes metabolize the organic
matter in the presence of oxygen, converting solid organic carbon to CO₂ and water vapor.
The solid matrix literally disappears.

This process is:

- **Irreversible** — oxidized carbon cannot be restored
- **Continuous** — as long as the soil remains aerated and microbially active, mass loss
  continues
- **Sensitive to temperature** — warming accelerates microbial metabolism and therefore
  oxidation rates
- **Distinct from mechanical compaction** — it is a mass loss, not a rearrangement; no
  change in effective stress is required
  
```{figure} ../figures/13_sac_delta_subsidence.jpg
---
name: Sacramento delta subsidence
width: 800px
alt: Schematic cross-section through a city showing building loads transmitted through
     foundation soils into unconsolidated sediments below, with a subsidence bowl
     centered on the densest urban core.
---
(Left) vertical rate map over the Sacramento Delta generated by tying the line-of-sight rate maps from individual UAVSAR flight lines into a GNSS reference frame (NA12). Vertical GNSS rates (round colored markers) are in good agreement with the vertical rates estimated from InSAR, i.e., they fall within the uncertainty bounds. InSAR data within the overlap region (dashed black line) and those collocated with GNSS observations are used to estimate a planar correction applied to the InSAR data to tie the reference to GNSS. (Right) Corresponding vertical rate uncertainties show smaller uncertainty for regions with multiple observations made with different viewing geometries. Uncertainty variation within a UAVSAR flight line is increased by the large range of look angles across the swath when the LOS rates are projected into the vertical direction. Profiles through the data at selected locations are shown in Fig. 6 and Fig. 7. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.) [Bekaert et al. (2018)](https://doi.org/10.1016/j.rse.2018.10.023)
```

Rates of organic soil oxidation can reach several cm/yr under warm, well-drained
conditions. The Sacramento–San Joaquin Delta peat islands have lost 1–8 m of elevation
since they were drained for agriculture in the late 19th century — not primarily from
mechanical compaction, but from oxidation. Many islands now sit 3–5 m below sea level,
retained only by earthen levees.

```{figure} ../figures/13_sac_delta_subsidence_total.png
---
name: Sacramento delta subsidence in total
width: 600px
alt: Subsidence in the Sacramento-San Joaquin Delta
---
Subsidence in the Sacramento-San Joaquin Delta
```

---

## Anthropogenic Surface Loading

The weight of cities depresses the crust. Placing a large mass on unconsolidated sediments
increases total stress, which — by Terzaghi's principle — increases effective stress and
causes compaction. The same physics governs glacial isostatic adjustment, at a vastly
different scale.

The magnitude is typically small relative to groundwater-driven subsidence — a recent
analysis of New York City estimated a contribution of ~1–2 mm/yr from building loads alone
[Parsons et al. (2023)](https://doi.org/10.1029/2022EF003465). But on soft sediments in dense urban cores it is measurable with
InSAR, and it matters for two reasons:

1. It is **always present** in cities built on alluvium — it cannot be turned off by
   policy
2. In cities where groundwater pumping has been successfully regulated, loading may become
   the residual signal that explains why subsidence continues despite improved water
   management
   
```{figure} ../figures/13_new_york.jpg
---
name: New York
width: 800px
alt: Subsidence in New York
---
(a) Excerpt from building base outline database for New York City showing parts of Manhattan, Queens, and Brooklyn. Base outlines and height data were used to calculate total building floor areas, which combined with live and dead load values yields a building's mass. (b) The combined building load profile distributed in 100 m-by-100 m cells is shown superposed on the finite element model used to calculate subsidence.
```

---

## Additional Drivers

Three further drivers are worth naming, though they appear less prominently in today's
case studies:

**Hydrocarbon and fluid extraction** operates through the same Terzaghi mechanism as
groundwater pumping but at greater depth, over larger rock volumes, and often in regions
where the deformation signal is spatially separated from visible infrastructure. Coastal
Louisiana is the clearest example: the >50,000 oil and gas wells drilled in the delta
plain contribute a deep compaction signal that stacks on top of natural compaction and
sediment starvation.

**Karst dissolution and underground construction** produce localized but dramatic
subsidence through void formation rather than compaction. Sinkholes in karst terrain and
settlement above tunnels follow different mechanics than the Terzaghi framework — worth
flagging as a separate class of problem even if they are not the focus of this lecture.

**Sea level rise** is not a driver of subsidence — the ground is not sinking faster because
the ocean is rising. It is the reason subsidence becomes catastrophic. A coast subsiding
at 10 mm/yr experiences an effective **relative sea level rise** of 10 mm/yr + 3–4 mm/yr
(global mean) = 13–14 mm/yr. The two processes are independent in mechanism but
inseparable in consequence. We will return to this framing in the synthesis.

---

# The Central Valley

## Setting

The Central Valley of California extends approximately 700 km from Redding to Bakersfield
and is one of the most productive agricultural regions on Earth. It depends heavily on
groundwater; surface water allocations during droughts are frequently cut to zero, forcing
farmers entirely onto pumped groundwater.

The subsurface geology is critical to understanding the deformation signal:

- **Coarse-grained aquifers** (sands and gravels) fill much of the valley and produce the
  elastic seasonal signal
- **Corcoran Clay** — a laterally extensive, fine-grained lacustrine aquitard reaching 60+ m
  thickness in the southern valley — is the primary source of inelastic compaction and
  long-term subsidence
- The Corcoran Clay separates the valley-fill aquifer system into upper and lower zones;
  pumping-induced drawdown below the clay drives irreversible compaction that cannot be
  recovered even if pumping stops

Subsidence in the Central Valley was first documented in the 1920s. Modern satellite
geodesy has revealed its full spatial extent and shown that rates accelerated dramatically
during the 2012–2016 drought.

```{figure} ../figures/13_sj_subsidence_photo.jpg
---
name: Land subsidence in California
width: 400px
alt: Land subsidence in California
---
Land subsidence in California - Approximate location of maximum subsidence in the United States identified by research efforts of Dr. Joseph F. Poland (pictured). Signs on pole show approximate altitude of land surface in 1925, 1955, and 1977. The site is in the San Joaquin Valley southwest of Mendota, California. This photo shows the approximate location of maximum subsidence in the United States, identified by research efforts of Dr. Joseph F. Poland (pictured). The site is in the San Joaquin Valley southwest of Mendota, California. Signs on pole show approximate altitude of land surface in 1925, 1955, and 1977. The land surface subsided about 9 meters from 1925 to 1977 due to aquifer-system compaction.
```

---

## GNSS Evidence

```{figure} ../figures/13_sjv_gnss.png
---
name: Central Valley GNSS vertical GNSS velocities
width: 500px
alt: Result of GPS Imaging of the vertical velocity field using the median spatial filtered MIDAS velocities. The black dots represent the GPS stations. The color scale is in mm/yr; positive (red) is upward, and negative (blue) is downward, saturated at color scale limits.
---
Result of GPS Imaging of the vertical velocity field using the median spatial filtered MIDAS velocities. The black dots represent the GPS stations. The color scale is in mm/yr; positive (red) is upward, and negative (blue) is downward, saturated at color scale limits.
```

A single GNSS vertical time series contains multiple signals that can be separated and
interpreted independently:

```{figure} ../figures/13_CRCN.png
---
name: Central Valley GNSS time series CRCN
width: 500px
alt: Vertical GNSS time series from station CRCN in Tulare County showing seasonal
     oscillation superimposed on a long-term downward trend.
---
Vertical position time series from GNSS station CRCN. The seasonal
oscillation (amplitude ~14 mm) reflects elastic compaction and rebound of coarse-grained
aquifers tracking winter recharge and summer pumping. The secular downward trend reflects
irreversible compaction of the Corcoran Clayat a rate of 240 mm/yr.
```

---

## InSAR Evidence

```{figure} ../figures/13_ca_vlm.jpg
---
name: Vertical Land MOtion in CA
width: 800px
alt: CA VLM
---
VLM (mm/year) for 2015–2023 estimated from Sentinel-1 InSAR in combination with GNSS data (InSAR-VLM), relative to ITRF2014 [International Terrestrial Reference Frame, 2014 solution; (59)]. Negative VLM values reflect subsidence, while positive values reflect uplift. Uncertainties on rates (formal uncertainties, 1σ) and its trend temporal variability (also in fig. S1) within observation period are shown as insets. Site/event locations are marked as GNSS (circles), tide gauge (inverted triangles), and major earthquakes (stars). Tectonic plate boundaries (maroon lines) follow: PA, Pacific plate; NA, North America plate; and JF, Juan de Fuca plate (66). [Govorcin et al. (2025)](https://doi.org/10.1126/sciadv.ads8163)
```

The spatial resolution of InSAR reveals something that GNSS cannot: the **heterogeneous
pattern of compaction** reflects the underlying geology at the scale of individual fields
and canal segments. Where the Corcoran Clay is thick, subsidence is rapid and permanent.
Where it is absent or thin, the signal is elastic and recovers seasonally.

Practical consequences are severe:

- The **California Aqueduct** has sagged and required repeated costly re-leveling; flow
  capacity is reduced where the canal floor has dropped below design grade
- **Well casings** shear as fine-grained layers compact differentially relative to the
  steel casing
- **Canal and road infrastructure** in the most affected counties shows ongoing
  deformation damage measurable from space

---

## Policy Response and Partial Recovery

California's **Sustainable Groundwater Management Act (SGMA, 2014)** is a three-bill
package signed by Governor Jerry Brown in September 2014. It is the first comprehensive
statewide groundwater regulation in California's history. SGMA requires high- and
medium-priority basins to reach sustainable groundwater use by **2042**, with critically
overdrafted basins — including the most severely affected parts of the San Joaquin Valley
— held to an earlier deadline of **2040**. Implementation is local: Groundwater
Sustainability Agencies (GSAs) formed from regional authorities are responsible for
developing and implementing Groundwater Sustainability Plans for each basin.

The wet years of 2016–2017 and early SGMA implementation produced measurable changes in
GNSS records: the elastic seasonal amplitude decreased, and the apparent secular rate
slowed. This partial recovery is **not** a reversal of inelastic compaction — it is head
recovery in the coarse-grained aquifer.

👉 Elastic rebound is recoverable; inelastic compaction of the Corcoran Clay is permanent.
**SGMA can stop or slow deformation but cannot undo what has already been lost.** The geodetic
record makes this distinction legible in a way that no water-level measurement alone can.

---

# Deltas

## Global Delta Subsidence

Deltas occupy only 1% of Earth's land area but host an estimated 350–500 million people,
including 10 of the world's 34 megacities. They are also, almost universally, sinking.

[Ohenhen et al. (2026)](https://doi.org/10.1038/s41586-025-09928-6) used Sentinel-1 InSAR
to map surface-elevation change across 40 major global deltas between 2014 and 2023,
providing the first systematic, high-resolution, delta-wide subsidence dataset at global
scale. Key findings:

- In **38 of 40 deltas**, more than 50% of the delta area is subsiding
- In **18 of 40 deltas**, average subsidence rates exceed the regional geocentric sea-level
  rise rate — meaning subsidence, not climate-driven sea-level rise, is the dominant driver
  of relative sea-level rise for those populations today
- Approximately **236 million people** live in deltas where subsidence outpaces sea-level
  rise — 50% more than those where the reverse is true
- The fastest-sinking deltas are the **Chao Phraya** (Thailand), **Brantas** (Indonesia),
  and **Yellow River** (China), with average rates more than twice the current global
  sea-level rise rate
- Groundwater storage loss is the strongest single anthropogenic predictor of subsidence,
  dominant in 10 of the 40 deltas; most others reflect mixed contributions from groundwater
  extraction, sediment flux reduction, and urban expansion

```{figure} ../figures/13_deltas.webp
---
name: Global delta subsidence
width: 720px
alt: World map showing 40 global deltas color-coded by average land subsidence rate, with
     circle size proportional to the percentage of delta area subsiding faster than
     geocentric sea-level rise.
---
Spatial pattern of VLM across global deltas. a, Proportion of each delta exposed to different rates of subsidence. Note that only subsiding areas are represented in each bar, and areas of uplift within each delta are omitted to emphasize the extent of elevation loss. b–m, Spatial maps of VLM rates for the Fraser (Canada) (b), Mississippi (the USA) (c), Parana (Argentina) (d), Niger (Nigeria) (e), Nile (Egypt) (f), Po (Italy) (g), Ganges–Brahmaputra (India–Bangladesh) (h), Chao Phraya (Thailand) (i), Mekong (Vietnam) (j), Red River (Vietnam) (k), Pearl (China) (l), Yellow River (China) (m) deltas. Positive VLM (green–purple hues) suggests uplift or elevation gain, whereas negative VLM (yellow–orange–red hues) indicates land subsidence. The spatial VLM maps for the other 28 deltas are shown in Extended Data Figs. 2–4. Background image in b–m is Esri, streets-dark. Scale bars, 5 km (b); 50 km (c,f,h,j); 20 km (d,e,i,k,l,m); 10 km (g). After [Ohenhen et al. (2026)](https://doi.org/10.1038/s41586-025-09928-6).
```

👉 For most delta populations, the immediate threat is not climate-driven sea-level rise —
it is the ground beneath them sinking. Subsidence is faster, more localized, and in
principle more tractable. But **65% of the deltas** fall into what Ohenhen et al. call the
"Unprepared Divers" category: high relative sea-level rise rates combined with low
institutional capacity to respond.

The Mississippi Delta is the case we will examine in detail — chosen not because it is
the worst (the Asian deltas are faster-sinking) but because its multi-driver complexity
and long geodetic record make it the most instructive.

---

## Mississippi River Delta

The Mississippi Delta is the most instructive example of subsidence caused by multiple
stacked drivers. Separating them is a research problem worth solving, because different drivers call for different policy responses.

**Natural compaction** is likely the dominant driver. [Törnqvist et al. (2008)](https://doi.org/10.1038/ngeo129) used radiocarbon-dated sediment
cores to directly measure millennial-scale compaction rates in the delta, finding rates up to 5 mm/yr primarily associated with peat compression under overburden loading, with locally higher rates plausible over shorter timescales. The delta is built on ~10,000 years of Holocene sediments — clays, silts, peats, and sands that are still consolidating under their own weight. This is a critically important distinction from the Sacramento Delta, where the dominant process is **oxidation** of drained, aerated peat. In coastal Louisiana the peat remains buried and largely waterlogged; it compacts mechanically under overburden load rather than being biochemically consumed. Both produce subsidence; the mechanisms are entirely different.

**Sediment starvation** is the principal human modification to the natural system. The extensive levee network built to control flooding and protect navigation has disconnected
the Mississippi from its floodplain. Before levee construction, annual floods deposited fresh sediment across the delta surface, partially offsetting natural compaction. That replenishment is now cut off. Human drivers stack on top of a large natural signal — they do not replace it.

**Hydrocarbon extraction** adds a deep component. More than 50,000 oil and gas wells have
been drilled in coastal Louisiana. Fluid withdrawal at depth produces the same Terzaghi
response as groundwater pumping — reduced pore pressure, increased effective stress,
compaction — but at greater depth and over larger volumes.

**Groundwater pumping** contributes an additional shallow signal in urban areas including
New Orleans.

> **Question:** Given this stack of drivers, which one would you target with policy, and
> why? What would success look like in a geodetic time series?

---

## New Orleans

New Orleans was built largely on the natural levees and backswamp deposits of the lower
Mississippi. As the city expanded through the 20th century, drainage of low-lying areas
caused rapid subsidence through clay compaction and organic soil oxidation. Much of the
city now lies 1–3 m below sea level; some neighborhoods reach 5 m below.

```{figure} ../figures/13_mrd.webp
---
name: New Orleans InSAR subsidence
width: 720px
alt: Pattern of land subsidence over the Mississippi River delta. More than half of the land measured on the Mississippi delta is sinking at a rate faster than four millimeters per year, with a maximum sinking rate exceeding 30 millimeters per year. 
---
Pattern of land subsidence over the Mississippi River delta. More than half of the land measured on the Mississippi delta is sinking at a rate faster than four millimeters per year, with a maximum sinking rate exceeding 30 millimeters per year. 
```

The geodetic record extends back decades through leveling surveys, allowing a long-term
arc to be constructed:

- Early 20th century: rapid subsidence as low-lying areas were drained and pumped
- Mid-20th century: continued decline; much of the city below sea level by 1950
- Late 20th century to present: continued subsidence at 6–9 mm/yr in the fastest areas

Katrina (2005) is the most visible consequence of this long-term trajectory. The storm
surge that overtopped and breached the levees entered a city that was already well below
sea level — the flood was catastrophic in part because decades of subsidence had already
made it inevitable.

---

## The Compound Hazard

```{figure} ../figures/13_rslr.gif
---
name: Compound hazard animation
width: 680px
alt: Animation depicting relative sea-level rise due to rising ocean surface level and land subsidence due to groundwater withdrawal (Source: Earth Observatory of Singapore)
---
Animation depicting relative sea-level rise due to rising ocean surface level and land subsidence due to groundwater withdrawal (Source: Earth Observatory of Singapore)
```

The key number for infrastructure planning is not global mean sea level rise — it is
**relative sea level rise**, the change in water level relative to the land surface:

$$
\dot{e}_\text{RSLR} = \dot{e}_\text{SLR} + |\dot{e}_\text{subsidence}|
$$

At 6–9 mm/yr of subsidence plus 3–4 mm/yr of absolute sea level rise, relative sea level
rise exceeds **1 cm/yr** in parts of coastal Louisiana. Infrastructure designed for 2050
flood probabilities must account for both terms. Geodesy provides the subsidence term —
it is the only reliable way to measure it at the spatial resolution needed for planning.

👉 The geodetic community provides one term in the compound hazard equation. Without it,
coastal risk assessments underestimate exposure by a factor of two or more in rapidly
subsiding regions.

---

# Sinking Cities

The narrative of sinking cities is often framed around coastal megacities in Asia or
Europe, but subsidence is pervasive across American cities as well — including inland
ones where sea level rise is not a direct concern. The hazard there is primarily
infrastructure damage from differential settlement.

[Ohenhen et al. (2025)](https://doi.org/10.1038/s44284-025-00240-y) used Sentinel-1
InSAR from 2015–2021 to map VLM across the 28 most populous US cities at ~28 m
resolution. Key findings:

- **At least 20% of the urban area is sinking in every single city** studied
- In 25 of the 28 cities, at least 65% of the area is sinking
- Approximately **34 million people** — 10% of the total US population — live on
  sinking land across these cities
- **Texas cities dominate the rankings**: Houston, Fort Worth, and Dallas have the
  highest area-weighted average subsidence rates, exceeding 4 mm/yr; Houston has 42%
  of its land area sinking faster than 5 mm/yr and 12% faster than 10 mm/yr
- Groundwater extraction is the dominant driver nationally, consistent with the
  Terzaghi mechanism: **76% of the variance in subsidence rates across confined
  aquifer systems** is explained by groundwater level changes alone
- In northeastern and midwestern cities (New York, Philadelphia, Washington DC,
  Chicago, Indianapolis), **glacial isostatic adjustment** contributes 1–3 mm/yr of
  regional subsidence — a natural signal that cannot be mitigated
  
```{figure} ../figures/13_houston.webp
---
name: Houston subsidence
width: 720px
alt: Map of vertical land movement in Houston from [Ohenhen et al. (2025)](https://doi.org/10.1038/s44284-025-00240-y).
---
Map of vertical land movement in Houston from [Ohenhen et al. (2025)](https://doi.org/10.1038/s44284-025-00240-y).
```

```{figure} ../figures/13_subsidence_us_cities.webp
---
name: US cities subsidence
width: 720px
alt: Map of the 28 most populous US cities color-coded by area-weighted average VLM
     rate, with selected inset maps showing spatially variable subsidence patterns for
     New York, Houston, Las Vegas, Seattle, and Washington DC.
---
a, The average rate of VLM for 28 US cities as evaluated in this study. Each circle is color-coded to the respective average VLM for each city (Supplementary Table 2). b–f, Spatially varying VLM for New York, NY (b); Las Vegas, NV (c); Seattle, WA (d); Houston, TX (e) and Washington, DC (f). The location of each city is highlighted in a. Positive VLM (green–purple colors) indicates uplift, and negative VLM (yellow–orange–red colors) indicates subsidence. LGA, LaGuardia Airport, NY. Individual VLM maps for all 28 cities are shown in Extended Data Figs. 1–3. National and state boundaries in a are based on public domain vector data by World DataBank (https://data.worldbank.org/) generated in MATLAB. Background images in b–f from streets-dark ESRI, HERE, Garmin, Foursquare, METI/NASA, USGS. After [Ohenhen et al. (2025)](https://doi.org/10.1038/s44284-025-00240-y).
```

The primary risk in inland cities is not flooding — it is **differential settlement**,
the spatial gradient in subsidence rate that strains buildings and infrastructure even
at modest average rates. Ohenhen et al. estimate more than 29,000 buildings across
these cities sit in high or very high angular distortion hazard zones. San Antonio,
Austin, and Houston account for more than 82% of buildings at very high risk.

👉 Subsidence is not only a coastal problem. In US cities, the more immediate hazard
is often the structural damage that accumulates silently in building foundations,
pipelines, and roads — well before anyone is at risk of flooding.

---

# California's Sinking Coast

California offers an unusually complete picture of how multiple subsidence drivers
interact at the scale of a single state coastline.
[Waters et al. (2020)](https://doi.org/10.1126/sciadv.aba4551) combined ALOS
L-band (2007–2011) and Sentinel-1 (2014–2018) InSAR with 441 GNSS stations to produce
the first continuous VLM map for California's entire ~1,350 km coast at ~100 m
resolution — a roughly 1,000-fold improvement over what GNSS alone could provide.

```{figure} ../figures/13_subsidence_california_vlm.jpg
---
name: California coastal VLM
width: 700px
alt: VLM rate map along California's coast showing broad zones of subsidence and uplift,
     with detail insets for the San Francisco Bay Area, Monterey Bay, Los Angeles, and
     San Diego.
---
VLM rates along the coast of California (2007–2018) from combined ALOS and Sentinel-1
InSAR with GNSS. Negative values (blue) indicate subsidence; positive values (red)
indicate uplift. The map captures both long-wavelength tectonic signals and short-
wavelength anthropogenic signals from groundwater extraction and sediment compaction.
After [Blackwell et al. (2020)](https://doi.org/10.1126/sciadv.aba4551).
```

The spatial pattern reveals the full taxonomy of drivers operating simultaneously:

**Tectonic signals** dominate the long-wavelength pattern. North of Cape Mendocino,
subduction at the Mendocino Triple Junction causes crustal thickening and uplift of
3–5 mm/yr. South of Cape Mendocino, the Pacific–North American plate boundary is
predominantly strike-slip, producing little tectonic uplift. GIA contributes slow
subsidence of up to ~2 mm/yr at latitudes above 37°N.

**Groundwater extraction and recharge** produce the most spatially variable signals.
The clearest examples of each end-member sit within 100 km of each other in the Los
Angeles region: the Ventura basin is subsiding due to groundwater extraction, while the
Santa Ana valley is uplifting at 3–5 mm/yr due to active managed aquifer recharge in
Orange County. This juxtaposition makes Southern California an unusually clean natural
experiment in the elastic response of aquifer systems.

```{figure} ../figures/13_bay_area_vlm.webp
---
name: Bay Area VLM
width: 700px
alt: VLM rate map in the San Francisco bay area showing mostly subsidence.
---
VLMs during 2007-2018 for the San Francisco Bay Area [Blackwell et al. (2020)](https://doi.org/10.1126/sciadv.aba4551).
```

**Sediment compaction** drives subsidence around the major bays. The San Francisco Bay
perimeter subsides at up to −5.9 mm/yr; San Francisco International Airport is sinking
faster than −2 mm/yr due to Bay Mud and landfill compaction. Monterey Bay shows the
fastest coastal rates in the state, reaching −8.7 mm/yr, driven by compaction of
Salinas, Elkhorn, and Pajaro River sediments combined with local faulting.

The population exposure is substantial: **between 4.3 and 8.7 million Californians**
in coastal communities are exposed to subsidence, with the largest numbers in San
Francisco (~460,000–805,000), Los Angeles (~8,500–2,300,000), and San Diego
(~202,000–2,259,000).

👉 The California coast is not uniformly sinking or rising — it is a patchwork
controlled by tectonic setting, sediment type, and water management, often varying
faster than the inter-station spacing of any GNSS network. This is precisely the
observational gap that InSAR fills.

---

# Summary

- Terzaghi's effective stress principle — $\sigma = \sigma' + u$ — governs
  compaction-driven subsidence: groundwater withdrawal reduces pore pressure, increases
  effective stress on the grain skeleton, and causes compaction.
- Elastic compaction (coarse-grained aquifers) is reversible; inelastic compaction
  (fine-grained aquitards) is permanent once effective stress exceeds the preconsolidation
  stress. The geodetic signatures are distinct: elastic compaction produces a seasonal,
  reversible signal; inelastic compaction produces a secular downward trend that does not
  recover with head rebound.
- Subsidence drivers include groundwater extraction, reduced recharge, sediment starvation,
  organic soil oxidation, hydrocarbon and fluid extraction, anthropogenic surface loading,
  and natural compaction. Sea level rise is not a driver of subsidence but determines its
  consequences through relative sea level rise.
- The Central Valley is the best-instrumented example of groundwater-driven subsidence.
  GNSS time series capture the elastic/inelastic decomposition; InSAR reveals spatial
  heterogeneity controlled by Corcoran Clay thickness. Peak rates exceed 60 cm/yr. SGMA
  represents a policy response, but inelastic compaction already committed cannot be undone.
- The Mississippi Delta illustrates the multi-driver case: natural compaction, sediment
  starvation from levee construction, and hydrocarbon extraction all stack. New Orleans now
  lies below sea level in many areas. Relative sea level rise in coastal Louisiana exceeds
  1 cm/yr in the fastest-sinking areas — a compound of subsidence and absolute sea level
  rise.
- Subsidence is widespread in US cities: at least 20% of urban area is sinking in
  every major US metropolis, exposing ~34 million people to VLM-driven hazards.
  Groundwater extraction from confined aquifers explains 76% of the variance in
  observed subsidence rates; the primary risk in inland cities is differential
  settlement and infrastructure damage rather than flooding. Along California's coast,
  4–9 million people are exposed to subsidence driven by a combination of tectonic
  setting, sediment compaction, and groundwater extraction — a spatial patchwork that
  only high-resolution InSAR can resolve.

---
