# The Inverse Problem: Finding Fault Slip from Surface Observations

## Purpose

Last lecture we established the forward problem: given a slip distribution
$\mathbf{m}$ and Green's functions $\mathbf{G}$, compute the predicted surface
displacements $\mathbf{d} = \mathbf{G}\mathbf{m}$. That was a physics calculation —
it always has a unique, stable answer.

This lecture runs the problem in reverse. We have measured surface displacements
from a real earthquake or slow slip event — GPS offsets, InSAR fringes. We want
to know **where on the fault the slip occurred, and how much**.

That sounds simple. It is not. The same equations that made the forward problem
easy make the inverse problem genuinely hard, in ways that are both mathematical
and physical. Understanding those difficulties — and how to deal with them — is
the whole point of this lecture.

By the end you will be able to:

- explain why the inverse problem is harder than the forward problem, even when
  the equations look the same
- describe what it means for a matrix to be singular or ill-conditioned, and
  why that matters for fault slip estimation
- construct the least-squares solution and explain when it fails
- write down a regularized inversion and explain in plain terms what each piece does
- use the L-curve to choose how much regularization to apply
- interpret the resolution matrix to honestly assess what your inversion recovered

You will implement all of this in the upcoming lab.

---

# Part 1 — The Setup: What We Have and What We Want

## A Motivating Scenario

Imagine it is July 5, 2019. A Mw 7.1 earthquake has just ruptured a system of
previously unmapped strike-slip faults near Ridgecrest in the Mojave Desert,
California — the largest earthquake to hit Southern California in twenty years.
GNSS receivers across the region have recorded static offsets of up to ~50 cm.
Sentinel-1 InSAR satellites will image the full deformation field with centimeter
precision, revealing a complex pattern of conjugate NW- and NE-striking fault
strands across hundreds of square kilometers of desert.

You are a geodesist. You have:

- A **data vector** $\mathbf{d}$ — GNSS offsets and InSAR displacements at
  thousands of sites, all stacked into a single column of numbers.
- A **Green's function matrix** $\mathbf{G}$ — computed from Okada's solution for
  your assumed fault geometry. This is the same matrix you built in the forward
  modeling lecture and lab.

You want to find the slip distribution $\mathbf{m}$ that, when fed into the
forward model $\mathbf{d} = \mathbf{G}\mathbf{m}$, reproduces the observations.
Can you just divide both sides by $\mathbf{G}$?

$$\mathbf{m} = \mathbf{G}^{-1}\mathbf{d} \quad \text{???}$$

The answer is almost always no — and understanding *why* not is the core of
this lecture.

---

## Recapping the Equation

$$\underbrace{\mathbf{d}}_{n \times 1} = \underbrace{\mathbf{G}}_{n \times m}
\underbrace{\mathbf{m}}_{m \times 1}$$

Let's be concrete about what these are:

- $\mathbf{d}$ is the **data vector** — all your displacement measurements
  stacked into one long column. If you have 150 GNSS stations each measuring
  east, north, and vertical displacement, then $n = 450$.
- $\mathbf{m}$ is the **model vector** — the slip on every fault patch, stacked
  into one long column. If you discretize the fault into 300 patches each with
  two slip components (strike-slip and dip-slip), then $m = 600$.
- $\mathbf{G}$ is the **Green's function matrix**, which is $n \times m$: one row
  per observation, one column per slip parameter. Entry $G_{ij}$ answers: if
  patch $j$ slips 1 meter, how much does observation $i$ move?

---

## Two Things to Notice About the Sizes

In the example above, $n = 450$ observations and $m = 600$ unknowns. There are
more unknowns than observations. This is the norm in slip inversion and it immediately 
tells us that no unique solution exists — infinitely
many slip distributions will reproduce the same surface data.

Even when $n > m$ on paper, the situation is often just as bad in practice,
because many observations are not independent. InSAR pixels separated by 1 km
share atmospheric noise. GNSS stations on the same crustal block move together.
The *effective* number of independent constraints is much smaller than the raw
count. As Ide (2007) puts it, the effective rank of $\mathbf{G}$ in slip inversion
is typically "less than the number of parameters," so the problem is underdetermined
even when it appears overdetermined on paper.

---

## The Three Things That Can Go Wrong

**1. Non-uniqueness.** When there are more unknowns than independent constraints,
infinitely many slip distributions fit the data equally well. The inverse has no
unique answer. Which one do you report?

**2. Instability.** Even when a unique solution technically exists, it can be
wildly sensitive to tiny changes in the data. A 1 mm measurement error might
produce a 500 m error in the recovered slip. This happens — as we will see in
detail — when two fault patches produce nearly identical surface signals and the
inversion cannot distinguish between them.

**3. Physical implausibility.** Even if a mathematically valid solution exists,
it might predict negative slip (a thrust fault patch slipping in the wrong
direction), or adjacent patches alternating between +20 m and −18 m. The linear
algebra does not know about geology.

All three problems are addressed the same way: **regularization** — adding
geological constraints to the inversion that encode what we know fault slip
distributions should look like.

---

## Why Deep Patches Are the Worst Offenders

Problems (1) and (2) are much worse for deep fault patches than shallow ones.

