# GNSS I: From Satellite Signals to Position

## Purpose

GNSS receivers determine position by measuring signals transmitted from orbiting satellites. In this lecture, we follow the measurement chain from satellite clocks and ranging codes through pseudorange positioning and precise carrier-phase observations.

In this lecture, we will:

- introduce the components of a GNSS system
- explain how signal travel time provides a range measurement
- determine why four satellites are required for positioning
- distinguish code-based and carrier-phase positioning
- identify the corrections needed to obtain geodetic-quality positions

---

# GNSS

## How Can Satellites Measure the Motion of the Ground?

Global Navigation Satellite Systems (GNSS) is familiar as a navigation tool, but geophysicists use the same basic system to measure motions far smaller than the positioning uncertainty shown on a phone.

GNSS can record:

- tectonic plates moving a few centimeters per year
- permanent displacement during an earthquake
- slow fault slip over days to months
- inflation and deflation of volcanoes
- subsidence caused by groundwater withdrawal

The central question for this lecture is:

> How does GNSS work?

```{figure} ../figures/01_gnss_cascadia.png
---
width: 500px
alt: Map of northern Cascadia showing GNSS velocities directed northeast near the coast and decreasing toward the continental interior.
---
Tectonic setting of northern Cascadia with selected GNSS velocity vectors (thin blue arrows) showing motion with respect to stable North America (UNAVCO, McCaffrey et al., 2013). Juan de Fuca plate motion with respect to North America (DeMets et al., 2010) shown in thick black arrows. Juan de Fuca slab depth contours (Blair et al., 2011) are shown with dotted lines and are 10 km intervals. UTM grid coordinates (m) are in NAD83 UTM Zone 10N.
```

---

## GNSS Is Part of Everyday Infrastructure

Many systems use GNSS even when they do not need to know their location. 

GNSS provides:

- positions for navigation, surveying, and mapping
- timing for seismometers and other scientific instruments
- synchronization for communication, power, and financial systems
- a stable global framework for measuring changes at Earth's surface

Satellite navigation supports much more than directions on a phone.

---

## How Does GNSS Determine Your Position?

**GNSS** satellites orbit the Earth while broadcasting coded signals containing:

- the satellite's location in orbit
- the time the signal was transmitted

A receiver compares the transmission and reception times to estimate the distance to each satellite:

$$
\text{distance} \approx \text{travel time} \times \text{speed of light}
$$

Measurements from multiple satellites are then combined to determine the receiver's location through **trilateration**.

```{figure} ../figures/01_gps_trilateration.jpg
---
width: 700px
---
Each satellite constrains the receiver to locations at a particular distance from that satellite. The intersection of several distance constraints determines the receiver's position.
```

---

## GPS Is One Member of GNSS

**GPS** refers specifically to the satellite-navigation system operated by the United States. **GNSS** is the broader term for global satellite-navigation systems, including:

- **GPS**: 24+ satellites, 6 orbital planes, 55° inclination, ~20,200 km altitude
- **GLONASS**: First launched in 1982, full global coverage restored in 2011, Satellites have slightly different frequencies
- **Galileo**: Civilian-focused, full constellation in 2023
- **BeiDou**: BeiDou-3 provides global coverage since 2020, earlier versions have preferential coverage over China

Modern receivers can combine signals from multiple constellations. More available satellites can provide:

- better coverage
- stronger geometry
- more observations in obstructed environments
- more robust positioning

Each GNSS system contains three major segments:

- **space segment:** satellites that transmit signals
- **control segment:** ground stations that monitor satellite orbits and clocks
- **user segment:** receivers and processing systems

```{figure} ../figures/01_sky_satellites.png
---
width: 800px
---
Example of satellites visible in Davis, CA at 2 PM PST September 28, 2026.
```

---

## The GPS Constellation Provides Continuous Coverage

The nominal GPS constellation places at least 24 satellites in **six orbital planes**, allowing at least four satellites to be observed from almost anywhere on Earth.

Each satellite orbits:

- at an altitude of approximately **20,200 km**
- with an inclination of **55°**
- once every **half sidereal day**, or approximately 11 hours 58 minutes

