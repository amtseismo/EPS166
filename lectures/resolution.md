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