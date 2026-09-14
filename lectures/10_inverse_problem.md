# The Inverse Problem

## Purpose

In the forward modeling lecture we established that surface deformation is
related to fault slip by a linear system:

$$\mathbf{d} = \mathbf{G}\mathbf{m}$$

Given $\mathbf{m}$ (slip distribution) and $\mathbf{G}$ (Green's functions),
computing $\mathbf{d}$ (predicted observations) is straightforward. The
**inverse problem** runs this in reverse: given $\mathbf{d}$ (observations)
and $\mathbf{G}$ (Green's functions), recover $\mathbf{m}$ (slip distribution).

This turns out to be much harder — mathematically, physically, and practically.

In this lecture we will:

- define the inverse problem and contrast it with the forward problem
- introduce the tomography problem as a concrete, geometric example
- derive the least-squares solution and understand when it fails
- show why underdetermined and ill-conditioned systems need regularization
- introduce data covariance matrices and weighted least squares
- derive damping and smoothing regularization and their physical meaning
- introduce the L-curve for choosing the regularization parameter
- define the resolution matrix and model covariance — the tools for
  understanding what we can and cannot recover

---

# The Forward and Inverse Problems

---

## Two Directions Through the Same Equation

$$\mathbf{d} = \mathbf{G}\mathbf{m}$$

| | Forward problem | Inverse problem |
|---|---|---|
| **Given** | Model $\mathbf{m}$ | Data $\mathbf{d}$ |
| **Find** | Predicted data $\mathbf{d}$ | Model parameters $\mathbf{m}$ |
| **Solution** | Always exists, unique, stable | May not exist; non-unique; unstable |
| **Method** | Matrix–vector multiply | Requires inversion or optimization |

The forward problem is a physical calculation. The inverse problem is a
mathematical one — and the three failure modes (non-existence, non-uniqueness,
instability) are the central challenges we must address.

---

## A Concrete Example: Block Tomography

Before deriving the general theory, let's build intuition with a geometric
example you can visualize.

Consider a 2D grid of blocks, each with an unknown slowness perturbation
$s_j$ (fractional change in slowness from a reference model). Seismic rays
travel from sources to stations along paths that cross multiple blocks.

```{figure} ../figures/11_tomo_setup.png
---
width: 680px
alt: A 4×4 grid of slowness blocks with ray paths crossing from sources on one side to stations on the other. Each ray accumulates travel time anomaly proportional to the slowness perturbation in each block it crosses.
---
A simple 2D tomography problem. Each ray $i$ travels through a set of blocks,
accumulating travel time anomaly $r_i = \sum_j b_{ij} s_j$ where $b_{ij}$ is
the path length of ray $i$ through block $j$. The matrix $\mathbf{G}$ (here
$b_{ij}$) is sparse — most rays pass through only a few of the blocks.
```

For each ray $i$, the travel time residual is:

$$r_i = \sum_{j=1}^{m} b_{ij} s_j$$

where $b_{ij}$ is the path length of ray $i$ through block $j$ and $s_j$ is
the slowness perturbation of block $j$. Assembling all rays:

$$\underbrace{\mathbf{d}}_{n \times 1} = \underbrace{\mathbf{G}}_{n \times m}
\underbrace{\mathbf{m}}_{m \times 1}$$

This is **exactly the same equation** as the slip inversion problem — the
only difference is that here $\mathbf{m}$ contains slowness perturbations
and $\mathbf{G}$ contains ray path lengths, rather than slip values and
elastic Green's functions.

👉 **The mathematics of tomography and slip inversion are identical.** The
physical interpretation of $\mathbf{m}$ and $\mathbf{G}$ differs; the
linear algebra does not.

---

## Why the Inverse Problem Is Harder

Three things can go wrong:

**1. The system may be underdetermined ($n < m$):** fewer observations than
unknowns. No unique solution exists — infinitely many $\mathbf{m}$ fit the
data equally well. In tomography: too few ray paths to constrain all blocks.
In slip inversion: too few GNSS stations to resolve all fault patches.

**2. The system may be ill-conditioned:** $\mathbf{G}^T\mathbf{G}$ is nearly
singular, meaning small changes in $\mathbf{d}$ (noise) cause huge changes
in $\mathbf{m}$. This happens when some model parameters have nearly the same
effect on the data — they cannot be distinguished.

**3. The model may be physically unreasonable:** even if a mathematical
solution exists, it may have negative slip, discontinuous patches, or other
features that are geologically implausible.

All three problems are addressed by **regularization** — adding constraints
that encode our prior knowledge about what a reasonable model looks like.

---

# Least Squares

---

## The Overdetermined Case

When we have more observations than unknowns ($n > m$) and the system is
consistent (no measurement errors), we can in principle solve exactly.
With noise, no exact solution exists — we instead minimize the squared
misfit between predicted and observed data.

**The least-squares objective:**

$$\min_{\mathbf{m}} \|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2$$

Setting the gradient to zero:

$$\mathbf{G}^T\mathbf{G}\mathbf{m} = \mathbf{G}^T\mathbf{d}$$

These are the **normal equations**. The least-squares solution is:

$$\boxed{\mathbf{m}_{LS} = (\mathbf{G}^T\mathbf{G})^{-1}\mathbf{G}^T\mathbf{d}}$$

**Geometric interpretation:** $\mathbf{G}\mathbf{m}_{LS}$ is the orthogonal
projection of $\mathbf{d}$ onto the column space of $\mathbf{G}$. We find the
model whose predicted data is as close as possible to the observations, in the
least-squares sense.

```{figure} ../figures/11_least_squares_geometry.png
---
width: 550px
alt: Geometric diagram showing the data vector d, the column space of G as a plane, and the least-squares solution as the orthogonal projection of d onto that plane.
---
Geometric interpretation of least squares. The data vector $\mathbf{d}$
(red) lives in $n$-dimensional data space. The column space of $\mathbf{G}$
(gray plane) contains all vectors that can be predicted by the model. The
least-squares solution $\mathbf{G}\mathbf{m}_{LS}$ (blue) is the orthogonal
projection of $\mathbf{d}$ onto this subspace. The residual vector
$\mathbf{d} - \mathbf{G}\mathbf{m}_{LS}$ (dashed) is perpendicular to the
column space.
```

---

## The Underdetermined Case: Minimum Norm

When $n < m$, the system has infinitely many solutions. Among all solutions
that fit the data exactly, the one with the **smallest norm** (shortest vector
in model space) is:

$$\mathbf{m}_{MN} = \mathbf{G}^T(\mathbf{G}\mathbf{G}^T)^{-1}\mathbf{d}$$

This is the **minimum norm solution**. While mathematically clean, it is
often physically wrong — for slip inversion it spreads the slip as broadly
as possible across all fault patches, rather than concentrating it where the
data actually demands it.

> **Question:** The minimum norm solution minimizes $\|\mathbf{m}\|^2$.
> For slip inversion, this means minimizing the total slip magnitude across
> all patches. Is this a good physical prior? What would a more geologically
> reasonable prior look like?

---

# Data Covariance and Weighted Least Squares

---

## Not All Data Are Equal

The simple least-squares solution treats all observations as equally reliable.
In practice:

- GNSS vertical offsets have larger uncertainties than horizontal offsets
- Near-fault GNSS stations have larger signal-to-noise than far-field stations  
- InSAR pixels in urban areas are more coherent than those over vegetation
- Different datasets (GNSS, InSAR, HR-GNSS) have fundamentally different error
  characteristics

The **data covariance matrix** $\mathbf{C}_d$ encodes these uncertainties:

$$C_d^{ij} = \text{cov}(d_i, d_j) = \begin{cases}
\sigma_i^2 & i = j \quad \text{(variance of observation } i\text{)} \\
\rho_{ij}\sigma_i\sigma_j & i \neq j \quad \text{(covariance between observations)}
\end{cases}$$

For uncorrelated data with known uncertainties $\sigma_i$, $\mathbf{C}_d$
is diagonal:

$$\mathbf{C}_d = \begin{pmatrix} \sigma_1^2 & & \\ & \ddots & \\ & & \sigma_n^2 \end{pmatrix}$$

---

## Weighted Least Squares

Observations with smaller variance should count more. The **weighted least
squares** objective down-weights uncertain observations:

$$\min_{\mathbf{m}} (\mathbf{G}\mathbf{m} - \mathbf{d})^T \mathbf{C}_d^{-1}
(\mathbf{G}\mathbf{m} - \mathbf{d})$$

The solution is:

$$\boxed{\mathbf{m}_{WLS} = (\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G})^{-1}
\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{d}}$$

For diagonal $\mathbf{C}_d$ this is equivalent to dividing each equation by
$\sigma_i$ before solving — a data with smaller uncertainty receives more weight.

---

## The InSAR Covariance Structure

InSAR data is spatially correlated — adjacent pixels share atmospheric noise
and orbital errors, so their residuals are not independent. The off-diagonal
terms of $\mathbf{C}_d$ are non-negligible.

A common model for InSAR spatial covariance is an exponential decay:

$$C_d^{ij} = \sigma^2 \exp\!\left(-\frac{d_{ij}}{L}\right)$$

where $d_{ij}$ is the distance between pixels $i$ and $j$ and $L$ is the
correlation length (typically 10–50 km for atmospheric noise).

```{figure} ../figures/11_insar_covariance.png
---
width: 650px
alt: A variogram showing the variance of InSAR phase as a function of pixel separation, with the fitted exponential covariance model.
---
InSAR covariance structure estimated from an earthquake interferogram. The
variance (semi-variogram) increases with pixel separation and saturates at
the spatially uncorrelated noise level $\sigma^2$. The correlation length $L$
is estimated from the slope at the origin. This structure must be accounted
for to avoid overweighting the dense InSAR data relative to the sparse GNSS.
```

👉 Ignoring InSAR covariance structure typically **overweights the InSAR data**
relative to GNSS — the millions of InSAR pixels are not millions of independent
observations; their effective number of independent data points is much smaller.

---

## Combining Multiple Datasets

When combining GNSS, InSAR ascending, and InSAR descending data, the combined
data vector and covariance matrix are block-diagonal:

$$\mathbf{d} = \begin{pmatrix}\mathbf{d}_{GNSS}\\ \mathbf{d}_{InSAR,asc}\\ \mathbf{d}_{InSAR,dsc}\end{pmatrix}, \quad
\mathbf{C}_d = \begin{pmatrix}\mathbf{C}_{GNSS} & & \\ & \mathbf{C}_{asc} & \\ & & \mathbf{C}_{dsc}\end{pmatrix}$$

The relative weighting between datasets is controlled by the ratio of their
noise levels — not by the number of observations. This is why careful
estimation of $\mathbf{C}_d$ is as important as the inversion itself.

---

# Regularization

---

## Why We Need It

Even with carefully weighted data, $\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G}$
is typically singular or nearly singular for the slip inversion problem.
This happens because:

- the fault has more patches than independent data constraints
- deep patches produce broad surface signals that look similar to each other
- the data coverage is spatially uneven

Attempting to invert a nearly singular matrix amplifies noise catastrophically.
We need to add information.

**Regularization** adds a penalty term to the objective function that
encodes our prior expectation about what a reasonable model looks like.
The two most common forms are damping and smoothing.

---

## Damping (Tikhonov Regularization)

**Damping** penalizes the size of the model — it says "prefer small slip values."

The augmented system:

$$\begin{bmatrix}\mathbf{G}\\ \lambda\mathbf{I}\end{bmatrix}\mathbf{m}
= \begin{bmatrix}\mathbf{d}\\ \mathbf{0}\end{bmatrix}$$

This minimizes the objective:

$$\|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2 + \lambda^2\|\mathbf{m}\|^2$$

The solution:

$$\mathbf{m}_{damp} = (\mathbf{G}^T\mathbf{G} + \lambda^2\mathbf{I})^{-1}
\mathbf{G}^T\mathbf{d}$$

The regularization parameter $\lambda$ controls the trade-off: large $\lambda$
forces the model toward zero (small slip everywhere); small $\lambda$ lets
the data drive the solution.

**Physical meaning:** damping is appropriate when we expect the true slip
to be small and concentrated. It stabilizes the inversion by pulling
unreasonably large slip values back toward zero.