Because each satellite completes two orbits while Earth rotates once relative to the stars, its path across the sky repeats approximately once per sidereal day. This makes satellite coverage and geometry predictable.

The 55$^\circ$ inclination is a compromise that provides broad global coverage without requiring polar orbits. GPS satellites never pass directly over the poles, but they remain visible above the horizon at polar locations.

As the satellites rise and set, receivers observe signals from different directions, providing continuous coverage and changing satellite geometry.

```{figure} ../figures/01_gnss_constellations.png
---
width: 800px
alt: Orbits of active global and regional navigation satellites
---
Orbits of active global and regional navigation satellites [GGOS](https://geodesy.science/ggos/products/gnss-orbits-clocks-biases/)
```

---

## Control Segment (how a satellite knows where it is)

Consists of **Master Control Station (MCS)**, monitoring stations, and ground antennas:

- The MCS computes the orbital corrections needed.
- The monitoring stations track each satellite and have atomic clocks for precise timing.
- The ground antennas upload navigation messages and corrections to the satellites.

```{figure} ../figures/01_control_segment.png
---
width: 800px
---
Control segment sites.
```

---

# The GPS Signal

A GPS signal combines three components:

1. **Carrier wave**
   - transports the signal through space
   - oscillates at a precisely controlled radio frequency

2. **Pseudorandom noise (PRN) code**
   - identifies the transmitting satellite
   - provides a recognizable timing pattern
   - allows the receiver to estimate signal travel time

3. **Navigation message**
   - describes the satellite's orbit and clock
   - provides the information needed to calculate satellite position

```{figure} ../figures/01_gps_signal_structure.jpg
---
width: 800px
---
A GPS signal consists of a ranging code and navigation message modulated onto a radio-frequency carrier wave. [GNSS Decoded: GPS Signal Structure](https://gnssdecoded.com/gps-signal-structure/)
```

---

## The Carrier Wave

The **carrier wave** is the high-frequency radio signal that transports GPS information through space.

GPS carrier frequencies are derived from a fundamental frequency of **10.23 MHz**, maintained by the satellite's atomic clocks. This precisely controlled frequency provides the timing stability required for positioning.

GPS satellites transmit in three primary frequency bands:

| Band | Frequency | Wavelength | Primary role |
| --- | ---: | ---: | --- |
| **L1** | 1575.42 MHz | 19 cm | Primary civilian and military signals |
| **L2** | 1227.60 MHz | 24 cm | Additional civilian and military signals; dual-frequency correction |
| **L5** | 1176.45 MHz | 25 cm | Modern civilian safety-of-life and high-performance applications |

The unmodulated carrier does not identify the satellite or describe its orbit. The **PRN code** and **navigation message** must be encoded onto it to provide that information.

Using observations from the same satellite on multiple frequencies allows the receiver to estimate and remove most of the frequency-dependent ionospheric delay.

---

## PRN code (C/A Code)

The **Coarse/Acquisition (C/A) code** is a pseudorandom sequence available to civilian receivers.

Each satellite transmits a different 1,023-chip C/A code, allowing the receiver to distinguish signals arriving from multiple satellites on the same carrier frequency.

This is **code-division multiple access (CDMA)**: all satellites can share the L1 frequency because each one transmits a different PRN code.

The receiver:

1. generates a copy of the satellite's known code
2. shifts its copy in time
3. finds the shift that produces the strongest correlation
4. converts that time shift into an apparent range

The C/A code repeats **every millisecond** and has a chip rate of 1.023 million chips per second.

One chip corresponds to approximately:

$$
\frac{c}{1.023\times10^6\ \mathrm{chips/s}}
\approx 293\ \mathrm{m/chip}
$$

By matching a fraction of a chip, a receiver can obtain meter-scale range measurements.

---

## PRN code (P-Code)

The **P-code**, originally called the Precision code, has a chip rate ten times faster than the C/A code.

Its shorter effective chip length allows finer code-based range measurements:

- C/A-code chip length: approximately 293 m
- P-code chip length: approximately 29 m

For most users, the P-code is encrypted as the **P(Y) code** and is primarily associated with authorized military applications.