Recall from last lecture that a patch's surface fingerprint gets broader and
smoother as depth increases. A patch at 5 km depth produces a sharp, localized
signal. A patch at 25 km depth produces a broad, diffuse signal that overlaps
heavily with its neighbors.

When two adjacent deep patches produce nearly identical fingerprints, the
inversion faces a fundamental problem: any amount of slip can be transferred
from one patch to the other without changing the predicted surface displacement
at all. From the surface data's perspective, the two patches are indistinguishable.

```{figure} ../figures/10_singular_G_patch_fingerprints.png
---
name: Patches
width: 800px
alt: Cross-section showing three fault patches at different depths, alongside their surface displacement fingerprints. The shallow patch produces a sharp localized signal; the two deep patches produce nearly identical broad signals.
---
**Figure 1.** Surface displacement fingerprints (columns of **G**) for three fault patches at different depths. The shallow patch A (orange) produces a sharp, localized signal easily identified by the inversion. The two deep patches B and C produce broad, nearly identical signals — their columns in **G** are nearly parallel. When columns of **G** are nearly parallel, **G**ᵀ**G** becomes nearly singular and cannot be safely inverted. The inversion cannot distinguish slip on B from slip on C, so it may assign arbitrarily large and opposite values to both while still fitting the data at the surface.
```

---

# Part 2 — Least Squares: The Obvious Approach and Why It Fails

## What We Want

We want the slip vector $\mathbf{m}$ such that $\mathbf{G}\mathbf{m}$ is as
close as possible to our observed data $\mathbf{d}$. The natural measure of
"close" is the sum of squared differences:

$$\text{misfit} = \|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2
= \sum_{i=1}^{n} \left(\text{predicted}_i - \text{observed}_i\right)^2$$

We square the differences so that positive and negative gaps do not cancel, and
so that large gaps are penalized more heavily than small ones. This is the
**least-squares** criterion — the same one you have seen in curve fitting.

> **Objective function:** The expression being minimized —
> $\|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2$ — is called the **objective
> function**. It is a single number that scores how bad a given slip
> distribution $\mathbf{m}$ is: large when the model fits poorly, zero
> when it fits perfectly. The point of least squares is to find the
> $\mathbf{m}$ that makes this number as small as possible.

---

## Deriving the Solution

To minimize $\|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2$, take the derivative with
respect to $\mathbf{m}$ and set it to zero. This gives the **normal equations**:

$$\mathbf{G}^T\mathbf{G}\,\mathbf{m} = \mathbf{G}^T\mathbf{d}$$

Why "normal"? Because at the minimum, the residual vector
($\mathbf{d} - \mathbf{G}\mathbf{m}$, the gap between predictions and
observations) is perpendicular (normal) to the column space of $\mathbf{G}$ —
the set of all surface displacement patterns the model can possibly produce.
Geometrically, $\mathbf{G}\mathbf{m}_{LS}$ is the point in the column space
closest to the observed data $\mathbf{d}$.

Solving the normal equations:

$$\boxed{\mathbf{m}_{LS} = (\mathbf{G}^T\mathbf{G})^{-1}\mathbf{G}^T\mathbf{d}}$$

---

## What Does "Singular" Mean, and Why Does It Matter?

The least-squares formula requires inverting the matrix $\mathbf{G}^T\mathbf{G}$.
But not all matrices can be inverted.

**A matrix is singular if it cannot be inverted.** By analogy: $1/x$ is undefined
when $x = 0$, because no number times zero gives you back 1. A singular matrix
is the multi-dimensional equivalent — it collapses some directions in space to
zero, and you cannot undo that. If $\mathbf{G}^T\mathbf{G}$ is singular, the
formula $(\mathbf{G}^T\mathbf{G})^{-1}$ does not exist, and the solution blows up.

**A matrix is ill-conditioned** (i.e. nearly singular) if it can
technically be inverted, but the result is not meaningful. Near-singular
matrices act like dividing by a very small number — a tiny change in the input
produces an enormous change in the output. If $\mathbf{G}^T\mathbf{G}$ is nearly
singular, a 1 mm error in your GPS measurement can become a 1000 m error in your
recovered slip. The inversion magnifies noise instead of filtering it.

This happens in fault inversion whenever two columns of $\mathbf{G}$ are nearly
identical — that is, whenever two patches produce nearly the same surface signal.
The matrix $\mathbf{G}^T\mathbf{G}$ becomes nearly singular, and inverting it is
numerically meaningless.

> **Example:** Suppose patches B and C each produce 2 mm of northward
> displacement at every station. The inversion can assign +1000 m to B and −999 m
> to C and get almost exactly the same predicted data as assigning 0.5 m to each.
> Both solutions fit the data equally well. The mathematics picks one of them, but
> the result is not physical.

---

## The Underdetermined Case: Infinitely Many Solutions

When there are more unknowns than independent constraints, there are infinitely
many slip vectors that exactly satisfy $\mathbf{G}\mathbf{m} = \mathbf{d}$.

The mathematical reason is that **G** has a **null space** — a set of slip
patterns that produce zero surface displacement. These are not physically
desired; they arise because some combinations of slip on different patches
cancel each other's surface signals perfectly. If $\mathbf{m}_0$ is one
solution that fits the data, then $\mathbf{m}_0 + \mathbf{n}$ also fits
the data exactly for any null space vector $\mathbf{n}$, because adding
$\mathbf{n}$ changes the predicted displacements by exactly zero. The
inversion has no way to distinguish between these solutions, giving
infinitely many equally valid answers. Deep patches whose broad, overlapping
signals nearly cancel each other are close to null space vectors — which is
why deep slip is always the hardest to resolve.

