#!/usr/bin/env python3
"""
PHYC54 Test Suite: Symbolic Euler-Lagrange Compiler Verification.
"""

import sympy as sp
from symbolic_euler_lagrange_compiler import compile_euler_lagrange

def test_compiler():
    t = sp.Symbol("t", real=True)
    m = sp.Symbol("m", positive=True)
    k = sp.Symbol("k", positive=True)
    x = sp.Function("x")(t)

    # 1. 1D SHO
    L = sp.Rational(1, 2) * m * x.diff(t)**2 - sp.Rational(1, 2) * k * x**2
    eq = compile_euler_lagrange(L, [x], t)[0]
    expected = m * x.diff(t, 2) + k * x
    assert sp.simplify(eq - expected) == 0, f"SHO compilation failed: {eq} != {expected}"
    print("  ✓ Harmonic oscillator Euler-Lagrange compilation verified.")

    # 2. Free particle (L = 1/2 m v^2) -> m * a = 0
    L_free = sp.Rational(1, 2) * m * x.diff(t)**2
    eq_free = compile_euler_lagrange(L_free, [x], t)[0]
    assert sp.simplify(eq_free - m * x.diff(t, 2)) == 0
    print("  ✓ Free particle Euler-Lagrange compilation verified.")

if __name__ == "__main__":
    print("=== Running PHYC54 Lagrangian Compiler Tests ===")
    test_compiler()
    print("🎉 All compiler tests passed successfully!")
