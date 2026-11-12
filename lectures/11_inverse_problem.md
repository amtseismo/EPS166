# The Inverse Problem Continued: Finding Fault Slip from Surface Observations

## Purpose

In this lecture we continue our discussion of inverse problems.

By the end you will be able to:

- use the L-curve to choose how much regularization to apply
- understand how to weight data to account for uncertainties
- interpret the resolution matrix to honestly assess what your inversion recovered

You will implement all of this in the corresponding lab.

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

---

## Why is it L-shaped?

The shape arises because there are two qualitatively different regimes of what
the inversion is doing as $\lambda$ varies — not one continuous slider.

**Regime 1 — the horizontal arm (large $\lambda$):** The inversion is fitting
the *signal* — the real, coherent pattern of surface displacement driven by
fault slip. Each reduction in $\lambda$ buys a large improvement in data fit
at a moderate cost in roughness. The curve moves steeply leftward because you
are making genuine progress: each step in $\lambda$ unlocks more signal.

**Regime 2 — the vertical arm (small $\lambda$):** The signal has already been
fit. Further reductions in $\lambda$ only let the inversion chase *noise*
— random, spatially incoherent measurement errors. Fitting random noise is
geometrically expensive: a spatially random function requires a very rough
model. So for tiny gains in misfit, roughness explodes upward. The curve
shoots nearly vertically because you are paying an enormous roughness price
for almost no improvement in fit.

**The corner is the transition point between these two regimes** — the last
good buy before the marginal cost of better data fit becomes prohibitive. That
is what makes it the optimal $\lambda$.

The two ends describe where you are on the curve, but neither explains the
shape. The shape comes from the existence of a sharp transition — which only
happens when noise is present (see below).

> **Rule of thumb:** A well-regularized solution should fit the data to within
> roughly its noise level. If residuals are much smaller than measurement
> uncertainties, you are fitting noise. If they are much larger, you are
> over-smoothing.

---

## Why Noise Creates the L-curve Corner

The L-curve only has a corner when data contain noise.

**Without noise** — there is only Regime 1. Every reduction in $\lambda$ buys
real signal, all the way to $\lambda = 0$ where the misfit reaches zero. There
is no transition to a second regime, because there is no noise to fit. The
roughness-vs-misfit tradeoff is a smooth, monotone curve with no kink.

**With noise** — the noise creates a **floor** in the data misfit. Here is
why the floor exists: measurement noise is spatially random, and random noise
*cannot* be reproduced by any physically plausible slip distribution without
making the model extremely rough. So once the inversion has fit everything that
can be fit with a smooth model — the signal — the remaining misfit is
irreducible without a catastrophic penalty in roughness. That irreducible
minimum is the noise floor: approximately the total variance of the measurement
errors, $\sum_i \sigma_i^2$.

Once $\lambda$ is small enough that the solution reaches this floor, Regime 2
begins. Any further reduction in $\lambda$ barely moves the misfit (you are
already at the floor) but roughness shoots up as the model starts fitting the
spatial pattern of the noise. The sharp change in the trade-off rate is the
corner.

**Without noise the floor is at zero; the two regimes merge into one; the
corner disappears.**

> **The corner marks the $\lambda$ at which the solution first reaches the
> noise floor** — fitting the data to within its noise level, and no further.

```{figure} ../figures/10_two_lcurve.png
---
name: fig-l-curve-noise
width: 700px
alt: Two L-curves on the same axes — one for noiseless data showing a
  smooth continuous curve with no corner, one for noisy data showing a
  clear L-shaped bend.
---
The same inversion run on noiseless data (blue) and noisy data (red,
$\sigma = 2$ mm). Without noise the curve slopes continuously — no corner.
With noise a clear bend appears. The corner of the noisy curve is the
optimal $\lambda$: the solution is fitting the signal without yet fitting
the noise.
```

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

## The Resolution Matrix

**How faithfully can the inversion recover slip on each fault patch?**

Write the regularized inversion as $\mathbf{m}_{est}=\mathbf{M}\mathbf{d}$.
Substituting $\mathbf{d}=\mathbf{G}\mathbf{m}_{true}+\boldsymbol{\varepsilon}$ gives

$$
\mathbf{m}_{est}
=
\underbrace{\mathbf{M}\mathbf{G}}_{\mathbf{R}}
\mathbf{m}_{true}
+
\mathbf{M}\boldsymbol{\varepsilon}.
$$

The **resolution matrix** $\mathbf{R}$ describes how the inversion
transforms the true slip pattern. The second term describes how data
noise enters the estimated slip.

For a single patch $j$,

$$
(m_{est})_j
=
\sum_{k=1}^{N} R_{jk}(m_{true})_k
+
(\mathbf{M}\boldsymbol{\varepsilon})_j.
$$

**Row $j$ of $\mathbf{R}$ contains the weights linking true slip across
the fault to the estimated slip on patch $j$.** Plotting these weights
on the fault gives its *resolution kernel*.

- **Red:** true slip here contributes positively to the estimate on patch $j$.
- **Blue:** true slip here contributes negatively.
- **White:** true slip here has little influence on that estimate.

These weights are not probabilities and need not sum to one.

---

## Building Intuition 

Imagine the true slip distribution has a sharp asperity on a deep patch —
say, 10 m of slip concentrated on one patch, and zero slip on the patches
around it. Ideally the inversion would report 10 m on that patch and 0 m
on its neighbors. But because the patch is deep, its surface signal is
broad and smooth, and looks almost identical to the signal you would get
from spreading the same total slip over three or four neighboring patches.
The inversion cannot tell the difference.