One approach — the **minimum norm solution** — picks the solution with the smallest
total slip. But "smallest total slip" is not the right criterion for fault slip. Real
earthquakes concentrate slip in asperities. The minimum norm solution smears a
little slip uniformly across every patch — mathematically clean but geologically
wrong.

> **The bottom line:** Plain least squares fails for fault inversion. The matrix
> is singular or nearly singular, noise gets amplified catastrophically, and even
> when a solution exists it has the wrong physical character. We need to add
> information from outside the data.

---

# Part 3 — Regularization: Adding What the Data Cannot Provide

## The Core Idea

Since the data alone cannot pin down a unique, stable, physically reasonable slip
distribution, we need to bring in external information. That information comes from
geology: we know things about what a fault slip distribution should look like even
before looking at a single GPS measurement.

**Regularization** formalizes this. We add a **penalty term** to the objective
function that scores how geologically unreasonable a given slip distribution is.
The inversion then minimizes the combined score: fit the data well, but not at
the cost of a geologically absurd model.

The structure is:

$$\min_{\mathbf{m}} \underbrace{\|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2}_{\text{data misfit}}
+ \underbrace{\lambda^2 \cdot \text{penalty}(\mathbf{m})}_{\text{geological penalty}}$$

The parameter $\lambda$ (lambda) is a dial that controls the balance:

- **Large $\lambda$:** the geological penalty dominates. The solution looks
  physically reasonable but may not fit the data very well.
- **Small $\lambda$:** the data misfit dominates. The solution fits the data
  closely but may be noisy and unrealistic.
- **Goal:** find a $\lambda$ where the solution fits the data to within its noise
  level and looks geologically plausible.

How to choose $\lambda$ is covered in Part 5. First, two choices of penalty.

---

## Damping: "Prefer Small Slip"

The simplest penalty is on the **total size** of the slip vector:

$$\text{penalty} = \|\mathbf{m}\|^2 = m_1^2 + m_2^2 + \cdots + m_M^2$$

Among all distributions that fit the data reasonably, prefer the one with the
smallest total slip. The combined objective is:

$$\min_{\mathbf{m}} \|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2 + \lambda^2\|\mathbf{m}\|^2$$

This can be rewritten as an augmented least-squares system by stacking extra
equations below the original:

$$\begin{bmatrix}\mathbf{G}\\ \lambda\mathbf{I}\end{bmatrix}\mathbf{m}
= \begin{bmatrix}\mathbf{d}\\ \mathbf{0}\end{bmatrix}$$

The bottom block says: try to make $\lambda \cdot \mathbf{m} \approx \mathbf{0}$
— keep the slip small. The solution is:

$$\mathbf{m}_{damp} = (\mathbf{G}^T\mathbf{G} + \lambda^2\mathbf{I})^{-1}
\mathbf{G}^T\mathbf{d}$$

Notice what adding $\lambda^2\mathbf{I}$ does: it adds a positive number to every
diagonal entry of $\mathbf{G}^T\mathbf{G}$. This prevents any direction from
collapsing to zero. Even if $\mathbf{G}^T\mathbf{G}$ was singular, the sum
$\mathbf{G}^T\mathbf{G} + \lambda^2\mathbf{I}$ is always invertible for $\lambda > 0$.
**Regularization literally fixes the singularity problem.**

**When is damping appropriate?** When you expect slip to be genuinely small —
slow slip events with centimeter-scale motion. For large earthquakes with meter-scale
slip, damping is the wrong geological expectation and will underestimate the slip.

---

## Smoothing: "Prefer Spatially Coherent Slip"

For most coseismic earthquakes, the better geological expectation is not that
slip is small, but that it varies **smoothly** across the fault. Adjacent patches
tend to have similar slip — real fault slip does not jump erratically from one
subfault to the next.

**Smoothing regularization** penalizes abrupt changes between neighboring patches:

$$\text{penalty} = \|\mathbf{L}\mathbf{m}\|^2$$

where $\mathbf{L}$ is the **Laplacian smoothing matrix**. Here is what it does.

The second derivative of a function at a point measures how much that point
differs from its neighbors. For slip values on a 1D row of patches:

$$\text{second derivative at patch } j \approx m_{j-1} - 2m_j + m_{j+1}$$

If this is large in magnitude, the slip is curving sharply at patch $j$ — it is
rough. If this is near zero, the slip is varying smoothly there. The matrix
$\mathbf{L}$ computes this second derivative at every patch simultaneously.
One row of $\mathbf{L}$ looks like:

$$[\mathbf{L}]_j = \begin{pmatrix} \cdots & 1 & -2 & 1 & \cdots \end{pmatrix}$$

