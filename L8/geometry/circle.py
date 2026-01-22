import math

def area(radius):
    if radius <= 0:
        raise ValueError("Raza trebuie sa fie pozitiva.")
    return math.pi * radius ** 2

def circumference(radius):
    if radius <= 0:
        raise ValueError("Raza trebuie sa fie pozitiva.")
    return 2 * math.pi * radius