What it actually reports might look something like this — a row of the
resolution matrix for that patch:

$$\mathbf{R}_j = [\cdots,\ 0.1,\ 0.2,\ 0.4,\ 0.2,\ 0.1,\ \cdots]$$

Read this as a recipe: our estimate for patch $j$ is built from

$$(\mathbf{m}_{est})_j = \cdots + 0.1\,m_{\text{left-left}}
+ 0.2\,m_{\text{left}}
+ 0.4\,m_j
+ 0.2\,m_{\text{right}}
+ 0.1\,m_{\text{right-right}} + \cdots$$

With the true slip being 10 m on patch $j$ and 0 m everywhere else, the
inversion reports:

$$(\mathbf{m}_{est})_j = 0.1(0) + 0.2(0) + 0.4(10) + 0.2(0) + 0.1(0) = 4\ \text{m}$$

The inversion finds only 4 m where the true slip was 10 m. The rest has
been smeared onto neighbouring patches — each of which will also report a
few meters of slip even though none actually occurred there. The total
moment is roughly preserved, but the spatial pattern is wrong.

Now consider a shallow patch under the same network. Its surface signal is
sharp and distinctive — no neighboring patch produces anything like it. Its
resolution kernel might look like:

$$\mathbf{R}_j = [\cdots,\ 0.0,\ 0.05,\ 0.90,\ 0.05,\ 0.0,\ \cdots]$$

The same calculation gives $(\mathbf{m}_{est})_j = 0.90 \times 10 = 9$ m —
close to the truth, with only minor leakage into neighbors.

The resolution matrix quantifies this patch by patch for the whole fault.
A row close to a row of the identity matrix (one large value on the
diagonal, near-zeros elsewhere) means that patch is well resolved. A row
with weight spread broadly across many patches means the inversion is
averaging over a large area, and any feature smaller than that averaging
width is invisible.

---

## What does good resolution look like?

**Perfect resolution:** $\mathbf{R}=\mathbf{I}$. Each patch has a weight
of one on itself and zero everywhere else.

**Good resolution:** a kernel concentrated at the target patch, with
a self-weight near one and little contribution from other patches.

**Poor resolution:** a broad or displaced kernel, potentially with
negative sidelobes. The estimated slip mixes contributions from
different parts of the fault and may suppress or distort real features.

> **A smooth recovered slip model does not necessarily mean the true
> slip was smooth—it may reflect limited resolution.**

```{figure} ../figures/10_resolution_matrix.png
---
name: fig-resolution-matrix
width: 800px
alt: Six panels showing true slip, recovered slip, their difference,
  the resolution matrix, and resolution kernels for shallow and deep patches.
---
**Top:** True slip, recovered slip, and their difference illustrate
the loss or distortion of spatial detail. **Bottom:** The resolution
matrix and two example row kernels show which parts of the true model
contribute to each target patch's estimate. Stars mark the target
patches. A compact kernel centered on its target indicates better
localization; a broad or displaced kernel indicates mixing across
the fault. Red and blue show positive and negative weights, respectively.
```

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

# Summary

- The **regularization parameter $\lambda$** is chosen using the **L-curve**: plot
  model roughness vs. data misfit for a range of $\lambda$ values, and choose the
  corner. The optimal solution fits the data to within its noise level.
  
- The **data covariance matrix** $\mathbf{C}_d$ encodes measurement uncertainties.
  **Weighted least squares** down-weights noisy observations and up-weights precise
  ones, preventing one noisy dataset from dominating the inversion.
  
- The **resolution matrix** Tells you how well the inversion can recover slip on any given fault patch.

---

# Additional Resources

> **Textbook:** Menke, W. (2018). *Geophysical Inverse Theory* (2nd ed.).
> Princeton University Press. The standard graduate reference.

> **Reference for this lecture:** Ide, S. (2007). Slip inversion. In
> *Treatise on Geophysics*, Vol. 4, pp. 193–223. Elsevier. Sections 4.07.2–4.07.4
> cover the formulation used here; Section 4.07.4 has the Chi-Chi comparison.


---

# Appendix — Derivation of the Resolution Matrix

For the smoothed, weighted least-squares inversion we have been building,
$\mathbf{M}$ is the matrix that maps data directly to slip estimates:

$$\mathbf{M} = (\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G}
+ \lambda^2\mathbf{L}^T\mathbf{L})^{-1}\mathbf{G}^T\mathbf{C}_d^{-1}$$

You can verify this is correct by substituting $\mathbf{d} = \mathbf{G}\mathbf{m}$
(the noiseless forward model) and checking that $\mathbf{M}\mathbf{d}$ gives back
the regularized least-squares solution $\mathbf{m}_{smooth}$ from Part 3. The
resolution matrix is then:

$$\mathbf{R} = \mathbf{M}\mathbf{G} =
(\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G}
+ \lambda^2\mathbf{L}^T\mathbf{L})^{-1}
\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G}$$

Notice what happens at the two extremes. When $\lambda = 0$ (no
regularization), $\mathbf{R}$ reduces to
$(\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G})^{-1}
\mathbf{G}^T\mathbf{C}_d^{-1}\mathbf{G} = \mathbf{I}$ — perfect resolution,
but an unstable inversion. As $\lambda \to \infty$ (heavy regularization),
the penalty term dominates and $\mathbf{R} \to \mathbf{0}$ — the inversion
ignores the data entirely and recovers nothing. The L-curve corner is the
balance between these two limits.