(with $-2$ in column $j$, and $1$ in the columns for patch $j$'s neighbors).
Penalizing $\|\mathbf{L}\mathbf{m}\|^2$ means penalizing the squared second
derivative across the fault. The inversion is discouraged from producing sharp
kinks or checkerboard patterns in the slip.

The augmented system:

$$\begin{bmatrix}\mathbf{G}\\ \lambda\mathbf{L}\end{bmatrix}\mathbf{m}
= \begin{bmatrix}\mathbf{d}\\ \mathbf{0}\end{bmatrix}$$

The bottom block says: try to make $\lambda \cdot \mathbf{L}\mathbf{m} \approx \mathbf{0}$
— keep the slip smooth. The solution is:

$$\mathbf{m}_{smooth} = (\mathbf{G}^T\mathbf{G} + \lambda^2\mathbf{L}^T\mathbf{L})^{-1}
\mathbf{G}^T\mathbf{d}$$

```{figure} ../figures/10_damping_vs_smoothing.png
---
name: fig-damping-vs-smoothing
width: 800px
alt: Six-panel figure. Top row: slip maps for the true slip distribution, the damped inversion, and the smoothed inversion. Bottom row: predicted vs observed displacements at each station for each model, with RMS misfit labelled.
---
Top row: Slip distributions recovered by each approach on the same synthetic fault, compared to the true slip (left). The damped inversion (centre) amplifies noise into large, oscillating values with unphysical back-slip (blue) — the size penalty suppresses amplitude but imposes no spatial structure. The smoothed inversion (right) recovers a coherent asperity in the correct location, though blurred relative to the truth. Bottom row: observed displacements (black dots) and model predictions (coloured line) at each station, sorted by along-strike position. The damped model achieves a lower RMS misfit (1.39 vs 1.76) by fitting noise as well as signal — its jagged predicted line tracks individual data outliers. The smoothed model fits the broad pattern of the data without chasing every wiggle. This is the central trade-off of regularization: a better data fit does not mean a better slip model.
```

---

## Comparing the Two

| | Damping | Smoothing |
|---|---|---|
| **Penalty** | $\lambda^2\|\mathbf{m}\|^2$ — total slip size | $\lambda^2\|\mathbf{L}\mathbf{m}\|^2$ — slip roughness |
| **Geological expectation** | Slip is small | Slip varies smoothly |
| **Best for** | Slow slip events | Coseismic earthquakes |
| **Risk** | Underestimates large, concentrated asperities | Blurs sharp slip boundaries |

---

## The Non-Negativity Constraint

One more constraint is almost always imposed: **slip must be non-negative** —
it must be in the physically expected direction. A thrust patch should slip
upward (or not at all). A right-lateral strike-slip patch should slip rightward.
Negative slip (back-slip) during a coseismic rupture is physically unreasonable.

Without this constraint, the inversion often assigns large negative slip to patches
to cancel their neighbors' signals, fitting the data with an absurd model. The
constraint is added as:

$$\min_{\mathbf{m} \geq \mathbf{0}} \|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2
+ \lambda^2\|\mathbf{L}\mathbf{m}\|^2$$

The "$\mathbf{m} \geq \mathbf{0}$" means every entry must be zero or positive.
This is called **non-negative least squares (NNLS)**, implemented in Python as
`scipy.optimize.nnls` or `scipy.optimize.lsq_linear` with explicit bounds.

---

# Part 4 — Choosing the Regularization Parameter

## The Central Trade-Off

The regularization parameter $\lambda$ controls a genuine tension. Think of it
as a dial with two extremes:

**Too small $\lambda$:** the data misfit term dominates. The inversion will fit
every data point as closely as possible — but GPS measurements contain noise, so
the inversion will also fit the noise. The recovered slip will show high-frequency
oscillations that reflect measurement errors, not real fault slip. The model
explains the data too well.

**Too large $\lambda$:** the smoothing penalty dominates. The solution becomes
an unrealistically featureless blob — all patches slip about the same amount
regardless of what the data say. The model fits the data poorly.

**The right $\lambda$** lives between these extremes: the solution fits the data
to within the noise level (no better, no worse) and looks geologically plausible.
Finding it requires systematically exploring a range of $\lambda$ values.

---

## The L-Curve

The **L-curve** is the standard tool. Here is how to construct one:

1. Run the inversion for many values of $\lambda$, from very small to very large.
2. For each solution, compute two quantities:
   - the **data misfit** — how poorly the model fits the observations:
     $$\|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2 = \sum_{i=1}^{n}(\mathbf{G}_i\mathbf{m} - d_i)^2$$
   - the **model roughness** — how spatially variable the slip distribution is:
     $$\|\mathbf{L}\mathbf{m}\|^2 = \sum_{j=1}^{M}(\mathbf{L}_j\mathbf{m})^2$$
     where $\mathbf{L}_j\mathbf{m}$ is the discrete second derivative of slip
     at patch $j$ — large when adjacent patches differ strongly, near zero
     when slip varies smoothly.
3. Plot roughness on the vertical axis and misfit on the horizontal axis. Each
   value of $\lambda$ gives one point.

The resulting curve is L-shaped:

```{figure} ../figures/10_slip_lcurve.png
---
name: fig-l-curve
width: 950px
alt: Seven-panel figure. Left column: L-curve in log-log space with three
  labelled points marking under-regularized, optimal, and over-regularized
  solutions. Top row: slip maps for each of the three solutions. Bottom
  row: predicted vs observed displacements at each station for each
  solution, with RMS misfit labelled.
---
**Top row:** recovered slip distributions for three values of $\lambda$
on the same synthetic fault. The under-regularized model (red,
$\lambda = 0.04$) amplifies noise into large-amplitude oscillations with
unphysical back-slip (blue). The optimal model (green, $\lambda = 0.50$)
recovers a coherent slip pattern. The over-regularized model (blue,
$\lambda = 2.54$) is a featureless plateau — the smoothing penalty has
overwhelmed the data signal entirely. **Middle row:** predicted vs
observed displacements at each station. The under-regularized model
achieves the lowest RMS misfit (0.53) by fitting noise as well as signal;
the optimal model fits the data to within its noise level (0.65); the
over-regularized model fits poorly (0.82). A lower RMS does not mean a
better slip model. **Bottom row:** the L-curve plotted on linear (left)
and log-log (right) scales. The L-shape is geometrically clear on the
linear scale: a near-vertical arm where roughness drops steeply at low
misfit, bending into a near-horizontal arm where misfit grows but
roughness is already near its floor. Log-log is the standard in the
literature because it gives readable axes on both arms — but it compresses
the L into a smooth bend. In practice, the goal is to identify the corner
(the point of maximum curvature), not a literal right angle.
```

**Why is it L-shaped?**

- **Large $\lambda$ (upper left):** the smoothing penalty completely controls the
  solution, which is flat and featureless. The misfit is large (the model is too
  smooth to match the data), but the roughness is tiny.
- **Small $\lambda$ (lower right):** the data fit controls the solution. The
  model explains every data point including the noise, becoming very rough. The
  misfit is tiny, but the roughness is large.
- **At the corner:** the curve bends. Decreasing $\lambda$ beyond the corner
  produces rapidly increasing roughness for very little improvement in fit. **The corner is the optimal balance.**

> **Rule of thumb:** A well-regularized solution should fit the data to within
> roughly its noise level. If residuals are much smaller
> than measurement uncertainties, you are fitting noise. If they are much larger,
> you are over-smoothing.

---

# Part 5 — Data Weighting: Not All Observations Are Equal

## The Problem with Equal Weighting

Everything in Part 3 treated all observations as equally reliable. In reality,
some measurements are much more precise than others. A GNSS station directly
above the fault recording a 30 cm offset with 2 mm uncertainty carries far more
information than a distant station recording a 3 mm signal with 5 mm uncertainty.
Treating them equally is like giving equal credibility to a precision laboratory 
measurement and a rough field estimate.

In practice:

- GNSS vertical offsets are 2–3× noisier than horizontal offsets (most atmospheric
  noise is vertical).
- InSAR coherence varies: bare desert (like Ridgecrest) is excellent; vegetated
  areas are noisy.
- InSAR has millions of pixels and GNSS has hundreds of stations. Treating all
  measurements equally lets InSAR completely dominate — even though those millions
  of pixels are not millions of independent measurements (adjacent pixels share the
  same atmospheric noise).

---

## The Data Covariance Matrix

We encode each measurement's reliability in the **data covariance matrix**
$\mathbf{C}_d$. This is an $n \times n$ matrix. For uncorrelated observations
with uncertainties $\sigma_i$, it is diagonal:

$$\mathbf{C}_d = \begin{pmatrix} \sigma_1^2 & 0 & \cdots & 0 \\
0 & \sigma_2^2 & \cdots & 0 \\
\vdots & & \ddots & \vdots \\
0 & 0 & \cdots & \sigma_n^2 \end{pmatrix}$$

Think of it as a lookup table: diagonal entry $\sigma_i^2$ is the variance
(uncertainty squared) of measurement $i$. Large variance = noisy measurement.
Small variance = precise measurement.

Off-diagonal entries $C_d^{ij}$ capture correlations between measurements — if
observations $i$ and $j$ share a noise source (e.g., both lie under the same
patch of atmosphere), they co-vary and $C_d^{ij} \neq 0$. For most GNSS
applications we assume uncorrelated measurements and use a diagonal $\mathbf{C}_d$.
For InSAR, correlations between adjacent pixels matter.

> **Where do uncertainties come from?** The $\sigma_i$ values come directly
> from the GNSS processing software (GAMIT, GIPSY, or Bernese): when you
> download a processed GNSS time series or coseismic offset solution, the
> uncertainty is reported alongside the displacement. They reflect a
> combination of formal receiver noise, atmospheric delay residuals, and
> monument stability. The vertical component is typically 2–3× larger than
> horizontal — which is why vertical displacements are often down-weighted
> or dropped entirely in geodetic inversions.

---

## Weighted Least Squares

With $\mathbf{C}_d$ in hand, we modify the objective function to weight each
observation by its precision:

$$\min_{\mathbf{m}} \|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2_{\mathbf{C}_d^{-1}}$$

where the subscript $\mathbf{C}_d^{-1}$ on the norm means each residual is
scaled by the precision of that observation. This is shorthand for:

$$\min_{\mathbf{m}} \sum_{i=1}^{n} \frac{\left(\mathbf{G}_i\mathbf{m} - d_i\right)^2}{\sigma_i^2}$$

where $\mathbf{G}_i$ is the $i$-th row of $\mathbf{G}$ and $d_i$ is the
$i$-th observation. Each squared residual is divided by the variance of
that observation — precise measurements (small $\sigma_i$) count more,
noisy measurements (large $\sigma_i$) count less. When $\mathbf{C}_d =
\mathbf{I}$ (all observations equally reliable) this reduces to the
ordinary misfit $\|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2$ from Part 2.

The solution:

$$\boxed{\mathbf{m}_{WLS} = (\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G})^{-1}
\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{d}}$$

