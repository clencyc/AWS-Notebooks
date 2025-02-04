import math

def cylinder_volume(height, radius):
    pi = math.pi
    print(height * pi * radius ** 2)

cylinder_volume(10, 3)
cylinder_volume(height=10, radius=3)