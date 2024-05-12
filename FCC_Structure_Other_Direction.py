#Create fcc lattice structure (other direction) with python 3
#A.M.Pourattar | Pourattar96@ut.ac.ir | University of Tehran | April 2022

import numpy as np

# Constants
a = 4.0478  # Lattice constant
lx, ly, lz = 6, 6, 6  # Dimensions in terms of lattice constant
primitive_positions = np.array([[0, 0, 0], [0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]])

# Directions for each vector
l1 = np.array([1, 1, -2])
l2 = np.array([1, -1, 0])
l3 = np.array([-1, -1, -1])

# Lengths of vectors (magnitude)
r1 = np.sqrt(6)
r2 = np.sqrt(2)
r3 = np.sqrt(3)

def adjust_positions():
    for i in range(len(primitive_positions)):
        s1 = np.sqrt(1 + 1 + 4)
        s2 = np.sqrt(1 + 1 + 0)
        s3 = np.sqrt(1 + 1 + 1)
        primitive_positions[i] *= [a / s1, a / s2, a / s3]
    return primitive_positions

def generate_lattice():
    positions = []
    adjusted_positions = adjust_positions()
    for i in range(-lx // 2, lx // 2 + 1):
        for j in range(-ly // 2, ly // 2 + 1):
            for k in range(-lz // 2, lz // 2 + 1):
                for pos in adjusted_positions:
                    x = pos[0] + a * (l1[0] / r1) * i + a * (l2[0] / r2) * j + a * (l3[0] / r3) * k
                    y = pos[1] + a * (l1[1] / r1) * i + a * (l2[1] / r2) * j + a * (l3[1] / r3) * k
                    z = pos[2] + a * (l1[2] / r1) * i + a * (l2[2] / r2) * j + a * (l3[2] / r3) * k
                    positions.append([x, y, z])
    return positions

def write_to_file(positions):
    with open("datafile.xyz", "w") as f:
        f.write(f"{len(positions)}\n\n")
        for pos in positions:
            f.write(f"Al\t{pos[0]}\t{pos[1]}\t{pos[2]}\n")

def main():
    positions = generate_lattice()
    print('* Lattice constant: {:.4f} \n* Number of atoms: {}'.format(a, len(positions)))
    write_to_file(positions)

if __name__ == "__main__":
    main()
