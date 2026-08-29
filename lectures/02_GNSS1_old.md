# GNSS I: From Satellite Signals to Position

## Purpose

GNSS receivers determine position by measuring signals transmitted from orbiting satellites. In this lecture, we follow the measurement chain from satellite clocks and ranging codes through pseudorange positioning and precise carrier-phase observations.

In this lecture, we will:

- introduce the components of a GNSS system
- explain how signal travel time provides a range measurement
- determine why four satellites are required for positioning
- examine how satellite geometry affects position uncertainty
- distinguish code-based and carrier-phase positioning
- identify the corrections needed to obtain geodetic-quality positions

---

# How Can Satellites Measure the Motion of the Ground?

GNSS is familiar as a navigation tool, but geophysicists use the same basic system to measure motions far smaller than the positioning uncertainty shown on a phone.

GNSS can record:

- tectonic plates moving a few centimeters per year
- permanent displacement during an earthquake
- slow fault slip over days to months
- inflation and deflation of volcanoes
- subsidence caused by groundwater withdrawal

The central question for this lecture is:

> How does GNSS work?

```{figure} ../figures/02_gnss_cascadia.png
---
width: 500px
---
Tectonic setting of northern Cascadia with selected GNSS velocity vectors (thin blue arrows) showing motion with respect to stable North America (UNAVCO, McCaffrey et al., 2013). Juan de Fuca plate motion with respect to North America (DeMets et al., 2010) shown in thick black arrows. Juan de Fuca slab depth contours (Blair et al., 2011) are shown with dotted lines and are 10 km intervals. UTM grid coordinates (m) are in NAD83 UTM Zone 10N.
```

---

# GNSS Is Part of Everyday Infrastructure

Many systems use GNSS even when they do not need to know their location. They use the precise time carried by the satellite signals.

GNSS provides:

- positions for navigation, surveying, and mapping
- timing for seismometers and other scientific instruments
- synchronization for communication, power, and financial systems
- a stable global framework for measuring changes at Earth's surface

Satellite navigation supports much more than directions on a phone.

---

# How Does GPS Determine Your Position?

GPS satellites orbit the Earth while broadcasting coded signals containing:

- the satellite's location in orbit
- the time the signal was transmitted

A receiver compares the transmission and reception times to estimate the distance to each satellite:

$$
\text{distance} \approx \text{travel time} \times \text{speed of light}
$$

Measurements from multiple satellites are then combined to determine the receiver's location through **trilateration**.

```{figure} ../figures/02_gps_trilateration.jpg
---
width: 700px
---
Each satellite constrains the receiver to locations at a particular distance from that satellite. The intersection of several distance constraints determines the receiver's position.
```

---

# A Constellation Provides Global Coverage

GNSS satellites orbit in six planes so that a minimum of four satellites are visible from almost anywhere on Earth.

Orbital period is 1/2 sidereal day.

As the satellites move, different satellites rise and set above the receiver. This provides continuous global coverage rather than positioning from one fixed part of the sky.

There is a coverage hole at the poles where satellites are never directly overhead

```{figure} ../figures/XX_gnss_constellation.png
---
width: 800px
---
GNSS satellites are distributed among multiple orbital planes, allowing several satellites to be observed simultaneously from the Earth's surface.
```

---

# GPS Is One Member of GNSS

**GPS** refers specifically to the satellite-navigation system operated by the United States. **GNSS** is the broader term for global satellite-navigation systems, including:

- GPS: 24+ satellites, 6 orbital planes, 55° inclination, ~20,200 km altitude
- GLONASS: First launched in 1982, full global coverage restored in 2011, Satellites have slightly different frequencies
- Galileo: Civilian-focused, full constellation in 2023
- BeiDou: BeiDou-3 provides global coverage since 2020, earlier versions have preferential coverage over China

Modern receivers can combine signals from multiple constellations. More available satellites can provide:

- better coverage
- stronger geometry
- more observations in obstructed environments
- more robust positioning

Each GNSS system contains three major segments:

- **space segment:** satellites that transmit signals
- **control segment:** ground stations that monitor satellite orbits and clocks
- **user segment:** receivers and processing systems

```{figure} ../figures/02_sky_satellites.png
---
width: 800px
---
Example of satellites visible in Davis, CA at 2 PM PST September 28, 2026.
```

---

# Control Segment (how a satellite knows where it is)

Consists of **Master Control Station (MCS)**, monitoring stations, and ground antennas:

- The MCS computes all the orbitalcorrections needed.
- The monitoring stations track each satellite and have atomic clocks for precise timing.
- The ground antennas upload navigation messages and corrections to the satellites.

```{figure} ../figures/02_control_segment.png
---
width: 800px
---
Control segment sites.
```

---

# A GPS Signal Has Three Layers

A GPS satellite transmits a radio-frequency **carrier wave** containing two types of encoded information:

