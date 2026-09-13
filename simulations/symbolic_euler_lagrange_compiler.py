#!/usr/bin/env python3
"""
Symbolic Euler-Lagrange Compiler for Classical Mechanics.
Translates scalar Lagrangians L(q, q_dot, t) into explicit differential equations of motion.
"""

import sympy as sp

def compile_euler_lagrange(L, q_funcs, t):
    """
    Computes d/dt(dL/dq_dot) - dL/dq = 0 for a list of generalized coordinates.
    """
    eqs = []
    for q in q_funcs:
        q_dot = q.diff(t)
        dL_dq_dot = L.diff(q_dot)
        dt_dL_dq_dot = dL_dq_dot.diff(t)
        dL_dq = L.diff(q)
        eq = sp.simplify(dt_dL_dq_dot - dL_dq)
        eqs.append(eq)
    return eqs

if __name__ == "__main__":
    t = sp.Symbol("t", real=True)
    m = sp.Symbol("m", positive=True)
    k = sp.Symbol("k", positive=True)
    g = sp.Symbol("g", positive=True)
    l = sp.Symbol("l", positive=True)

    # 1. Simple Harmonic Oscillator
    x = sp.Function("x")(t)
    L_sho = sp.Rational(1, 2) * m * x.diff(t)**2 - sp.Rational(1, 2) * k * x**2
    sho_eq = compile_euler_lagrange(L_sho, [x], t)[0]

    print("=== PHYC54 Symbolic Euler-Lagrange Compiler ===")
    print(f"1. Harmonic Oscillator Lagrangian: L = {L_sho}")
    print(f"   Compiled Equation of Motion: {sho_eq} = 0")

    # 2. Simple Pendulum: theta
    theta = sp.Function("theta")(t)
    L_pendulum = sp.Rational(1, 2) * m * l**2 * theta.diff(t)**2 - m * g * l * (1 - sp.cos(theta))
    pend_eq = compile_euler_lagrange(L_pendulum, [theta], t)[0]

    print(f"\n2. Pendulum Lagrangian: L = {L_pendulum}")
    print(f"   Compiled Equation of Motion: {pend_eq} = 0")