**Limitation:** damping does not prevent spatially rough solutions —
adjacent patches can have wildly different slip values even with heavy damping.

---

## Smoothing (Laplacian Regularization)

**Smoothing** penalizes the roughness of the model — it says "prefer spatially
smooth slip distributions."

The penalty term uses the **finite difference Laplacian** $\mathbf{L}$:

$$\nabla^2 m_j \approx 0.25(m_{left} + m_{right} + m_{up} + m_{down}) - m_j$$

The augmented system:

$$\begin{bmatrix}\mathbf{G}\\ \lambda\mathbf{L}\end{bmatrix}\mathbf{m}
= \begin{bmatrix}\mathbf{d}\\ \mathbf{0}\end{bmatrix}$$

This minimizes:

$$\|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2 + \lambda^2\|\mathbf{L}\mathbf{m}\|^2$$

The solution:

$$\mathbf{m}_{smooth} = (\mathbf{G}^T\mathbf{G} + \lambda^2\mathbf{L}^T\mathbf{L})^{-1}
\mathbf{G}^T\mathbf{d}$$

```{figure} ../figures/11_damping_vs_smoothing.png
---
width: 720px
alt: Two inverted slip distributions for the same synthetic data — one using damping (left) showing noisy, small-amplitude patches, and one using smoothing (right) showing a coherent, spatially smooth asperity.
---
Damping vs. smoothing regularization for a synthetic slip inversion. **Left:**
damped solution — slip is small everywhere but can still be spatially rough.
**Right:** smoothed solution — the spatial pattern is physically coherent and
the asperity is clearly recovered, at the cost of slightly blurring its edges.
For most slip inversions, smoothing is preferred because it produces
geologically interpretable results.
```