Modern civilian GPS also includes newer ranging codes, such as L2C and signals on L5.

---

## The Navigation Message Describes the Satellite

The satellite also transmits a **navigation message** at only **50 bits per second**.

It contains:

- the satellite's orbital parameters, or broadcast ephemeris
- satellite-clock corrections
- satellite health and status
- an almanac containing coarse orbit information for the constellation
- GPS time and related correction parameters

The receiver needs both:

- the **code timing** to estimate the signal's travel time
- the **navigation message** to determine where the satellite was when it transmitted the signal

> Measuring the travel time is useful only if the receiver also knows the satellite's position and clock behavior.

```{figure} ../figures/01_nm_frame.jpeg
---
width: 700px
---
The navigation message contains subframes that hold different types of information. Subframe 1 (Clock Correction & Satellite Health): Contains the GPS week number, satellite clock corrections, and satellite health status. This information is updated frequently and is critical for computing accurate pseudoranges. Subframes 2 & 3 (Ephemeris Data): Provide the precise orbital parameters for the transmitting satellite. This ephemeris data is valid for 2-4 hours and allows the receiver to calculate the satellite’s position to within a few meters. Ephemeris data is essential for accurate positioning. Subframes 4 & 5 (Almanac, Ionospheric Model, & UTC Parameters): Contain coarse orbital information (almanac) for all GPS satellites, ionospheric correction model parameters, and UTC time correlation. The almanac allows the receiver to predict which satellites should be visible and aids in rapid satellite acquisition. Because subframes 4 and 5 contain data for all satellites, it takes 25 frames (12.5 minutes) to transmit the complete almanac. [GNSS Decoded: GPS Signal Structure](https://gnssdecoded.com/gps-signal-structure/)
```

```{figure} ../figures/01_nm_structure.jpeg
---
width: 700px
---
The navigation message contains subframes that hold different types of information. [GNSS Decoded: GPS Signal Structure](https://gnssdecoded.com/gps-signal-structure/)
```
---

## The Code and Data Modulate the Carrier

The navigation data and PRN code are first combined into a single binary sequence.

That sequence is placed onto the carrier using **binary phase-shift keying (BPSK)**:

- one binary state leaves the carrier unchanged
- the other reverses the carrier phase by $180^\circ$

The receiver knows the PRN sequence and uses these phase reversals to find and identify the satellite signal.

After acquisition, the receiver removes the known code and navigation-data modulation and tracks the underlying carrier phase.

> Note that a navigation bit remains constant over many complete transmissions of the C/A-code sequence.

```{figure} ../figures/01_modulation.png
---
width: 800px
---
The combined PRN code and navigation data modulate the carrier by reversing its phase. A receiver removes the known modulation before tracking the underlying carrier phase. [GNSS Decoded: GPS Signal Structure](https://gnssdecoded.com/gps-signal-structure/)
```

---

# Basic Positioning

```{figure} ../figures/01_signal_reception.jpeg
---
width: 800px
---
Steps involved in GPS signal creation, transmission, and reception. [GNSS Decoded: GPS Signal Structure](https://gnssdecoded.com/gps-signal-structure/)
```

---

## Signal Reception

For each possible satellite, the receiver:

- generates a local copy of the satellite's known PRN code
- searches across possible code-arrival times and Doppler-shifted frequencies
- cross-correlates the local code with the received signal

A strong correlation peak indicates that the receiver has detected the satellite and estimated the arrival time of its code.

---

## Code Ranging Produces a Pseudorange

After acquiring a satellite, the receiver measures the PRN code's arrival-time offset.

With perfectly synchronized clocks and no propagation delays, signal travel time would give the geometric range:

$$
\rho_i=c\Delta t_i
$$

In reality, the measured code range also contains clock errors, atmospheric delays, and other biases. It is therefore called a **pseudorange**:

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

- $P_i$ is the measured pseudorange
- $\rho_i$ is the true geometric satellite–receiver distance
- $\delta t_r$ and $\delta t_i$ are receiver- and satellite-clock errors
- $I_i$ and $T_i$ are ionospheric and tropospheric delays
- $\epsilon_i$ includes multipath, hardware biases, and measurement noise