1. **Ranging code**
   - identifies the satellite
   - provides a recognizable timing pattern
   - allows the receiver to estimate signal travel time

2. **Navigation message**
   - describes the satellite's orbit
   - provides clock corrections
   - reports satellite status

3. **Carrier phase**
   - provides a much more precise measure of changes in range
   - enables geodetic positioning

> The carrier transports the signal, the code provides timing, and the navigation message tells the receiver where the satellite was when the signal was transmitted.

```{figure} ../figures/02_gps_signal_structure.png
---
width: 800px
---
A GPS signal consists of a ranging code and navigation message modulated onto a radio-frequency carrier wave.
```

---

# The C/A Code Identifies and Ranges to a Satellite

The **Coarse/Acquisition (C/A) code** is a pseudorandom sequence available to civilian receivers.

Each satellite transmits a different C/A code, allowing the receiver to distinguish signals arriving from multiple satellites on the same carrier frequency.

The receiver:

1. generates a copy of the satellite's known code
2. shifts its copy in time
3. finds the shift that produces the strongest correlation
4. converts that time shift into an apparent range

The C/A code repeats every millisecond and has a chip rate of 1.023 million chips per second.

One chip corresponds to approximately:

$$
\frac{c}{1.023\times10^6\ \mathrm{chips/s}}
\approx 293\ \mathrm{m/chip}
$$

By matching a fraction of a chip, a receiver can obtain meter-scale range measurements.

```{figure} ../figures/02_ca_code_correlation.png
---
width: 800px
---
The receiver shifts a locally generated copy of the satellite's C/A code until it aligns with the received code. The required time shift provides an estimate of signal travel time.
```

---

# The P-Code Is a More Precise Ranging Code

The **P-code**, originally called the Precision code, has a chip rate ten times faster than the C/A code.

Its shorter effective chip length allows finer code-based range measurements:

- C/A-code chip length: approximately 293 m
- P-code chip length: approximately 29 m

For most users, the P-code is encrypted as the **P(Y) code** and is primarily associated with authorized military applications.

Modern civilian GPS also includes newer ranging codes, such as L2C and signals on L5.

> The P-code improves code-based ranging, but geodetic GNSS obtains its highest precision by measuring the phase of the carrier wave.

```{figure} ../figures/02_ca_p_code.png
---
width: 800px
---
The faster chip rate of the P-code produces shorter chips than the C/A code, allowing finer code-based ranging.
```

---

# The Navigation Message Describes the Satellite

The satellite also transmits a low-rate **navigation message** containing:

- the satellite's orbital parameters, or broadcast ephemeris
- satellite-clock corrections
- satellite health and status
- information about the GPS constellation
- the relationship between GPS time and other time systems

The receiver needs both:

- the **code timing** to estimate the signal's travel time
- the **navigation message** to determine where the satellite was when it transmitted the signal

> Measuring the travel time is useful only if the receiver also knows the satellite's position and clock behavior.

```{figure} ../figures/02_navigation_message.png
---
width: 700px
---
The navigation message provides the orbit and clock information needed to calculate the satellite's position at the time of signal transmission.
```

---

# Basic Positioning

If a signal travels at the speed of light, its apparent range is:

$$
\rho = c\Delta t
$$

where:

- $\rho$ is the measured range
- $c$ is the speed of light
- $\Delta t$ is the signal travel time

One range places the receiver on a sphere centered on the satellite.

Multiple ranges locate the receiver through **trilateration**.

> **Connection:** This resembles locating an earthquake from arrival times. Receiver-clock bias plays a role analogous to the unknown earthquake origin time.

---

## Why Is It a Pseudorange?

The receiver estimates signal travel time by comparing the satellite's transmission time with the receiver's reception time:

$$
P_i=c\left(t_{r,i}^{\mathrm{receiver}}-t_{s,i}^{\mathrm{satellite}}\right)
$$

This is called a **pseudorange** because the satellite and receiver clocks are not perfectly synchronized. The measured travel time therefore does not initially equal the true signal travel time.

The complete code-observation equation also contains propagation delays and other errors:

$$
P_i
=
\rho_i
+
c(\delta t_r-\delta t_i)
+
I_i
+
T_i
+
\epsilon_i
$$

where:

- $\rho_i$ is the true geometric satellite–receiver distance
- $c(\delta t_r-\delta t_i)$ represents receiver- and satellite-clock errors
- $I_i$ is the ionospheric propagation delay
- $T_i$ is the tropospheric propagation delay
- $\epsilon_i$ includes multipath, hardware biases, and measurement noise

> Clock errors affect our measurement of **when** the signal traveled; atmospheric delays affect **how long the signal actually took** to travel.

---

## Why Are Four Satellites Required?

The unknowns are:

- receiver $x$ coordinate
- receiver $y$ coordinate
- receiver $z$ coordinate
- receiver-clock bias

At least four independent satellite observations are therefore required.

