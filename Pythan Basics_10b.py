# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 00:07:58 2021

Object Oriented Programming 
class, self (=this keyword), __init__(), __repr__()
Vector (x, y, z)
rint = random.randint

"""

# Widget
# |      \         / Push button
# |       \       /
# |        Button ---- Radio button
# Scrollbar      \ 
#                 \
#                  Checkbox

class Student:
    def __init__(self, name, physics, maths, chemistry):   # Special function - Constructor
        self.name = name
        self.physics = physics
        self.maths = maths
        self.chemistry = chemistry
    
    def get_total(self):  # Normal fucntion, user defined
        return self.maths + self.physics + self.chemistry
    
    def get_average(self):  # Normal fucntion, user defined
        return self.get_total() / 3
    
    def __repr__(self):  # Special function
        return f"{self.name}: ({self.maths}, {self.physics}, {self.chemistry})"
    
f = open('scores.csv', 'r')
student_list = []
for line in f.readlines()[1:]:
    elements = line.strip().split(',')
    name = elements[0]
    m = int(elements[1])
    p = int(elements[2])
    c = int(elements[3])
    student_list.append(Student(name, m, p, c))
f.close()

print("STUDENT TOTALS:")
for s in student_list:
    print(s.name, s.get_total())

# Sort students by their scores
students_sorted = sorted(student_list, key=lambda x : x.get_total())
print(students_sorted)

print()
print('###################### Example 2 #################################')
print()

import math
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def mag(self):  # Magnitude
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    
    def __add__(self, v):  # Method overloading
        return Vector(self.x + v.x, self.y + v.y, self.z + v.z)
    
    def __sub__(self, v):  # Method overloading
        return self.__add__(Vector(-v.x, -v.y, -v.z))
    
    def __pow__(self, n):  # Method overloading
        return Vector(self.x**n, self.y**n, self.z**n)

v1 = Vector(1, 2, 3)
v2 = Vector(1, -2, 4)
print(v1 + v2)

# Let's create a random list of vectors
import random
rint = random.randint  # Important shortcut
random_vectors = []
for i in range(10):
    random_vectors.append( Vector(rint(-5, 5), rint(-5, 5), rint(-5, 5)) )

# 1. Magnitude of all vectors:
mags = list(map(lambda x : x.mag(), random_vectors))
print(mags)

# 2. Z-coordinate of each vector
z_coords = list(map(lambda x : x.z, random_vectors))
print(z_coords)

# 3. Square the coordinates of each vector
v_squared = [v**2 for v in random_vectors]
print(v_squared)
