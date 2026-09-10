import os

# Base directory
base_dir = "/home/igorkan/repos/phyc54h3/extra"

# Remove the aggregated files
for f in ["arnold-chapters-1-4.qmd", "math-methods-taylor-ch6.qmd"]:
    filepath = os.path.join(base_dir, f)
    if os.path.exists(filepath):
        os.remove(filepath)

files_to_create = {
    "arnold-chapter-1.qmd": r"""---
title: "Arnold Chapter 1: Experimental Facts"
subtitle: "Newtonian Mechanics and Galilean Spacetime"
date: "2026-09-10"
categories: [arnold, classical-mechanics, math, extra]
format:
  html:
    toc: true
    math: true
---

# Overview

Arnold begins by establishing the fundamental principles (axioms) of Newtonian mechanics in a highly abstract manner.

*   **Galilean Space and Time:** Space is an affine space $\mathbb{A}^3$ associated with the vector space $\mathbb{R}^3$, equipped with a Euclidean metric. Time is a one-dimensional affine space $\mathbb{A}^1$.
*   **Galilean Group:** The group of affine transformations of Galilean space-time that preserve time intervals and spatial distances between simultaneous events.
*   **Newton's Equation:** $\ddot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \dot{\mathbf{x}}, t)$. The fundamental experimental fact is that the initial state (position and velocity) completely determines the motion of a mechanical system.
""",
    
    "arnold-chapter-2.qmd": r"""---
title: "Arnold Chapter 2: Investigation of the Equations of Motion"
subtitle: "Conservative Systems and the Two-Body Problem"
date: "2026-09-10"
categories: [arnold, classical-mechanics, math, extra]
format:
  html:
    toc: true
    math: true
---

# Overview

This chapter investigates the behavior of solutions to Newton's equations, specifically focusing on conservative systems with one degree of freedom and the two-body problem.

*   **Systems with One Degree of Freedom:** The phase space is a plane $(x, y)$ where $y = \dot{x}$. The energy $E = \frac{1}{2}\dot{x}^2 + U(x)$ is conserved, leading to the phase curves being the level sets of $E(x, y)$.
*   **Central Force Fields:** The two-body problem is reduced to a one-body problem in a central field using the conservation of momentum and angular momentum.
*   **Kepler's Problem:** Arnold derives Kepler's laws by analyzing the effective potential $U_{\text{eff}}(r) = U(r) + \frac{M^2}{2r^2}$, highlighting the role of the centrifugal barrier.
""",

    "arnold-chapter-3.qmd": r"""---
title: "Arnold Chapter 3: The Principle of Least Action"
subtitle: "Lagrangian Mechanics on Manifolds"
date: "2026-09-10"
categories: [arnold, classical-mechanics, math, extra, calculus-of-variations]
format:
  html:
    toc: true
    math: true
---

# Overview

Arnold transitions from the Newtonian formulation in $\mathbb{R}^n$ to the Lagrangian formulation on smooth manifolds.

*   **Calculus of Variations:** The action functional is defined as $\Phi[\gamma] = \int_{t_0}^{t_1} L(t, \gamma(t), \dot{\gamma}(t)) \, dt$.
*   **Euler-Lagrange Equations:** The condition for stationarity ($\delta \Phi = 0$) yields the Euler-Lagrange equations $\frac{d}{dt} \frac{\partial L}{\partial \dot{q}} - \frac{\partial L}{\partial q} = 0$.

## §12: Extremals of Integrals on Manifolds

**Advanced Corequisite for Taylor Chapter 6 (Problems 6.7, 6.16, 6.17)**

Provides a differential geometric perspective on geodesics as auto-parallel curves on embedded surfaces like cylinders, spheres, and cones. The calculus of variations is generalized to coordinate-free language on manifolds.
""",

    "arnold-chapter-4.qmd": r"""---
title: "Arnold Chapter 4: Conservation Laws"
subtitle: "Symmetries and Noether's Theorem"
date: "2026-09-10"
categories: [arnold, classical-mechanics, math, extra]
format:
  html:
    toc: true
    math: true
---

# Overview

This chapter introduces the fundamental connection between symmetries and conservation laws (Noether's Theorem) in the Lagrangian formalism.

*   **Noether's Theorem:** If the Lagrangian is invariant under a one-parameter group of diffeomorphisms, there exists a corresponding first integral (conserved quantity).
*   **Energy, Momentum, and Angular Momentum:**
    *   Time translation invariance $\implies$ Conservation of Energy.
    *   Spatial translation invariance $\implies$ Conservation of Linear Momentum.
    *   Rotational invariance $\implies$ Conservation of Angular Momentum.
""",

    "boas-chapter-4.qmd": r"""---
title: "Boas Chapter 4: Partial Differentiation"
subtitle: "Focus on Sec 4.7: Differentiation of Integrals (Leibniz Rule)"
date: "2026-09-10"
categories: [boas, math-methods, calculus, extra]
format:
  html:
    toc: true
    math: true
---

# Differentiation of Integrals (Leibniz Rule)

**Prerequisite for Taylor Chapter 6**

*   **Concept:** Differentiating parameterized functionals $\frac{d}{d\alpha} \int f \, dx$ through the integral sign.
*   **Application:** Crucial for understanding how to vary an integral path with respect to a parameter $\alpha$ when deriving the Euler-Lagrange equations.
""",

    "boas-chapter-5.qmd": r"""---
title: "Boas Chapter 5: Multiple Integrals"
subtitle: "Focus on Sec 5.4: Curvilinear Coordinates & Scale Factors"
date: "2026-09-10"
categories: [boas, math-methods, calculus, extra]
format:
  html:
    toc: true
    math: true
---

# Curvilinear Coordinates & Scale Factors

**Prerequisite for Taylor Chapter 6 (Problem 6.6)**

*   **Concept:** Fast derivation of the infinitesimal distance squared $ds^2 = \sum h_i^2 dq_i^2$.
*   **Application:** Required for constructing the complete table of arc lengths in various coordinate systems.
""",

    "boas-chapter-8.qmd": r"""---
title: "Boas Chapter 8: Ordinary Differential Equations"
subtitle: "Focus on Sec 8.1 – 8.5"
date: "2026-09-10"
categories: [boas, math-methods, differential-equations, extra]
format:
  html:
    toc: true
    math: true
---

# Ordinary Differential Equations

**Prerequisite for Taylor Chapter 6 (Problems 6.9, 6.11, 6.12, 6.17)**

*   **Concept:** Separation of variables and solving 2nd-order characteristic equations.
*   **Application:** Used to solve the resulting Euler-Lagrange differential equations analytically.
""",

    "boas-chapter-9.qmd": r"""---
title: "Boas Chapter 9: Calculus of Variations"
subtitle: "Focus on Sec 9.1 – 9.4"
date: "2026-09-10"
categories: [boas, math-methods, calculus-of-variations, extra]
format:
  html:
    toc: true
    math: true
---

# Calculus of Variations & First Integrals (Sec 9.1 – 9.3)

**Corequisite for Taylor Chapter 6 (Problems 6.10, 6.20, 6.21)**

*   **Concept:** Read in parallel with Taylor. Directly covers first integrals when the integrand is independent of the dependent variable $f(y', x)$ and the Beltrami identity when it's independent of the independent variable $f(y, y')$.

# Constrained Variation & Isoperimetric Problems (Sec 9.4)

**Corequisite for Taylor Chapter 6 (Problem 6.22)**

*   **Concept:** Mathematical formulation of Lagrange multipliers.
*   **Application:** Dido's problem of maximum enclosed area with a fixed string length.
""",

    "rhb-chapter-10.qmd": r"""---
title: "RHB Chapter 10: Vector Calculus"
subtitle: "Focus on Sec 10.1 – 10.3: Curvilinear Systems"
date: "2026-09-10"
categories: [rhb, math-methods, vector-calculus, extra]
format:
  html:
    toc: true
    math: true
---

# Vector Calculus & Curvilinear Systems

**Prerequisite for Taylor Chapter 6 (Problems 6.1, 6.2, 6.16, 6.17)**

*   **Concept:** Coordinate transformations between cylindrical, spherical, and conical metrics.
*   **Application:** Necessary for writing down the correct path length integrals $ds$ on curved surfaces.
""",

    "rhb-chapter-22.qmd": r"""---
title: "RHB Chapter 22: Calculus of Variations"
subtitle: "Focus on Sec 22.1 – 22.5"
date: "2026-09-10"
categories: [rhb, math-methods, calculus-of-variations, extra]
format:
  html:
    toc: true
    math: true
---

# Variational Calculus & Special Cases (Sec 22.1 – 22.3)

**Corequisite for Taylor Chapter 6 (Problems 6.10, 6.16, 6.20, 6.21)**

*   **Concept:** Systematic algebraic classification of Euler–Lagrange first integrals.

# Constrained Variations (Sec 22.4)

**Corequisite for Taylor Chapter 6 (Problem 6.22)**

*   **Concept:** Handling integral equality constraints like $\int \sqrt{1 + y'^2} \, ds = l$.

# Several Dependent / Independent Variables (Sec 22.5)

**Corequisite for Taylor Chapter 6 (Problems 6.26, 6.27)**

*   **Concept:** Formal derivation of coupled Euler–Lagrange equations and 3D straight line geodesics.
""",

    "arfken-chapter-3.qmd": r"""---
title: "Arfken Chapter 3: Vector Analysis"
subtitle: "Focus on Sec 3.10: Curvilinear Coordinates and Metric Tensors"
date: "2026-09-10"
categories: [arfken, math-methods, tensors, extra]
format:
  html:
    toc: true
    math: true
---

# Curvilinear Coordinates and Metric Tensors

**Corequisite for Taylor Chapter 6 (Problem 6.13)**

*   **Concept:** General framework for non-Euclidean metrics.
*   **Application:** Setting up the rapidity metric $ds = \frac{2}{1-r^2}\sqrt{dr^2 + r^2 d\theta^2}$.
""",

    "arfken-chapter-22.qmd": r"""---
title: "Arfken Chapter 22: Calculus of Variations"
subtitle: "Focus on Sec 22.1 – 22.2: Multi-Variable Systems"
date: "2026-09-10"
categories: [arfken, math-methods, calculus-of-variations, extra]
format:
  html:
    toc: true
    math: true
---

# Calculus of Variations & Multi-Variable Systems

**Corequisite for Taylor Chapter 6 (Problems 6.26, 6.27)**

*   **Concept:** Clean tensor/vector variation notation for problems with more than two variables.
""",

    "landau-chapter-2.qmd": r"""---
title: "Landau & Lifshitz Chapter II: Conservation Laws"
subtitle: "Focus on §6: Symmetries & Conservation Laws"
date: "2026-09-10"
categories: [landau, classical-mechanics, conservation-laws, extra]
format:
  html:
    toc: true
    math: true
---

# Symmetries & Conservation Laws

**Corequisite for Taylor Chapter 6 (Problems 6.10, 6.16, 6.20)**

*   **Concept:** Deepens the connection between coordinate independence (when the integrand $f$ is independent of a generalized coordinate $q$) and conserved quantities. Provides the profound physical reasoning behind the mathematical "first integrals" of the Euler-Lagrange equations.
"""
}

for filename, content in files_to_create.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "w") as f:
        f.write(content)

# We also need to update landau-chapter-1.qmd to explicitly mention §2
landau_1_path = os.path.join(base_dir, "landau-chapter-1.qmd")
if os.path.exists(landau_1_path):
    with open(landau_1_path, "r") as f:
        landau_content = f.read()
    
    if "The Principle of Least Action" not in landau_content:
        # Append it if missing
        append_content = r"""
## §2: The Principle of Least Action

**Corequisite for Taylor Chapter 6**

Provides the fundamental physical perspective on how path stationarity ($\delta S = 0$) works without coordinate artifacts. The principle of least action is the foundation from which Lagrange's equations are derived.
"""
        with open(landau_1_path, "a") as f:
            f.write(append_content)

