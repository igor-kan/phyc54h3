"""
Numerical Verification of Inertia Tensor Multilinear Algebra
PHYC54: Classical Mechanics

Validates:
1. Symmetry of the Inertia Tensor: I_{ij} == I_{ji}
2. Strict Positive Definiteness: omega^T I omega > 0 and Sylvester's criterion
3. Spectral Eigendecomposition and Principal Axes Orthogonality (R in SO(3))
4. Triangle Inequalities of Principal Moments of Inertia
5. Planar Lamina Exact Equality (Perpendicular Axis Theorem: I_1 + I_2 == I_3)
6. Non-Collinearity of L and omega vs Principal Axis Parallelism
"""

import numpy as np
import scipy.linalg as la


def compute_discrete_inertia_tensor(masses, positions):
    """
    Computes I_{ij} = sum_alpha m_alpha (delta_{ij} r_alpha^2 - r_{alpha, i} r_{alpha, j})
    """
    I = np.zeros((3, 3))
    delta = np.eye(3)
    for m, r in zip(masses, positions):
        r_sq = np.dot(r, r)
        I += m * (delta * r_sq - np.outer(r, r))
    return I


def test_inertia_symmetry_and_posdef():
    np.random.seed(42)
    # 10 random particles in 3D
    N = 10
    masses = np.random.uniform(0.5, 2.0, size=N)
    positions = np.random.uniform(-3.0, 3.0, size=(N, 3))

    I = compute_discrete_inertia_tensor(masses, positions)

    # 1. Symmetry
    assert np.allclose(I, I.T)

    # 2. Strict Positive Definiteness
    eigvals = np.linalg.eigvalsh(I)
    assert np.all(eigvals > 0)

    # 3. Sylvester's Criterion: all leading principal minors > 0
    assert I[0, 0] > 0
    assert np.linalg.det(I[:2, :2]) > 0
    assert np.linalg.det(I) > 0

    # 4. Kinetic energy quadratic form T = 0.5 * omega^T I omega > 0
    for _ in range(10):
        omega = np.random.randn(3)
        T_rot = 0.5 * omega.T @ I @ omega
        assert T_rot > 0


def test_spectral_principal_axes_and_triangle_inequalities():
    np.random.seed(123)
    N = 25
    masses = np.random.uniform(1.0, 5.0, size=N)
    positions = np.random.uniform(-5.0, 5.0, size=(N, 3))

    I = compute_discrete_inertia_tensor(masses, positions)

    # Eigendecomposition
    eigvals, R = np.linalg.eigh(I)
    I1, I2, I3 = eigvals

    # Principal axes matrix R must be orthogonal
    assert np.allclose(R.T @ R, np.eye(3))
    # Check orientation (ensure det = 1 for SO(3))
    if np.linalg.det(R) < 0:
        R[:, 0] *= -1
    assert np.isclose(np.linalg.det(R), 1.0)

    # Diagonalization
    I_diag = R.T @ I @ R
    assert np.allclose(I_diag, np.diag(eigvals))

    # Triangle Inequalities
    assert (I1 + I2) >= I3 - 1e-12
    assert (I2 + I3) >= I1 - 1e-12
    assert (I1 + I3) >= I2 - 1e-12


def test_planar_lamina_perpendicular_axis_theorem():
    np.random.seed(456)
    # Particles strictly in the z=0 plane
    N = 15
    masses = np.random.uniform(0.5, 3.0, size=N)
    positions = np.zeros((N, 3))
    positions[:, :2] = np.random.uniform(-4.0, 4.0, size=(N, 2)) # z=0

    I = compute_discrete_inertia_tensor(masses, positions)

    # Eigendecomposition
    eigvals = np.linalg.eigvalsh(I)
    # In planar lamina, I_zz = I_xx + I_yy
    assert np.isclose(I[2, 2], I[0, 0] + I[1, 1])
    # The largest principal moment must equal the sum of the two smaller ones
    sorted_eig = np.sort(eigvals)
    assert np.isclose(sorted_eig[0] + sorted_eig[1], sorted_eig[2])


def test_angular_momentum_collinearity():
    np.random.seed(789)
    # Distinct moments of inertia
    I = np.diag([2.0, 5.0, 9.0])

    # Along principal axis 1: omega = [1, 0, 0]
    omega_p1 = np.array([1.0, 0.0, 0.0])
    L_p1 = I @ omega_p1
    cross_p1 = np.cross(L_p1, omega_p1)
    assert np.allclose(cross_p1, 0.0) # Parallel!

    # Off-axis: omega = [1, 1, 1]
    omega_off = np.array([1.0, 1.0, 1.0])
    L_off = I @ omega_off
    cross_off = np.cross(L_off, omega_off)
    assert not np.allclose(cross_off, 0.0) # Not parallel!


if __name__ == "__main__":
    test_inertia_symmetry_and_posdef()
    test_spectral_principal_axes_and_triangle_inequalities()
    test_planar_lamina_perpendicular_axis_theorem()
    test_angular_momentum_collinearity()
    print("All PHYC54 inertia tensor and multilinear algebra tests passed successfully!")
