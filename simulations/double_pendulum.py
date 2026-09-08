"""
PHYC54: Double Pendulum Chaotic Dynamics & Phase Space Simulation
Solves the exact coupled nonlinear Euler-Lagrange equations of motion using scipy.integrate.solve_ivp.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Physical parameters
L1, L2 = 1.0, 1.0  # arm lengths (m)
m1, m2 = 1.0, 1.0  # bob masses (kg)
g = 9.81           # acceleration of gravity (m/s^2)

def equations_of_motion(t, y):
    """
    y = [theta1, omega1, theta2, omega2]
    Returns dy/dt = [omega1, alpha1, omega2, alpha2]
    """
    th1, w1, th2, w2 = y
    delta = th1 - th2

    # Denominators from mass matrix inversion
    den1 = L1 * (2*m1 + m2 - m2 * np.cos(2*th1 - 2*th2))
    den2 = L2 * (2*m1 + m2 - m2 * np.cos(2*th1 - 2*th2))

    # Angular acceleration 1
    num1 = (-g * (2*m1 + m2) * np.sin(th1) 
            - m2 * g * np.sin(th1 - 2*th2) 
            - 2 * np.sin(delta) * m2 * (w2**2 * L2 + w1**2 * L1 * np.cos(delta)))
    alpha1 = num1 / den1

    # Angular acceleration 2
    num2 = (2 * np.sin(delta) * (w1**2 * L1 * (m1 + m2) 
            + g * (m1 + m2) * np.cos(th1) 
            + w2**2 * L2 * m2 * np.cos(delta)))
    alpha2 = num2 / den2

    return [w1, alpha1, w2, alpha2]

def run_simulation(th1_0=np.pi/2, th2_0=np.pi/2, t_max=20.0):
    t_eval = np.linspace(0, t_max, 2000)
    sol = solve_ivp(equations_of_motion, [0, t_max], [th1_0, 0.0, th2_0, 0.0], 
                    t_eval=t_eval, method='Radau', rtol=1e-8, atol=1e-8)
    
    # Forward kinematics for bob positions
    th1 = sol.y[0]
    th2 = sol.y[2]
    x1 = L1 * np.sin(th1)
    y1 = -L1 * np.cos(th1)
    x2 = x1 + L2 * np.sin(th2)
    y2 = y1 - L2 * np.cos(th2)

    return sol.t, x1, y1, x2, y2

if __name__ == '__main__':
    t, x1, y1, x2, y2 = run_simulation()
    plt.figure(figsize=(8, 8))
    plt.plot(x2, y2, color='#e74c3c', lw=1, alpha=0.8, label='Bob 2 Chaotic Trajectory')
    plt.plot(x1, y1, color='#3498db', lw=0.8, alpha=0.5, label='Bob 1 Trajectory')
    plt.scatter([0], [0], color='black', s=50, zorder=5, label='Pivot')
    plt.title('PHYC54: Double Pendulum Chaotic Trajectory', fontsize=12, fontweight='bold')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.grid(True, linestyle=':', alpha=0.5)
    plt.legend()
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig('double_pendulum_trajectory.png', dpi=200)
    print("Simulation completed. Saved double_pendulum_trajectory.png")
