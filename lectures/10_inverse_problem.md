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
Surface displacement fingerprints (columns of **G**) for three fault patches at different depths. The shallow patch A (orange) produces a sharp, localized signal easily identified by the inversion. The two deep patches B and C produce broad, nearly identical signals — their columns in **G** are nearly parallel. When columns of **G** are nearly parallel, **G**ᵀ**G** becomes nearly singular and cannot be safely inverted. The inversion cannot distinguish slip on B from slip on C, so it may assign arbitrarily large and opposite values to both while still fitting the data at the surface.
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

---

# Additional Resources

> **Textbook:** Menke, W. (2018). *Geophysical Inverse Theory* (2nd ed.).
> Princeton University Press. The standard graduate reference.

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
