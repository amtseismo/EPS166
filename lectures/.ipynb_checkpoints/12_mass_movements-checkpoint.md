# Monitoring Mass Movements: *Why Slopes Fail And How We Study Them*


## Purpose


Mass Movements are an extreme component of mass wasting, the process of landscape evolution by which material is weathered and moved downhill.

In this lecture, we'll discuss:

- what mass movements are,
- the mechanics of slope failure,
- what triggers mass movements, and
- how we can monitor mass movements.

---

In recent decades, compounding climate shifts have led to both accelerated mass wasting in mountainous regions and to increasingly large and destructive mass movement events.

Altered climate process include:

1. Deglaciation
2. Permafrost degradation
3. Wildfire severity and extent
4. Increases in precipitation

The lecture slides show some example events like the 2025 Blatten Glacier Collapse, the 2010 Mt. Meager Landslide, and the 2025 Tracy Arm Landslide and Tsunami.

---

## Mass Movements: Gravity-driven deformation

Erosion removes weathered material from its source. Mass movements are the downslope movement of soil, rock, or debris
driven by gravity. These events are not caused by flowing water, ice, or wind, although these can be triggering factors. Instead mass movements occurs when gravity is greater than slope strength.


```{figure} ../figures/12_massmovements.png
---
width: 500px
alt: USGS diagram of mass movements.
---
Diagram showing various mass movement ranging from falls, slides, and flows for both rock masses and unconsolidated debris. Source: USGS
```

These events can range from slow soil creep to catastrophic landslides.


---

## Why do slopes fail?

Slopes fail when the driving stresses exceed the resisting forces of the slope.

```{figure} ../figures/12_slopeforces.png
---
width: 500px
alt: Diagram showing slope forces acting on a mass.
---
Comparison of unstable and stable slope forces acting on a mass block. When driving forces or shear stresses are larger than resistance or shear strength, the slope fails. If the resistance is larger than the driving forces, the slope is stable.
```

Driving stresses are controlled by:

1. Gravity
2. Slope Angle
3. Material Mass

Resisting forces are:

1. Friction
2. Cohesion
3. Effective Normal Stress


---

## How do we classify mass movements?

Generally, four classifications of movement - rock flows, rock slides/falls, debris flows, and debris slides/falls. Events are then sorted by velocity of the movement which can range from cm/year in the cases of processes like creep to km/hour for rockfalls or avalanches.

```{figure} ../figures/12_eventtypes.png
---
width: 500px
alt: Diagram showing the different types of mass movements sorted on a scale of velocity and flow classification.
---
Mass movements can primarily be sorted by material type -- rock and unconsolidated material. Each material type can fail either as a flow or as a slide/fall. Then events are characterized by the velocity ranging from slow events (cm/year) like creep to fast (km/hour) like avalanches or rock falls.
```

**Slides vs. Flows**

Mass movements can be classified as slides or flows. Slides involve a coherent block or mass. The failure can be rotational or translational depending on the rupture surface. 

```{figure} ../figures/12_slides.png
---
width: 500px
alt: Diagram showing rotational and translational slides.
---
In slides, the slope deforms as a coherent mass that moves along a shear plane. In rotational slides, the shear plane is concave and the slope deforms by rotating. In translational slides, the shear plane is flat and the mass deforms by sliding along this plane.
```

In contrast in a flow, the mass loses internal cohesion and acts as a fluid or slurry and has no rupture surface.

```{figure} ../figures/12_flows.png
---
width: 500px
alt: Diagram showing flow-type mass movements like earthflows and creep.
---
In flows, the mass instead loses all internal structure and therefore flows over the slope like a fluid. These processes can be nearly instantaneous like earthflows, that move on the scale of m/s over minutes to hours, or prolonged processes like creep, that move cm/yr over decadal time scales.
```

Timelines of failure can vary significantly and slope deformation can evolve over time in a process known as **progressive failure**. In this process, displacement slowly accelerates over a longer time-scale eventually leading to slope failure. Progressive failure can arrest howver and not all events end in catastrophic failure.

```{figure} ../figures/12_failure.png
---
width: 500px
alt: Diagram showing the displacement curve of progressive failure over time.
---
Progressive failure builds over time. Initially displacement is slow with a relatively slow and stable rate of motion. As the shear surface develops and slope forces change, the slope can begin to accelerate. Once the deformation caused by this acceleration has accumulated and system forces have changed, the slope can catastrophically fail.
```