**Physical meaning:** smoothing is the more geologically appropriate prior
for slip inversion — real fault slip distributions are spatially coherent,
not random patch by patch.

**Limitation:** heavy smoothing blurs sharp features. An asperity much
smaller than the spatial resolution of the data will be smeared over a
larger area.

---

## Damping vs. Smoothing: When to Use Each

| | Damping | Smoothing |
|---|---|---|
| **Penalty** | $\|\mathbf{m}\|^2$ — size of model | $\|\mathbf{L}\mathbf{m}\|^2$ — roughness |
| **Preferred when** | Slip expected to be small, localized | Slip expected to be spatially coherent |
| **Risk** | Can produce rough, patchy solutions | Can blur real sharp features |
| **Typical use** | SSEs (small, distributed slip) | Coseismic earthquakes |
| **Physical prior** | "Prefer small slip" | "Prefer smooth slip" |

In practice, both are often used together, with separate weights.

---

# The L-Curve

---

## Choosing the Regularization Parameter

The regularization parameter $\lambda$ controls the trade-off between:
- **Data misfit:** $\|\mathbf{G}\mathbf{m} - \mathbf{d}\|^2$ (how well we
  fit the observations)
- **Model norm or roughness:** $\|\mathbf{m}\|^2$ or $\|\mathbf{L}\mathbf{m}\|^2$
  (how geologically reasonable the solution is)

How do we choose $\lambda$? Too small → noisy, over-fitted model. Too large
→ over-smoothed, under-fitted model.

The **L-curve** plots model norm (or roughness) vs. data misfit as $\lambda$
varies:

```{figure} ../figures/11_L_curve.png
---
width: 600px
alt: An L-shaped curve plotting model roughness on the vertical axis against data misfit on the horizontal axis, with the optimal lambda at the corner of the L.
---
The L-curve. Each point on the curve corresponds to a different value of $\lambda$.
The upper-left region (large $\lambda$) gives smooth models with poor data fit.
The lower-right region (small $\lambda$) gives rough models with excellent data fit
but amplified noise. The optimal $\lambda$ is at the **corner** of the L — the
point of maximum curvature, which balances fit and smoothness. After Hansen (1992).
```

**The corner of the L** is the point of maximum curvature — where further
decreasing $\lambda$ produces rapidly increasing roughness with only marginal
improvement in fit. This is the optimal regularization parameter.

> **Note:** the L-curve method is a heuristic, not a guarantee. For well-behaved
> problems it works well; for strongly underdetermined problems it can be
> ambiguous. Cross-validation and Bayesian methods provide more rigorous
> alternatives but require more computation.

---

## Practical Note

It is never worth trying to fit the data perfectly, because all data contain
noise. An over-fitted model ($\lambda$ too small) fits the noise rather than
the signal, producing slip patches that are artifacts of measurement error
rather than real fault behavior.

👉 **A good regularization parameter produces a model that explains the data
to within the level of its estimated uncertainties — not better, not worse.**

---

# Resolution and Uncertainty

---

## The Resolution Matrix

After solving the regularized system, it is essential to ask: **what spatial
scale of slip can we actually resolve?** The answer is encoded in the
**resolution matrix** $\mathbf{R}$.

For the smoothed least-squares solution:

$$\mathbf{m}_{smooth} = \underbrace{(\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G}
+ \lambda^2\mathbf{L}^T\mathbf{L})^{-1}\mathbf{G}^T\mathbf{C}_d^{-1}}_{\mathbf{M}}\mathbf{d}$$

Substituting $\mathbf{d} = \mathbf{G}\mathbf{m}_{true} + \boldsymbol{\epsilon}$:

$$\mathbf{m}_{smooth} = \underbrace{\mathbf{M}\mathbf{G}}_{\mathbf{R}}\mathbf{m}_{true}
+ \mathbf{M}\boldsymbol{\epsilon}$$

The **resolution matrix** is:

$$\boxed{\mathbf{R} = (\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G}
+ \lambda^2\mathbf{L}^T\mathbf{L})^{-1}\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G}}$$

If $\mathbf{R} = \mathbf{I}$ (identity matrix), the recovered model equals
the true model perfectly — perfect resolution. In practice $\mathbf{R}
\neq \mathbf{I}$: the recovered model is a **blurred version** of the
true model, where the blurring kernel is given by the rows of $\mathbf{R}$.

---

## Interpreting the Resolution Matrix

The $j$-th row of $\mathbf{R}$ is the **resolution kernel** for patch $j$ —
it tells us that what we call "slip on patch $j$" is actually a weighted
average of the true slip on patches nearby $j$.

```{figure} ../figures/11_resolution_matrix.png
---
width: 720px
alt: Left panel showing the full resolution matrix as an image with bright diagonal elements; right panel showing two rows of the matrix as maps on the fault surface, illustrating how shallow patches are well resolved while deep patches are smeared.
---
**Left:** the resolution matrix $\mathbf{R}$ displayed as an image. A perfect
diagonal would mean perfect resolution. Off-diagonal elements indicate
trade-offs between patches. **Right:** two rows of $\mathbf{R}$ plotted as
resolution kernels on the fault surface. The shallow patch (top) is well
resolved — the kernel is compact. The deep patch (bottom) is poorly resolved
— the kernel is broad, meaning its recovered slip is an average over a large
fault area.
```

**Key insight:** resolution degrades with depth. Shallow patches, which
produce sharp surface signals, are well resolved. Deep patches, which
produce broad smooth signals, are poorly resolved — their slip trades off
with the slip on neighboring patches.

---

## The Model Covariance Matrix