This is identical to the ordinary least-squares formula, with $\mathbf{C}_d^{-1}$
inserted in both places. The $\mathbf{C}_d^{-1}$ effectively rescales each
equation by $1/\sigma_i$ before solving.

---

# Part 6 — What Did We Actually Recover?

## The Truth About Regularization

The regularized solution is not the true slip distribution. It is a smoothed,
blurred version of the true slip. We added the smoothing constraint because
the data alone could not determine a unique solution — but that constraint also
changes what we recover. A sharp asperity in the true slip distribution might
be averaged out by the smoothing and not appear in the recovered model, not
because it was not there, but because the data coverage was insufficient to
resolve it against the smoothing constraint.

How do we know how much blurring has occurred? The **resolution matrix** tells us.

---

## Building Intuition Before the Math

Imagine the true slip distribution has a small, sharp asperity on a deep patch
— say, 10 m of slip concentrated in a 10 km region. The surface signal from this
asperity is broad and smooth (because the patch is deep), and looks almost
identical to the signal from spreading the same total slip over a 30 km region.

The inversion sees the broad surface signal and, with smoothing applied, will
recover a broad, smooth slip distribution on that deep patch — not the sharp
asperity that is actually there. The recovered slip is the true slip *averaged*
over the patch and its neighbors. The resolution matrix quantifies exactly how
wide that averaging kernel is.