Slopes deformation can occur slowly over years/decades/centuries. When deformation becomes concentrated on a shear surface, this leads to increasing instability and can cause an acceleration in slope displacement.

Accelerating movement can indicate approaching instability, but does not always lead to catastrophic failure.

---

## What forces act on a slope?

```{figure} ../figures/12_forces.svg
---
width: 500px
alt: Diagram showing overall slope forces.
---
There are two main forces acting on a mass on a slope: the gravity force (black) and the resistance forces (green). Because the mass sits on a slope, the gravity force can further be translated into a slope parallel force (red) and the slope perpendicular or normal force (blue).
```

The main force acting on a mass ($m$) on a slope is *gravity*:

$$
W = m g sin\theta
$$

Slope angle ($\theta$) plays a major role in how much of the gravitational force becomes a downslope driving force: 

$$
F_{||} = m g sin\theta
$$

The resisting force ($F_r$) is a combination of cohesion ($c$), slip area ($A$), and friction:

$$
F_r = c'A+ N′ tan\phi′
$$

which means resistance is dependent on the effective normal force ($N'$) and the friction angle ($tan\phi'$).


**What influences gravitational stress?**))

```{figure} ../figures/12_impactsgravity.png
---
width: 500px
alt: Diagram showing how gravitational stress changes with three factors.
---
This diagram shows how slope angle ($\theta$), material density ($\rho$), and depth to failure plane ($z$) impact the gravitational force acting on a mass on a slope.
```

For a simplified slope model, gravitational shear stress ($\tau$) is:

$$
\tau = \rho g z sin\theta cos\theta
$$

This means gravitational stress is dependent on:
1. *Slope Angle ($\theta$)* -- A steeper slope means increased sliding
2. *Material Density ($\rho$)* -- Denser material means more gravitational loading
3. *Depth to Failure Plane ($z$)* -- Greater overlying material thickness means higher gravitational stress


**The Resistance Forces: Cohesion and Friction**

The Mohr-Coulomb Failure Criterion defines shear strength ($\tau_f$):

$$
\tau_f = c' + \sigma_n' tan\phi'
$$

where $c'$ is effective cohesion, $\sigma_n'$ is the effective normal stress, and $\phi'$ is the internal friction angle.

Effective cohesion is the component of shear stress not dependent on normal stress and represents the bonding or cementation between particles. Internal friction is the resistance to sliding between particles and surfaces. Friction is dependent on material properties. Frictional strength also increases with normal stress.

**What are some ways to reduce cohesion or friction on a slope?**

1. Weathering, fracturing, cracking
2. Saturation, increase in pore pressure, groundwater fluctuations 
3. Material alteration
4. Clay mineral formation
5. Grain crushing
6. Shear localization or progressive deformation
7. Loss of organic root material
8. And more…

**Effective Stress and Pore Pressure**

