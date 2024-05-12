#Molecular Dynamics Simulations (Refined Version) with python 3
#A.M.Pourattar | Pourattar96@gmail.com 

import numpy as np
import math
import random

# Constants
L = 40
A = 3.6147
R = 5
KB = 0.001987191
T = 300
M = 63.546
ALPHA = 1.4199
D0 = 0.4205
R0 = 2.78
DT = 0.01  # Time step

# Initialize atom coordinates
def initialize_positions(l, a, r):
    positions = []
    lattice_points = np.array([[0, 0, 0], [0.5, 0.5, 0], [0.5, 0, 0.5], [0, 0.5, 0.5]])
    for i in range(-l, l + 1):
        for j in range(-l, l + 1):
            for k in range(-l, l + 1):
                for point in lattice_points:
                    pos = a * (point + np.array([i, j, k]))
                    if np.linalg.norm(pos) <= r:
                        positions.append(pos)
    return np.array(positions)

# Calculate forces
def calculate_forces(positions, alpha, d0, r0):
    n = len(positions)
    forces = np.zeros_like(positions)
    for i in range(n):
        for j in range(i + 1, n):
            r_ij = positions[j] - positions[i]
            dist = np.linalg.norm(r_ij)
            if dist > 0:
                force_magnitude = d0 * alpha * (2 * np.exp(-2 * alpha * (dist - r0)) - np.exp(-alpha * (dist - r0)))
                forces[i] += force_magnitude * r_ij / dist
                forces[j] -= force_magnitude * r_ij / dist
    return forces

# Verlet integration for position and velocity
def verlet_integration(positions, velocities, forces, dt, m):
    new_positions = positions + velocities * dt + 0.5 * forces / m * dt**2
    new_velocities = velocities + 0.5 * forces / m * dt
    return new_positions, new_velocities

# Calculate velocities
def initialize_velocities(size):
    velocities = np.random.normal(0, np.sqrt(KB * T / M), (size, 3))
    return velocities - np.mean(velocities, axis=0)

def main():
    positions = initialize_positions(L, A, R)
    velocities = initialize_velocities(len(positions))
    forces = calculate_forces(positions, ALPHA, D0, R0)
    for step in range(100):  # Simulation steps
        positions, velocities = verlet_integration(positions, velocities, forces, DT, M)
        if step % 10 == 0:
            print(f"Step {step}: Positions:\n{positions}\n")