---

## The Resolution Matrix

Write the regularized inversion as a single linear operator $\mathbf{M}$ applied
to the data:

$$\mathbf{m}_{est} = \mathbf{M}\mathbf{d}$$

Now substitute the true forward model 
$\mathbf{d} = \mathbf{G}\mathbf{m}_{true} + \boldsymbol{\varepsilon}$ (true model plus noise):

$$\mathbf{m}_{est} = \mathbf{M}\mathbf{G}\,\mathbf{m}_{true}
+ \mathbf{M}\boldsymbol{\varepsilon}$$

where we define $\mathbf{R} = \mathbf{M}\mathbf{G}$ as the **resolution matrix**,
giving:

$$\mathbf{m}_{est} = \mathbf{R}\,\mathbf{m}_{true} + \mathbf{M}\boldsymbol{\varepsilon}$$

When $\mathbf{R}$ equals the identity matrix $\mathbf{I}$, resolution is perfect —
the estimated model equals the true model apart from noise. In practice
$\mathbf{R} \neq \mathbf{I}$, meaning our estimate for patch $j$ is a weighted
average of the true slip on patch $j$ and its neighbors. The $j$-th row of
$\mathbf{R}$ is the **resolution kernel** for patch $j$ — it tells you how wide
that averaging is.

A **compact resolution kernel** (most weight on patch $j$ itself) means patch $j$
is well-resolved — our estimate closely reflects what was actually there. A
**broad resolution kernel** (weight spread across many patches) means patch $j$
is poorly resolved — our estimate is an average over a large area, and we cannot
distinguish slip concentrated on patch $j$ from slip spread across its neighbors.

```{figure} ../figures/11_resolution_matrix.png
---
name: fig-resolution-matrix
width: 720px
alt: Left panel showing the resolution matrix as an image; right panel
  showing two resolution kernels — one compact for a shallow patch, one
  broad for a deep patch.
---
**Left:** the resolution matrix $\mathbf{R}$ displayed as an image. Each
row is the resolution kernel for one patch. A perfect diagonal would mean
perfect resolution everywhere. **Right:** two resolution kernels plotted
on the fault surface. The shallow patch has a compact kernel — its
estimate closely reflects the true slip there. The deep patch has a broad
kernel — its estimate is an average over a large area, meaning we cannot
resolve fine structure at depth.
```

---

## Resolution Always Degrades with Depth

This is not a coincidence. Deep patches produce broad surface signals whose
Green's function columns are nearly parallel. The inversion cannot distinguish
them. The smoothing regularization makes it worse — it explicitly averages
neighboring patches. The result is that resolution kernels for deep patches are
always broader than those for shallow patches, regardless of how good your data
coverage is.

This has a direct implication for how you interpret results: before claiming a
feature on a deep patch, check its resolution kernel. If the kernel spans 100 km,
you have not resolved a 10 km asperity — you have estimated the average slip over
a 100 km region.

---

## Model Uncertainty: A Separate Question

The resolution matrix tells you about blurring — how much the smoothing smears
the true slip. But there is a separate question: how much do measurement errors
in the data propagate into errors in the slip estimate?

The **model covariance matrix** $\mathbf{C}_m = \mathbf{M}\mathbf{C}_d\mathbf{M}^T$
answers this. Its diagonal entries give the variance of each slip estimate.
These two diagnostics measure different things:

| | What it tells you | Gets worse when |
|---|---|---|
| Resolution matrix $\mathbf{R}$ | How blurred is the solution? | $\lambda$ is large |
| Model covariance $\mathbf{C}_m$ | How uncertain is the solution? | $\lambda$ is small |

