###    Calculate the Stacking Fault Energy & Width      ###
###            Dislocation Characteristicts             ###


###
Amirmohammad Pourattar
Email: Pourattar96@gmail.com | Pourattar96@ut.ac.ir
###


import math

# Constants
G = 26.18e9
NO = 0.345
CONVERSION_FACTOR = 1e-10  # Convert to appropriate units
DEGREES_PER_RADIAN = 180 / math.pi

def get_vector_input(burgers_vector):
    x = float(input(f"Enter the x-coordinate of b1: "))
    y = float(input(f"Enter the y-coordinate of b2: "))
    return [x, y]

def read_dislocation_length(dislocation_line):
    x = float(input(f"Enter the x-coordinate of dislocation: "))
    return [x, 0]  # y-coordinate is zero

def calculate_angle_and_sine(vector1, vector2):
    dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1]
    magnitude1 = math.sqrt(sum(i**2 for i in vector1))
    magnitude2 = math.sqrt(sum(i**2 for i in vector2))
    cosine_angle = dot_product / (magnitude1 * magnitude2)
    angle_degrees = math.acos(cosine_angle) * DEGREES_PER_RADIAN
    sine_angle = math.sqrt(1 - cosine_angle**2)
    return angle_degrees, sine_angle

def main():
    f_atom = float(input("Enter the x-coordinate of the first atom: "))
    s_atom = float(input("Enter the x-coordinate of the second atom: "))
    
    b_1 = get_vector_input("b1")
    l1 = read_dislocation_length("leading partial dislocation")
    b_2 = get_vector_input("b2")
    l2 = read_dislocation_length("trailing partial dislocation")
    
    angle_b1_l1, sin_b1 = calculate_angle_and_sine(b_1, l1)
    angle_b2_l2, sin_b2 = calculate_angle_and_sine(b_2, l2)
    
    absolute_b_1 = math.sqrt(b_1[0]**2 + b_1[1]**2) * CONVERSION_FACTOR
    absolute_b_2 = math.sqrt(b_2[0]**2 + b_2[1]**2) * CONVERSION_FACTOR
    d = abs(s_atom - f_atom) * CONVERSION_FACTOR
    
    gama = (G * absolute_b_1 * absolute_b_2 * (math.cos(math.radians(angle_b1_l1)) * math.cos(math.radians(angle_b2_l2)) + (sin_b1 * sin_b2) / (2 - NO)) / (2 * math.pi * d)) * 1000
    
    print("gama is equal to:", gama)
    print("d is equal to:", d)
    print("angle between b1 and l1:", angle_b1_l1)
    print("angle between b2 and l2:", angle_b2_l2)

if __name__ == "__main__":
    main()
