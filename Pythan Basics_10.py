# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 23:09:14 2021

Lambda expression/ functions (short-hand)
Lambda Map() - map(lambda i: condition i, coll) or map(func, coll)
Lamdbda Filter() - filter(lambda i: condition i, coll)
Generator examples - yield x (returns value without memory allocation)

"""

def double_orig(x):
    return 2 * x

# Alternate:
double = lambda x : 2 * x # Shorter

# Capitalize first letter of
# the string

cap_first_letter = lambda x : x[0].upper() + x[1:]
print(cap_first_letter("hello"))

# Sort people by their last name
names = ["Elon Musk",
         "Peter Thiel",
         "Marc Andreessen",
         "Sergei Brin",
         "Eric Schmidt",
         "Bjarne Stroustrup"
         ]

def get_last_name(n):
    return n.split(' ')[1]

# We'll split based on space, then take second element for sorting
names_sorted = sorted(names, key=lambda n : n.split(' ')[1]
#                      key=get_last_name
                     )
print('Sorted last names:', names_sorted)

# Multi variable lambdas

is_sum_odd = lambda a, b: (a + b) % 2 ==1
print(is_sum_odd(10, 20))
print(is_sum_odd(1, 10))

print()
print('####################### 1 #############################################')
print()

# Find all pairs of +ve integers (a, b) such that
# 1 ≤ a ≤ b ≤ 1000000000
# where a² + b² is divisible by 9

# Q1. How would we generate all pairs?

import itertools

N = 10  # 1000000: Can give bigger number also

def myrange(a, b):
    i = a
    while i < b:
        yield i   # returns i without memory allocation
        i = i + 1

pairs_to_check = itertools.product(myrange(1, N), myrange(1, N))

# Enforce a ≤ b
pairs_to_check_2 = (i for i in pairs_to_check if i[0] <= i[1])

final_pairs = (i for i in pairs_to_check_2
               if ((i[0]**2 + i[1]**2) % 9 == 0) )

for i in final_pairs:
    print(i)  # exhausting values now

print()
print('####################### MAP/ FILTER #################################')
print()

# Find all pairs of +ve integers (a, b) such that
# 1 ≤ a ≤ b ≤ 1000
# where a² + b² is divisible by 9

import itertools
N = 10  # 1000000: Can give bigger number also

def myrange(a, b):
    i = a
    while i < b:
        yield i
        i = i + 1

pairs_to_check = itertools.product( myrange(1, N), myrange(1, N) )

pairs_to_check_2 = filter(lambda i: i[0] <= i[1], pairs_to_check)
final_pairs = filter(lambda i: (i[0]**2 + i[1]**2) % 9 ==0, pairs_to_check_2)

for i in final_pairs:
    print(i)

print()
print('##################### MAP/ FILTER 2 ################################')
print()

# MAP
x = [1, 2, 5, 9, 15]

# Square each element
x_squared = map(lambda i : i*i, x)
for i in x_squared:
    print(i)

animals = ["Dog", "Cat", "Monkey", "Bear"]
print(list(map(len, animals)))

# FILTER : Keep only elements that satisfy a condition

x_even = filter(lambda x : x% 2 == 0, x)
print(list(x_even))

x_odd = filter(lambda x : x% 2 == 1, x)
print(list(x_odd))

# Animals whose string length > 3
print(list( filter(lambda i : len(i) > 3, animals) ))

print()
print('###################### MAP 2 ######################################')
print()

f = open('test.csv', 'r')
lines = f.readlines()  #[1:] to skip 1st row
f.close()
emails = map(lambda i : i.split(',')[0].strip(), lines)
domain_names = map(lambda i: i.split('@')[1], emails)

# Unique domain names:
print(set(domain_names))

# OLD CODE:
f = open('test.csv', 'r')
for line in f:
    print(line.split(',')[0].split('@')[-1])
f.close()

print()
print('####################### 2 ###########################################')
print()

# Convert all MBs into KBs

x = ["10M", "20K", "3M"]

mb_to_kb = lambda x : x[-1] == "M" and str(int(x[:-1]) * 1024) + "K" or x  # Short circuit technique
remove_k = lambda x : int(x[:-1])
print(list(map(remove_k, map(mb_to_kb, x))))

print()
print('###################### GENERATOR #################################')
print()

x = [1, 10, 3, 7, 9, 4]
# May be more efficient to do this:
x_squared = (i * i for i in x)
# Rather than x_squared = [i * i for i in x]
# because the [] operation performs the squaring and stores in memory!

#for i in x_squared:
#    print(i)
    
# Primer on iterable "objects"
x_squared = (i * i for i in x)
# First element
print(x_squared.__next__())
# Second element
print(x_squared.__next__())
# 3rd element
print(x_squared.__next__())
# 4th element
print(x_squared.__next__())
# 5th element
print(x_squared.__next__())
# 6th element
print(x_squared.__next__())
# Finally
# print(x_squared.__next__())  # Error

# Another example
g = (i + 7 for i in x)

for i in g:
    print(i)
print("Running again!")
for i in g:
    print(i) # WON'T PRINT, AS IT'S EXHAUSTED/ CONSUMED IN ONE RUN
print("Ran again!")

print()
print('###################### GENERATOR 2 #################################')
print()

# Make your own generator
# Let us sum the series: 1 + 1/2² + 1/3² + 1/4² + … up to n terms
# WITHOUT allocating a large list, it should sum to pi² / 6

def series_element_gen(N):
    i = 1
    while i <= N:
        yield 1 / i / i
        i = i + 1

# Let's sum the above series up to 100000000 terms
print(sum(series_element_gen(100000000)))  # Takes time to print, but doesn't crash