Increasing $\lambda$ reduces noise sensitivity (smaller $\mathbf{C}_m$ diagonals)
but increases blurring (broader resolution kernels). The L-curve corner balances
both.

---

# Part 7 — Putting It All Together

## The Complete Problem

For a joint GNSS + InSAR slip inversion with smoothing, data weighting, and
non-negativity, the full problem is:

$$\min_{\mathbf{m} \geq \mathbf{0}}
\underbrace{(\mathbf{G}\mathbf{m} - \mathbf{d})^T\mathbf{C}_d^{-1}(\mathbf{G}\mathbf{m} - \mathbf{d})}_{\text{weighted data misfit}}
+ \underbrace{\lambda^2\|\mathbf{L}\mathbf{m}\|^2}_{\text{smoothing penalty}}$$

Each piece:

- **Weighted data misfit:** fit the observations, trusting precise measurements
  more than noisy ones. $\mathbf{C}_d^{-1}$ encodes which stations are reliable.
- **Smoothing penalty:** prefer slip that varies smoothly, as real faults do.
  $\mathbf{L}$ is the Laplacian that measures roughness.
- **Non-negativity:** slip must be in the expected direction.
- **$\lambda$:** chosen by L-curve to balance fit against smoothness.

This is the standard formulation in nearly all published geodetic slip inversions.

---

## The Workflow in Plain Steps

```
1. Prepare data
   ├── Collect GNSS/InSAR records
   ├── Estimate uncertainties σ_i for each measurement
   ├── Build C_d (diagonal matrix: σ_i² on diagonal)
   └── Decide how to handle InSAR overweighting (subsample or weight)

2. Build G  
   ├── Assume fault geometry from aftershocks, surface trace, focal mechanism
   └── Compute using Okada or cutde for each patch × each station

3. Build L  
   ├── Find neighboring fault patches (which ones share a side?)
   └── Construct Laplacian finite-difference operator

4. Choose λ  
   ├── Run inversions for a range of λ values
   └── Find the L-curve corner: fit = noise level, model = geologically plausible

5. Solve  
   ├── Stack [G; λL] → assembled_mat
   ├── Apply data weights
   └── Solve with NNLS or bounded least squares (scipy.optimize.lsq_linear)

6. Assess honestly
   ├── Compute resolution matrix R = MG
   ├── Plot resolution kernels for deep and shallow patches
   ├── Check that residuals match your data uncertainties
   └── State what is well-resolved and what is not
```

---

# Summary

- The **inverse problem** asks: given surface displacements $\mathbf{d}$ and
  Green's functions $\mathbf{G}$, find fault slip $\mathbf{m}$. Unlike the
  forward problem, the solution is generally non-unique, unstable, or physically
  unreasonable.

- A matrix is **singular** if it cannot be inverted — the matrix analog of
  dividing by zero. A matrix is **nearly singular** (ill-conditioned) if small
  input changes produce huge output changes. $\mathbf{G}^T\mathbf{G}$ is nearly
  singular whenever two fault patches have nearly identical surface signals, which
  always happens for deep patches.

- **Regularization** adds a geological penalty term. **Damping** (penalizes slip
  size, via $\lambda^2\|\mathbf{m}\|^2$) suits slow slip events. **Smoothing**
  (penalizes slip roughness, via $\lambda^2\|\mathbf{L}\mathbf{m}\|^2$) suits
  coseismic earthquakes. Both fix the singularity by making the matrix
  $\mathbf{G}^T\mathbf{G} + \lambda^2(\cdot)$ invertible.

- The **data covariance matrix** $\mathbf{C}_d$ encodes measurement uncertainties.
  **Weighted least squares** down-weights noisy observations and up-weights precise
  ones, preventing one noisy dataset from dominating the inversion.

- The **regularization parameter $\lambda$** is chosen using the **L-curve**: plot
  model roughness vs. data misfit for a range of $\lambda$ values, and choose the
  corner. The optimal solution fits the data to within its noise level.

- The **resolution matrix** $\mathbf{R} = \mathbf{M}\mathbf{G}$ measures blurring.
  A compact resolution kernel means a patch is well-resolved. A broad kernel means
  the estimate is an average over a large area. Resolution always degrades with depth.

- The **Chi-Chi earthquake** shows the resolution principle in action: gross
  features (well-resolved, data-controlled) agree across all groups; fine details
  (poorly-resolved, regularization-dependent) do not.

---

# Key Equations

| Quantity | Expression | Plain meaning |
|---|---|---|
| Forward problem | $\mathbf{d} = \mathbf{G}\mathbf{m}$ | Slip → surface displacement |
| Least squares | $\mathbf{m} = (\mathbf{G}^T\mathbf{G})^{-1}\mathbf{G}^T\mathbf{d}$ | Best fit, no constraints |
| Weighted LS | $\mathbf{m} = (\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G})^{-1}\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{d}$ | Best fit, weighted by data quality |
| Damped LS | $\mathbf{m} = (\mathbf{G}^T\mathbf{G} + \lambda^2\mathbf{I})^{-1}\mathbf{G}^T\mathbf{d}$ | Best fit, prefer small slip |
| Smoothed LS | $\mathbf{m} = (\mathbf{G}^T\mathbf{G} + \lambda^2\mathbf{L}^T\mathbf{L})^{-1}\mathbf{G}^T\mathbf{d}$ | Best fit, prefer smooth slip |
| Resolution matrix | $\mathbf{R} = \mathbf{M}\mathbf{G}$ | How blurred is the solution? |