The resolution matrix tells us about blurring from regularization. The
**model covariance matrix** $\mathbf{C}_m$ tells us about the uncertainty
from data noise:

$$\mathbf{C}_m = \mathbf{M}\mathbf{C}_d\mathbf{M}^T = 
(\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G} + \lambda^2\mathbf{L}^T\mathbf{L})^{-1}
\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G}
(\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G} + \lambda^2\mathbf{L}^T\mathbf{L})^{-T}$$

The diagonal elements of $\mathbf{C}_m$ give the **variance** of each
patch slip estimate. The off-diagonal elements give the **covariance**
(trade-off) between patch slip estimates.

| | Measures | Controlled by |
|---|---|---|
| $\mathbf{R}$ | Blurring (regularization effect) | $\lambda$, data coverage |
| $\mathbf{C}_m$ | Uncertainty (noise propagation) | Data noise, $\lambda$ |

👉 A good solution has both compact resolution kernels (small regularization
blurring) and small model covariance (small uncertainty). These two goals
trade off against each other — increasing $\lambda$ shrinks $\mathbf{C}_m$
but broadens $\mathbf{R}$.

---

# Connecting to Slip Inversion

---

## Everything Together: The Full System

For a joint GNSS + InSAR + non-negativity slip inversion with smoothing:

$$\min_{\mathbf{m} \geq 0}
\underbrace{(\mathbf{G}\mathbf{m} - \mathbf{d})^T\mathbf{C}_d^{-1}(\mathbf{G}\mathbf{m} - \mathbf{d})}_{\text{weighted data misfit}}
+ \underbrace{\lambda^2\|\mathbf{L}\mathbf{m}\|^2}_{\text{smoothing}}$$

subject to $m_j \geq 0$ for all patches (slip cannot be negative for a
prescribed rake direction).

The non-negativity constraint is added because we know the direction of slip
on a fault and we do not want the inversion to recover back-slip as a way
of fitting noise. This constraint makes the problem slightly nonlinear
(it becomes a non-negative least squares or quadratic programming problem),
but efficient algorithms exist.

---

## What the Tomography Example Taught Us

The seismic tomography problem and the slip inversion problem share the same
mathematical structure. From the tomography analogy we learned:

- **Blocks with many crossing rays** → well-resolved (analogous to shallow
  fault patches with dense near-field GNSS and InSAR coverage)
- **Blocks with few rays, or rays all in one direction** → poorly resolved
  (analogous to deep fault patches or areas with sparse data)
- **The resolution matrix rows** reveal exactly which model parameters are
  well constrained and which are smeared averages over a large area

```{figure} ../figures/11_tomo_ray_coverage.png
---
width: 650px
alt: Two panels showing a tomography model — on the left the ray coverage showing which blocks are crossed by many rays vs. few, and on the right the recovered velocity model showing well-resolved central blocks and poorly resolved corner blocks with few rays.
---
Ray coverage controls resolution in tomography — and data coverage controls
resolution in slip inversion. Blocks crossed by many rays at varied angles
are well resolved; blocks at the edges of the model with few ray paths are
poorly constrained. The same principle applies to fault patches: shallow
patches near dense GNSS networks are well resolved; deep patches far from
the data are not.
```

---

## Looking Ahead

In the next two lectures we will apply this framework to real problems:

**Lecture 12 — Cascadia SSE slip inversion (GNSS only):**
A clean first application — one dataset, well-constrained fault geometry,
spatially smooth slow slip. We will:
- build the Green's function matrix for the Cascadia subduction interface
- choose the regularization parameter using the L-curve
- recover the SSE slip distribution and interpret the resolution matrix

**Lecture 13 — Ridgecrest joint inversion (GNSS + InSAR + HR-GNSS):**
The full multi-dataset case. We will:
- combine three datasets with different noise characteristics
- show how the InSAR constrains the shallow near-fault slip that GNSS misses
- discuss what HR-GNSS adds beyond the static offset (rupture propagation)

---

# Summary

