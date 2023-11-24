import math

def rec_area(width, length):
    return width * length

def cir_area(radius):
    return math.pi * radius**2

def prism_vol(width, length, heigth):
    return width * length * heigth

def sphere_vol(radius):
    return (4/3) * math.pi * radius**3