---

# Additional Resources

> **Textbook:** Aster, R. C., Borchers, B., & Thurber, C. H. (2019).
> *Parameter Estimation and Inverse Problems* (3rd ed.). Academic Press.
> The most accessible graduate-level text; excellent on regularization and the
> L-curve with worked Python examples. Start here.

> **Textbook:** Menke, W. (2018). *Geophysical Inverse Theory* (2nd ed.).
> Princeton University Press. The standard graduate reference.

> **Classic paper:** Hansen, P. C. (1992). Analysis of discrete ill-posed
> problems by means of the L-curve. *SIAM Review*, 34(4), 561–580.

> **Reference for this lecture:** Ide, S. (2007). Slip inversion. In
> *Treatise on Geophysics*, Vol. 4, pp. 193–223. Elsevier. Sections 4.07.2–4.07.4
> cover the formulation used here; Section 4.07.4 has the Chi-Chi comparison.


---

# Appendix — Derivation of the Normal Equations

## Setup

We want to find the slip vector $\mathbf{m}$ that minimizes the sum of squared
residuals between predicted and observed displacements:

$$f(\mathbf{m}) = \|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2$$

For any vector $\mathbf{v}$, $\|\mathbf{v}\|^2 = \mathbf{v}^T\mathbf{v}$, so:

$$f(\mathbf{m}) = (\mathbf{G}\mathbf{m} - \mathbf{d})^T(\mathbf{G}\mathbf{m} - \mathbf{d})$$

---

## Step 1 — Expand

Expanding $(a - b)^T(a - b)$ just like $(a-b)^2 = a^2 - 2ab + b^2$:

$$f(\mathbf{m}) = \mathbf{m}^T\mathbf{G}^T\mathbf{G}\mathbf{m}
- 2\,\mathbf{d}^T\mathbf{G}\mathbf{m}
+ \mathbf{d}^T\mathbf{d}$$

The two cross terms are both scalars and equal
($\mathbf{d}^T\mathbf{G}\mathbf{m} = \mathbf{m}^T\mathbf{G}^T\mathbf{d}$),
so they combine into the single $-2$ term above.

---

## Step 2 — Differentiate

Take the gradient $\partial f / \partial \mathbf{m}$ using two rules from matrix calculus:

$$\frac{\partial}{\partial \mathbf{m}}\left(\mathbf{a}^T\mathbf{m}\right) = \mathbf{a}
\qquad \text{(linear term)}$$

$$\frac{\partial}{\partial \mathbf{m}}\left(\mathbf{m}^T\mathbf{A}\mathbf{m}\right) = 2\mathbf{A}\mathbf{m}
\qquad \text{(quadratic term, } \mathbf{A} \text{ symmetric)}$$

Applying term by term:

| Term in $f$ | Gradient |
|---|---|
| $\mathbf{m}^T\mathbf{G}^T\mathbf{G}\mathbf{m}$ | $2\mathbf{G}^T\mathbf{G}\mathbf{m}$ |
| $-2\,\mathbf{d}^T\mathbf{G}\mathbf{m}$ | $-2\mathbf{G}^T\mathbf{d}$ |
| $\mathbf{d}^T\mathbf{d}$ | $\mathbf{0}$ |

$$\frac{\partial f}{\partial \mathbf{m}} = 2\mathbf{G}^T\mathbf{G}\mathbf{m} - 2\mathbf{G}^T\mathbf{d}$$

---

## Step 3 — Set to Zero and Solve

At the minimum, the gradient is zero:

$$2\mathbf{G}^T\mathbf{G}\mathbf{m} - 2\mathbf{G}^T\mathbf{d} = \mathbf{0}$$

$$\boxed{\mathbf{G}^T\mathbf{G}\,\mathbf{m} = \mathbf{G}^T\mathbf{d}}
\qquad \leftarrow \textbf{ the normal equations}$$

If $\mathbf{G}^T\mathbf{G}$ is invertible, multiply both sides by its inverse:

$$\mathbf{m}_{LS} = (\mathbf{G}^T\mathbf{G})^{-1}\mathbf{G}^T\mathbf{d}$$

> **Why "normal"?** At the minimum, the residual vector
> $\mathbf{d} - \mathbf{G}\mathbf{m}$ is perpendicular (*normal*) to every
> column of $\mathbf{G}$. Geometrically, $\mathbf{G}\mathbf{m}_{LS}$ is the
> orthogonal projection of $\mathbf{d}$ onto the column space of $\mathbf{G}$.

> **Why does this fail?** The formula requires inverting $\mathbf{G}^T\mathbf{G}$.
> When two columns of $\mathbf{G}$ are nearly identical (two fault patches with
> nearly identical surface signals), $\mathbf{G}^T\mathbf{G}$ is nearly singular
> and cannot be safely inverted. Regularization fixes this by adding
> $\lambda^2\mathbf{I}$ or $\lambda^2\mathbf{L}^T\mathbf{L}$ to the matrix
> before inverting.
