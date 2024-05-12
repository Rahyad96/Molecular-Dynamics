###    Calculate the angle between two vector    ###
###   Dislocation Vector and its Burgers Vector  ###


###
Amirmohammad Pourattar
Email: Pourattar96@gmail.com | Pourattar96@ut.ac.ir
###

import math

# Constants
DEGREES_PER_RADIAN = 180 / math.pi

def read_vector(prompt):
    return [float(input(prompt.format(i))) for i in range(2)]

def calculate_angle_between_vectors(vector1, vector2):
    dot_product = sum(a * b for a, b in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(x**2 for x in vector1))
    magnitude2 = math.sqrt(sum(y**2 for y in vector2))
    cosine_angle = dot_product / (magnitude1 * magnitude2)
    angle_radians = math.acos(cosine_angle)
    return angle_radians * DEGREES_PER_RADIAN

def main():
    q = 0
    while q < 100:
        vector1 = read_vector("Enter i and j of the first vector: ")
        vector2 = read_vector("Enter i and j of the second vector: ")
        
        angle_degrees = calculate_angle_between_vectors(vector1, vector2)
        print("Theta is equal to: ", angle_degrees)
        
        q += 1