- The **inverse problem** $\mathbf{d} = \mathbf{G}\mathbf{m}$ asks for the
  model $\mathbf{m}$ given data $\mathbf{d}$ and Green's functions $\mathbf{G}$.
  Unlike the forward problem, the solution may not exist, may not be unique,
  and is typically unstable with respect to noise.

- The **least-squares solution** $\mathbf{m} = (\mathbf{G}^T\mathbf{G})^{-1}
  \mathbf{G}^T\mathbf{d}$ minimizes the squared misfit. For underdetermined or
  ill-conditioned systems it amplifies noise and fails in practice.

- The **data covariance matrix** $\mathbf{C}_d$ encodes measurement uncertainties
  and correlations. The **weighted least-squares** solution down-weights uncertain
  observations and properly handles correlated InSAR data.

- **Damping** (Tikhonov regularization) adds $\lambda^2\|\mathbf{m}\|^2$ to
  the objective — it prefers small slip. **Smoothing** adds $\lambda^2\|
  \mathbf{L}\mathbf{m}\|^2$ — it prefers spatially coherent slip. Both are
  controlled by the regularization parameter $\lambda$.

- The **L-curve** plots model roughness vs. data misfit as $\lambda$ varies.
  The optimal $\lambda$ is at the corner of the L — the point of maximum
  curvature that balances fit against physical reasonableness.

- The **resolution matrix** $\mathbf{R} = \mathbf{M}\mathbf{G}$ describes
  how the regularized inversion blurs the true model. A perfect diagonal
  $\mathbf{R} = \mathbf{I}$ means perfect resolution. In practice, deep
  patches are poorly resolved and their recovered slip is a smeared average
  of the true distribution.

- The **model covariance** $\mathbf{C}_m$ describes how data noise propagates
  into model uncertainty. Its diagonal elements give the variance of each
  slip estimate. Resolution and covariance trade off against each other as
  $\lambda$ is varied.

- The seismic tomography problem and the geodetic slip inversion problem are
  **mathematically identical** — the same equations, the same failure modes,
  and the same solutions apply to both.

---

# Additional Resources

> **Textbook:** [Geophysical Inverse Theory](https://press.princeton.edu/books/hardcover/9780691036342/geophysical-inverse-theory)  
> Menke, W. (2018, 2nd ed.). Princeton University Press. The standard graduate reference for inverse theory in geophysics.

> **Textbook:** [Parameter Estimation and Inverse Problems](https://doi.org/10.1016/C2009-0-61134-X)  
> Aster, R. C., Borchers, B., & Thurber, C. H. (2019, 3rd ed.). Academic Press. More accessible than Menke; excellent on regularization and the L-curve.

> **Classic paper:** [Analysis of discrete ill-posed problems by means of the L-curve](https://doi.org/10.1137/1034115)  
> Hansen, P. C. (1992). *SIAM Review*, 34(4), 561–580. The definitive paper on the L-curve method.

> **Review:** [Geodetic slip inversions — a review of methods](https://doi.org/10.1146/annurev-earth-053018-060600)  
> Bürgmann, R. (2018). The interseismic coupling of the Cascadia megathrust. *Annual Review of Earth and Planetary Sciences* — useful context for the next lecture.

> **Software:** [scipy.optimize.nnls](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.nnls.html)  
> Non-negative least squares solver used in the inversion lab.

---

# Sources

- Menke, W. (2018). *Geophysical Inverse Theory* (2nd ed.). Princeton University Press.
- Aster, R. C., Borchers, B., & Thurber, C. H. (2019). *Parameter Estimation and Inverse Problems* (3rd ed.). Academic Press.
- Hansen, P. C. (1992). Analysis of discrete ill-posed problems by means of the L-curve. *SIAM Review*, 34(4), 561–580. https://doi.org/10.1137/1034115
- Shearer, P. M. (2019). *Introduction to Seismology* (3rd ed.). Cambridge University Press.
- Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter Estimation*. SIAM. https://doi.org/10.1137/1.9780898717921