One of the most common ways to trigger slope failure is increasing pore pressure. This is because effective normal stress ($\sigma_n'$) is dependent on pore pressure ($p$):

$$
\sigma_n' = \sigma_n - p
$$

What causes pore pressure to increase?
- Rainfall infiltration
- Rapid loading (ex., earthquake shaking)
- Groundwater changes


**Factor of Safety – Is a slope stable?**

Factor of Safety ($𝐹𝑆$) is the ratio of resisting shear strength to driving stress:

$$
FS = \frac{Resisting shear strength}{Driving shear stress} = \frac{c' + (\rho g z cos^2 \theta - p) tan\phi'}{\rho g z sin\theta cos\theta}
$$

- If $FS$ < 1, the slope is unstable (driving stress exceeds strength).
- If $FS$ > 1, the slope is stable (strength exceeds driving stress).
- If $FS$ = 1, the slope is on the threshold of failure.

What changes $FS$?
- $FS$ will decrease if slope angle ($\theta$) or pore pressure ($p$) increases.
• $FS$ will increasing FS if cohesion ($c$) increases or the friction angle ($\phi$) becomes larger.


---

## What triggers a mass movement?

```{figure} ../figures/12_hubbard.jpg
---
width: 500px
alt: Post-earthquake InSAR image of the aftermath of the Hubbard Glacier earthquake 2025
---
InSAR image of Hubbard Glacier, McArthur Peak, and Mount King George in SW Yukon taken on 08 December 2025. The image shows the aftermath of the 06 December 2025 Hubbard Glacier Earthquake which triggered 200 individual landslides as well as snow and ice avalanches and the collapse of glacial features. Source: NASA
```

Some processes that can trigger mass movements include (but are not limited to):

- **Heavy rainfall** – adds weight and reduces friction in soil and rock
- **Earthquakes** – dynamic triggering by shaking slopes, causing loose material to move
- **Volcanic eruptions** – melt snow and ice, creating fast-moving debris flows
- **Human activity** – road cuts, deforestation, or oversteepening slopes
- **Freeze–thaw cycles** – loosen rock and soil over time
- **Outburst floods** – rapid addition of water to the slope system

**How does rainfall induce slope failure?**

1. *Increased pore pressure* - Rainfall infiltrates and raises groundwater levels. It also increases positive pore pressure which decreases effective normal stress and reduces friction.
2. *Loss of matric suction* - Infiltration reduces suction between soil particles as soils become wetter. This destabilizes shallow slopes where the water infiltrates.
3. *Increased gravitation loading* - Water has weight and therefore increases bulk density. Saturated materials weigh more. This extra mass increases gravitational loading.
4. *Increased overland flow* - Some slope processes like debris flows, require significant surface water and overland flow. This flow can entrain slope mass and sediments.

```{figure} ../figures/12_montecito.jpg
---
width: 500px
alt: Before and after image of the 2018 Montecito debris flows.
---
The Montecito Debris Flows in 2018 occured as the result of intense rainfall. This event was a classic example of a post-wildfire debris flow. Source: CNN
```

**How do earthquakes induce slope failure?**

1. Dynamic Loading
- Seismic waves produce transient ground accelerations
- These temporarily increase downslope stress
2. Cyclic weakening and progress damage
- Repeated shaking can cause deformation and fracturing
- Reduces cohesion and soil strength
3. Excess pore pressure and liquefaction
- Loading of saturated soils can generate excess pore pressure
- Increasing pore pressure reduces normal stress and friction
- In susceptible soils, liquefaction can cause loss of shear strength.

---

## How does a landslide develop over time?

```{figure} ../figures/12_progressivefailure.png
---
width: 500px
alt: Image showing the three stages of progressive slope failure.
---
Diagram showing the stages of progressive slope failure which include: (1) localized damage where damage is discontinuous, (2) shear zone propagation where damage begins to develop in adjacent regions, and (3) slope-scale instability where the failure surface has become complete and where the damage is slope-wide.
```

1. *Starts with localized deformation*: Small fractures or shear zones develop where there is concentrated stress. This deformation is limited to discontinuous portions of slope.
2. *Progressive weakening and stress redistribution*: As the slope continues to weaken and fracture, localization takes place. Stresses redistribute from discontinuous to adjacent regions and a shear surface begins to propagate although it has not yet fully developed.
3. *Slope-scale instability*: Once localized failure zones connect to form continuous slip surface, the entire slope is now unstable and can now transition from slow deformation to rapid movement.

---

## How do we measure slope deformation?

Four main techniques for monitoring mass movements:

1. **GNSS**: GNSS can be used to provide a time-series of displacement of a slope at specific spatial points which can track slow movement and accelerating displacement over time.
2. **LiDAR or InSAR**: If the goal of monitoring is spatially extensive measurments of surface deformation, both LiDAR and InSAR can provide these measurment down to cm-scale depending on data quality. These measurment systems do not provide a record of displacement over time and often have poor temporal resolution, with days or months of deformation taking place between data aquisitions. These methods are particularly helpful for identifying slow-moving landslides or for pre- and post-event analysis.
3. **Extensometers and Tiltmeters**: These instruments can provide a record of the distance of displacement over cracks or the changes in ground inclination over time. Like GNSS they provide a constant time-series of data and can be used to detext and track localized deformation within a slope.
4. **Seismic Monitoring**: Seismic monitoring can be used to detect the ground deformations associated with fracturing, sliding, and moving debris. It has high temporal resolution. This data is useful for stuyding rapid movements and provides an active record of event dynamics.

```{figure} ../figures/12_monitoring.png
---
width: 500px
alt: Examples of different mass movement monitoring methods.
---
Examples of the four different monitoring methods mentioned above: GNSS - point monitoring, InSAR - spatial displacement, Extensometer - relative point displacement, and Seismic - active ground vibration.
```

---

## Key Takeaways from this Lecture:

1. Slopes fail when their driving stresses (gravity, slope angle, material mass) exceed their resisting stresses (friction, cohesion, effective normal stress).
2. Slope failures can be triggered by a plethora of events like rainfall, earthquakes, volcanic eruptions, and human activity.
3. Both pre-failure and post-failure deformation can be monitored and assessed using LiDAR, InSAR, and other geodetic methods.