Each pseudorange constrains the receiver to an apparent distance from one satellite. Pseudoranges from multiple satellites are combined to estimate receiver position and clock bias.

> **Connection:** This resembles locating an earthquake from arrival times: receiver-clock bias plays a role analogous to the unknown earthquake origin time.

---

## Why Are Four Satellites Required?

To determine a users location, the unknowns are:

- receiver $x$ coordinate
- receiver $y$ coordinate
- receiver $z$ coordinate
- receiver-clock bias

At least four independent satellite observations are therefore required but even more observations reduce uncertainty.

With four or more satellites, the overdetermined system can be solved using least squares and you can estimate a position.

---

## Satellite Geometry and Dilution of Precision

Position accuracy depends on both:

- measurement accuracy
- satellite geometry

Satellites distributed broadly across the sky provide stronger constraints than satellites clustered in one direction.

**Low dilution of precision:** favorable geometry and smaller position uncertainty.

**High dilution of precision:** poor geometry and amplified position uncertainty.

The vertical component is usually less precise.

---

## Navigation and Geodesy Use the Same Signals

An everyday receiver can determine its location within seconds, but meter-scale positioning is not sufficient to measure tectonic motion.

Geodetic GNSS uses the same satellite signals with different observations, longer recording periods, and more sophisticated processing to achieve millimeter- to centimeter-scale precision.

> How do we transform a navigation measurement into a geodetic measurement?

```{figure} ../figures/01_bml_gps.jpg
---
width: 500px
---
Earthscope GPS site at the UC Davis Bodega Marine Laboratory.
```

---
# Precise Positioning

## Carrier Phase Provides Precision—but Not a Unique Range

Code measurements provide an approximate range, but they are not precise enough to measure small tectonic motions.

| Observation | Typical measurement precision | Primary role |
| --- | ---: | --- |
| **C/A code** | meters | satellite identification and coarse ranging |
| **P(Y) code** | decimeters | finer code ranging for authorized users |
| **Carrier phase** | millimeter-scale sensitivity | precise changes in satellite–receiver distance |

After acquiring a satellite, the receiver removes the known code and navigation-data modulation and tracks the phase of the carrier relative to a locally generated signal.

For the L1 carrier, the wavelength is approximately 19 cm. Measuring the phase to \(1\%\) of a cycle corresponds to:

$$
0.01 \times 19\ \mathrm{cm}
\approx 2\ \mathrm{mm}
$$

The receiver can measure the **fractional phase** very precisely, but it does not initially know how many complete wavelengths lie between the satellite and receiver:

$$
\rho = \lambda(N+\phi)
$$

where:

- $\lambda$ is the carrier wavelength
- $\phi$ is the measured fractional phase, expressed in cycles
- $N$ is the unknown number of complete cycles—the **integer ambiguity**

> Carrier phase is an extremely precise ruler, but the receiver must determine which cycle it is measuring before it can obtain a precise range.

```{figure} ../figures/01_carrier_phase_tracking.webp
---
width: 600px
---
Code correlation provides an approximate range and identifies the satellite. Tracking the shorter-wavelength carrier phase provides millimeter-scale sensitivity, but the total number of complete carrier cycles is initially unknown.
```

---

# Repeated Observations Constrain the Integer Ambiguity

Each tracked satellite has its own ambiguity, \(N_i\).

As a satellite moves across the sky:

- the satellite–receiver distance changes
- the measured fractional phase changes
- the viewing geometry changes
- \(N_i\) remains constant as long as the receiver maintains signal lock

The receiver can therefore track changes in range extremely precisely even before it knows the absolute number of cycles.

Combining observations from many satellites and times constrains:

- station position
- receiver clock
- atmospheric delays
- the ambiguity associated with each satellite

Depending on the processing strategy, ambiguities may be estimated as continuous values or resolved to integers.

If the receiver loses signal lock, it may lose count of one or more cycles. This produces a **cycle slip**, requiring a new ambiguity to be estimated.

> The ambiguity is unknown but constant; the changing geometry supplies new constraints on that same unknown.

---

