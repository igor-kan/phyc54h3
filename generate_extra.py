import os

arnold_content = r"""---
title: "Arnold: Mathematical Methods of Classical Mechanics"
subtitle: "Summary notes for Chapters 1-4"
date: "2026-09-10"
categories: [arnold, classical-mechanics, math, extra]
format:
  html:
    toc: true
    math: true
---

# Overview

These are supplementary notes based on the first four chapters of Vladimir I. Arnold's *Mathematical Methods of Classical Mechanics*. Arnold's approach is highly geometric and rigorous, formulating mechanics in the language of manifolds, tangent bundles, and symplectic geometry.

## Chapter 1: Experimental Facts

Arnold begins by establishing the fundamental principles (axioms) of Newtonian mechanics in a highly abstract manner.

*   **Galilean Space and Time:** Space is an affine space $\mathbb{A}^3$ associated with the vector space $\mathbb{R}^3$, equipped with a Euclidean metric. Time is a one-dimensional affine space $\mathbb{A}^1$.
*   **Galilean Group:** The group of affine transformations of Galilean space-time that preserve time intervals and spatial distances between simultaneous events.
*   **Newton's Equation:** $\ddot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \dot{\mathbf{x}}, t)$. The fundamental experimental fact is that the initial state (position and velocity) completely determines the motion of a mechanical system.

## Chapter 2: Investigation of the Equations of Motion

This chapter investigates the behavior of solutions to Newton's equations, specifically focusing on conservative systems with one degree of freedom and the two-body problem.

*   **Systems with One Degree of Freedom:** The phase space is a plane $(x, y)$ where $y = \dot{x}$. The energy $E = \frac{1}{2}\dot{x}^2 + U(x)$ is conserved, leading to the phase curves being the level sets of $E(x, y)$.
*   **Central Force Fields:** The two-body problem is reduced to a one-body problem in a central field using the conservation of momentum and angular momentum.
*   **Kepler's Problem:** Arnold derives Kepler's laws by analyzing the effective potential $U_{\text{eff}}(r) = U(r) + \frac{M^2}{2r^2}$, highlighting the role of the centrifugal barrier.

## Chapter 3: The Principle of Least Action (Lagrangian Mechanics)

Arnold transitions from the Newtonian formulation in $\mathbb{R}^n$ to the Lagrangian formulation on smooth manifolds.

*   **Calculus of Variations:** The action functional is defined as $\Phi[\gamma] = \int_{t_0}^{t_1} L(t, \gamma(t), \dot{\gamma}(t)) \, dt$.
*   **Euler-Lagrange Equations:** The condition for stationarity ($\delta \Phi = 0$) yields the Euler-Lagrange equations $\frac{d}{dt} \frac{\partial L}{\partial \dot{q}} - \frac{\partial L}{\partial q} = 0$.
*   **Extremals on Manifolds (§12):** Geodesics on embedded surfaces (like cylinders, spheres, and cones) are viewed geometrically as auto-parallel curves. The calculus of variations is generalized to coordinate-free language on manifolds.

## Chapter 4: Conservation Laws

This chapter introduces the fundamental connection between symmetries and conservation laws (Noether's Theorem) in the Lagrangian formalism.

*   **Noether's Theorem:** If the Lagrangian is invariant under a one-parameter group of diffeomorphisms, there exists a corresponding first integral (conserved quantity).
*   **Energy, Momentum, and Angular Momentum:**
    *   Time translation invariance $\implies$ Conservation of Energy.
    *   Spatial translation invariance $\implies$ Conservation of Linear Momentum.
    *   Rotational invariance $\implies$ Conservation of Angular Momentum.
"""