With more than four satellites, the overdetermined system can be solved using least squares.

---

# Satellite Geometry and Dilution of Precision

Position accuracy depends on both:

- measurement accuracy
- satellite geometry

Satellites distributed broadly across the sky provide stronger constraints than satellites clustered in one direction.

**Low dilution of precision:** favorable geometry and smaller position uncertainty.

**High dilution of precision:** poor geometry and amplified position uncertainty.

The vertical component is usually less precise.

---

# Navigation and Geodesy Use the Same Signals

An everyday receiver can determine its location within seconds, but meter-scale positioning is not sufficient to measure tectonic motion.

Geodetic GNSS uses the same satellite signals with different observations, longer recording periods, and more sophisticated processing to achieve millimeter- to centimeter-scale precision.

> How do we transform a navigation measurement into a geodetic measurement?

```{figure} ../figures/XX_navigation_to_geodesy.png
---
width: 800px
---
Navigation and geodetic GNSS use the same satellite signals but achieve different levels of precision through different observations and processing methods.
```

---

# Carrier Phase Provides Millimeter-Scale Sensitivity

Code ranging is not sufficiently precise for measuring tectonic deformation:

- C/A-code positioning: meter-scale
- P-code positioning: decimeter-scale
- carrier-phase measurement: millimeter-scale sensitivity

After identifying a satellite and aligning its pseudorandom code, the receiver tracks the phase of the underlying carrier wave.

The L1 carrier has a wavelength of approximately 19 cm. Measuring \(1\%\) of a carrier cycle corresponds to:

$$
0.01 \times 19\ \mathrm{cm}
\approx 2\ \mathrm{mm}
$$

However, the receiver does not initially know the total number of complete carrier cycles between the satellite and receiver:

$$
\rho = \lambda(N+\phi)
$$

where \(N\) is the unknown **integer ambiguity** and \(\phi\) is the measured fractional phase.

```{figure} ../figures/02_carrier_phase_tracking.png
---
width: 800px
---
Code correlation provides an approximate range and identifies the satellite. Tracking the shorter-wavelength carrier phase provides millimeter-scale sensitivity, but the total number of complete carrier cycles is initially unknown.
```

---

# Precise Positioning Requires Long Observations

A geodetic receiver records signals continuously as multiple satellites move across the sky.

Observing for many hours provides:

- measurements from many satellite directions
- changing satellite–receiver geometry
- repeated observations of the station position
- information needed to separate atmospheric delays from station position
- continuity for tracking carrier cycles and resolving integer ambiguities

A geodetic station therefore combines:

- a stable monument
- a calibrated antenna
- a high-quality receiver
- continuous observations from multiple satellites and frequencies

> The trade-off is time: navigation provides a meter-scale position within seconds, whereas geodetic processing combines hours of observations to obtain millimeter- to centimeter-scale positions.

```{figure} ../figures/02_satellite_sky_tracks.png
---
width: 700px
---
Satellite tracks recorded over many hours provide observations across a wide range of directions and elevation angles, improving position estimates and helping separate atmospheric delays from station motion.
```

---

# Precise Positioning Solves for Position and Errors Together

Carrier phase provides a precise measurement, but it contains contributions from the satellite, atmosphere, receiver, and measurement system.

Precise processing combines:

- carrier-phase observations
- precise satellite orbits and clock corrections
- multiple frequencies to reduce ionospheric delay
- models or estimates of tropospheric delay
- antenna calibrations
- integer-ambiguity and cycle-slip corrections
- observations from many satellites over time

Two common processing strategies are:

- **Precise Point Positioning:** uses precise orbit and clock products to estimate a station's position in a global reference frame
- **Relative positioning:** compares simultaneous observations at multiple stations so that shared errors cancel

The result is an estimate of the station's three-dimensional position—commonly one position per day—in a specified reference frame.

```{figure} ../figures/02_precise_positioning_workflow.png
---
width: 800px
---
Precise GNSS processing combines carrier-phase observations with satellite, atmospheric, antenna, and ambiguity corrections to estimate a station position in a defined reference frame.
```

---

# GNSS I Summary

GNSS positioning begins with signal travel times from satellites to a receiver.

Because receiver-clock bias is unknown, at least four satellites are required to determine a three-dimensional position.

Code observations provide meter-scale positions, while carrier-phase observations provide the precision needed to observe crustal deformation.

Achieving geodetic precision requires favorable satellite geometry, long observations, ambiguity resolution, precise orbit and clock products, and atmospheric corrections.

---

## Laboratory

Students will use the Simple Point Positioning section of the CRESCENT Fundamentals notebook to:

- calculate pseudoranges for a simulated receiver
- solve for receiver position and clock bias
- compare the recovered and true positions
- change satellite geometry
- quantify how geometry changes dilution of precision and position error

Do not assign the complete notebook. Sections 2–4 can be demonstrated briefly, while §§6–8 are optional extensions.
