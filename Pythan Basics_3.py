# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:43:50 2021

Refer -> Global Module Index in python.org
Plotting - pylab, numpy, Matplotlib
%matplotlib qt : New window
%matplotlib inline : Same window

numpy examples
np.random.randn(1000) # Guassian
np.random.rand(1000)  # Uniform
np.arange(0, 1, 1e-5)
np.linspace(0, 2, 10000)

Triangle of points using itertools
itertools.product(range(0, 10), range(0, 10))
dunder
"""

import numpy as np
import pylab as pl

"""
t = np.arange(0, 10, 0.01)  # set of small interval values
print(t)

x = np.sin(t)
y = np.cos(t)
pl.plot(t, x, 'r-', label='Sine') # line color red
pl.plot(t, y, 'b-', label='Cos') # line color blue
pl.rc('font', size=24)
pl.grid(True)

pl.legend() # label needed in plot()

pl.xlabel('Time (s)')
pl.ylabel('Amplitude')
pl.title('Sin-Cos waves')
pl.axis([0, 10, -1.8, 1.8])  # [-x, x, -y, y]

pl.savefig('p3.pdf')
pl.show() """

print()
print("##############################################")
print()

# Generate 10000 Gaussian numbers with Mean 15, variance 3
mu = 15
sigma = 3
x = mu + sigma * np.random.randn(100000)   
pl.hist(x, 100)
pl.grid()
pl.title(f'Histogram of Gaussian with $\\mu = {mu}, \\sigma = {sigma}$')
pl.show()

# 1. Trapezoidal integration
# Integrate x² from 0 to 2
# Ans: x³ / 3 for 0 to 2
# Evaluates to 8 / 3 = 2.667

# (a) how do we split the region between 0 and 2 into small parts?
# First approach: arange
x1 = np.arange(0, 1, 1e-5)
y = x1**2
print("Trapezoid area1", np.trapz(y, x1))

# Second approach: linspace
x2 = np.linspace(0, 2, 10000)
y = x2**2
print("Trapezoid area2", np.trapz(y, x2))
print()

# Examples of random number generation
# 1. Generate 1000 random Gaussian numbers and display their mean and variance
x = np.random.randn(1000)  # randn() and rand() are different
#print(x)
print("Length of x = ", len(x))
print()

print("Gaussian")
print("Mean:", np.mean(x))
print("Variance:", np.var(x))
print("Stddev:", np.std(x))
print()

# 2. Let's generate uniform numbers between (0, 1)
x = np.random.rand(1000)  # randn() and rand() are different
#print(x)
print("Length of x = ", len(x))
print()

print("Uniform")
print("Mean:", np.mean(x))
print("Variance:", np.var(x))
print("Stddev:", np.std(x))
print()

# How to "manually" find the variance and standard deviation
print("Verifying the var, std")
var = np.mean((x - np.mean(x))**2)
std = np.sqrt(var)
print("Checking variance: %.5f" %var)  # round off without , & 2 %
print("Checking stddev:", std)
print()

print()
print("##############################################")
print()

import itertools
import math as m

"""
Write a function that takes three float arguments: a, b and c, 
and returns a list of two-length tuples which are the coordinates 
included within x ≥ 0, y ≥ 0 and ax + by ≤ c.
"""

def required_points (a, b, c):
    x_intercept = c / a
    y_intercept = c / b

    points_to_check = itertools.product(
            range(0, m.ceil(x_intercept)),
            range(0, m.ceil(y_intercept)))
    #print(list(points_to_check))

    print("Points within range:")
    pts = [i for i in points_to_check if a * i[0] + b * i[1] <= c]
    return pts

print(required_points(1, 1, 3.3))
print(required_points(1, 1, 2.3))

print()
print("##############################################")
print()

"""
Write a function that takes three float arguments: a, b and c, 
and returns a list of two-length tuples which are the coordinates 
included within x ≥ 0, y ≥ 0 and ax + by ≤ c.
"""

def required_points2 (a, b, c):
    x_intercept2 = c/a
    y_intercept2 = c/b
    points_to_check2 = [(i, j) for i in range(0, m.ceil(x_intercept2)) 
                        for j in range(0, m.ceil(y_intercept2))
                        if a*i + b*j <= c]
    return points_to_check2
        
print(required_points2(1, 1, 3.3))
print(required_points2(1, 1, 2.3))  

print()
print("##############################################")
print()

def is_palindrome(x):
    return x.lower() == x.lower()[::-1]

if __name__ == "__main__":  # Code in this block will be called when run this file
    print("This is my program!")
    x = "madam"
    if is_palindrome(x):
        print(f"{x} is a palindrome!")