math_methods_content = r"""---
title: "Math Methods: Prerequisites & Corequisites"
subtitle: "Mapping mathematical concepts to Taylor's Classical Mechanics (Chapter 6)"
date: "2026-09-10"
categories: [math-methods, classical-mechanics, extra, calculus-of-variations]
format:
  html:
    toc: true
    math: true
---

# Mathematical Foundations for Calculus of Variations

The following is a curated reading list mapping specific mathematical methods topics from standard textbooks (Boas, RHB, Arfken, Landau, Arnold) directly to the problem solving techniques required for Chapter 6 of Taylor's *Classical Mechanics*.

## Mary L. Boas — Mathematical Methods in the Physical Sciences

*   **Ch 4 (Sec 4.7): Differentiation of Integrals (Leibniz Rule)**
    *   *Prerequisite:* Differentiating parameterized functionals $\frac{d}{d\alpha} \int f \, dx$ through the integral sign.
*   **Ch 5 (Sec 5.4): Curvilinear Coordinates & Scale Factors**
    *   *Prerequisite:* Fast derivation of $ds^2 = \sum h_i^2 dq_i^2$ for the complete table of arc lengths (Problem 6.6).
*   **Ch 8 (Sec 8.1 – 8.5): Ordinary Differential Equations**
    *   *Prerequisite:* Separation of variables and 2nd-order characteristic equations (Problems 6.9, 6.11, 6.12, 6.17).
*   **Ch 9 (Sec 9.1 – 9.3): Calculus of Variations & First Integrals**
    *   *Corequisite:* Read in parallel with Taylor. Directly covers first integrals for $f(y', x)$ (Problem 6.10) and the Beltrami identity (Problems 6.20, 6.21).
*   **Ch 9 (Sec 9.4): Constrained Variation & Isoperimetric Problems**
    *   *Corequisite:* Mathematical formulation of Lagrange multipliers for Dido's maximum enclosed area with fixed string length (Problem 6.22).

## RHB — Mathematical Methods for Physics and Engineering

*   **Ch 10 (Sec 10.1 – 10.3): Vector Calculus & Curvilinear Systems**
    *   *Prerequisite:* Coordinate transformations between cylindrical, spherical, and conical metrics (Problems 6.1, 6.2, 6.16, 6.17).
*   **Ch 22 (Sec 22.1 – 22.3): Variational Calculus & Special Cases**
    *   *Corequisite:* Systematic algebraic classification of Euler–Lagrange first integrals (Problems 6.10, 6.16, 6.20, 6.21).
*   **Ch 22 (Sec 22.4): Constrained Variations**
    *   *Corequisite:* Integral equality constraints $\int \sqrt{1 + y'^2} \, ds = l$ (Problem 6.22).
*   **Ch 22 (Sec 22.5): Several Dependent / Independent Variables**
    *   *Corequisite:* Formal derivation of coupled Euler–Lagrange equations and 3D straight line geodesics (Problems 6.26, 6.27).

## Arfken, Weber, Harris — Mathematical Methods for Physicists

*   **Ch 3 (Sec 3.10): Curvilinear Coordinates and Metric Tensors**
    *   *Corequisite:* General framework for non-Euclidean metrics such as the rapidity metric $ds = \frac{2}{1-r^2}\sqrt{dr^2 + r^2 d\theta^2}$ (Problem 6.13).
*   **Ch 22 (Sec 22.1 – 22.2): Calculus of Variations & Multi-Variable Systems**
    *   *Corequisite:* Clean tensor/vector variation notation for problems with more than two variables (Problems 6.26, 6.27).

## Landau & Lifshitz — Mechanics (Vol. 1)

*   **Ch I (§2): The Principle of Least Action**
    *   *Corequisite:* Physical perspective on how path stationarity ($\delta S = 0$) works without coordinate artifacts.
*   **Ch II (§6): Symmetries & Conservation Laws**
    *   *Corequisite:* Deepens the connection between coordinate independence ($f$ independent of $q$) and conserved quantities (Problems 6.10, 6.16, 6.20).

## Vladimir Arnold — Mathematical Methods of Classical Mechanics

*   **Ch 3 (§12): Extremals of Integrals on Manifolds**
    *   *Advanced Corequisite:* Differential geometric perspective on geodesics as auto-parallel curves on embedded surfaces like cylinders, spheres, and cones (Problems 6.7, 6.16, 6.17).
"""

with open('/home/igorkan/repos/phyc54h3/extra/arnold-chapters-1-4.qmd', 'w') as f:
    f.write(arnold_content)

with open('/home/igorkan/repos/phyc54h3/extra/math-methods-taylor-ch6.qmd', 'w') as f:
    f.write(math_methods_content)