## Long Observations Improve More Than Ambiguity Resolution

A geodetic receiver continuously records signals from multiple satellites as they move across the sky.

Observing for many hours provides:

- changing satellite–receiver geometry
- more observations than unknown parameters
- continuity for tracking carrier cycles
- stronger constraints on integer ambiguities
- observations at different elevation angles
- information for separating tropospheric delay from station position
- averaging of some random measurement noise

Continuous tracking is particularly important. As long as the receiver maintains lock, it can count changes in carrier cycles even before the initial integer ambiguity has been resolved.

A geodetic station therefore combines:

- a stable monument
- a calibrated antenna
- a high-quality multifrequency receiver
- continuous observations from many satellites

> Navigation emphasizes obtaining a position quickly. Geodetic GNSS emphasizes collecting enough precise, geometrically varied observations to distinguish position from ambiguity, atmospheric delay, and other errors.

---

## Precise Positioning Solves for Position and Errors Together

A carrier-phase observation contains the precise geometric range along with several unknown contributions:

$$
\Phi_i
=
\rho_i
+
c(\delta t_r-\delta t_i)
-
I_i
+
T_i
+
\lambda N_i
+
\epsilon_i
$$

Precise processing combines observations from many satellites and times with:

- precise satellite orbits and clock corrections
- multiple frequencies to estimate or remove ionospheric delay
- estimates of tropospheric delay
- antenna phase-center calibrations
- integer-ambiguity estimation
- detection and correction of cycle slips

Two common processing strategies are:

- **Precise Point Positioning:** uses precise satellite orbit and clock products to estimate a station position in a global reference frame
- **Relative positioning:** combines simultaneous observations from multiple stations so that many shared errors cancel or are reduced

The result is an estimate of the station's three-dimensional position in a specified reference frame—commonly one position for each day of observations.

---

# From Radio Signals to Crustal Motion

GNSS positioning begins by measuring signals traveling from satellites to a receiver.

- **Code observations** identify satellites and provide approximate absolute ranges.
- **At least four satellites** are needed to solve for three-dimensional position and receiver-clock bias.
- **Carrier-phase observations** measure fractional cycles with millimeter-scale sensitivity.
- **Integer ambiguities** represent the initially unknown number of complete carrier cycles.
- **Long, continuous observations** provide the changing geometry needed to constrain position, atmospheric delays, and ambiguities.
- **Precise processing** combines the observations with orbit, clock, atmospheric, and antenna information.

The final product is not usually a tectonic velocity. It is a sequence of station positions:

$$
\text{satellite signals}
\longrightarrow
\text{daily positions}
\longrightarrow
\text{position time series}
\longrightarrow
\text{crustal deformation}
$$

> In the next lecture, we will examine how daily GNSS positions are transformed into velocities, offsets, seasonal signals, and transient deformation.

---

# Laboratory: From Pseudoranges to Position

Students will use the **Simple Point Positioning** section of the CRESCENT GNSS Fundamentals notebook to:

- calculate pseudoranges for a simulated receiver
- solve for receiver position and clock bias
- compare the recovered and true positions
- change the satellite geometry
- quantify how geometry affects dilution of precision and position error

The laboratory focuses on code-based positioning. It establishes the positioning problem that geodetic carrier-phase processing solves with much greater precision.

Sections 2–4 can be demonstrated briefly. Sections 6–8 are optional extensions and need not be assigned as part of the core laboratory.

---

# Additional Resources

> **Reading:** [GNSS Decoded: GPS Signal Structure](https://gnssdecoded.com/gps-signal-structure/)  
> An accessible explanation of the carrier wave, PRN code, navigation message, and signal modulation.

> **Videos:** [Supplementary GNSS video playlist](https://www.youtube.com/playlist?list=PLiQBCOW0daZIruZeL2ZTAmoRvIO_iflZp)

> **Short Course:** [CRESCENT: Strain Accumulation and Release from GNSS](https://cascadiaquakes.org/geoscience-education-and-inclusion/technical-short-courses/geodesy/)  
> Lectures and Jupyter notebooks covering GNSS time series, earthquake-cycle deformation, and fault modeling.