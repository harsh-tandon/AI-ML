# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:56:37 2021

ctrl + l = clear output screen
akumar@ee.iitb.ac.in

itertools.product, itertools.permutations(str)
collections.Counter, most_common(int), 

''.join(x) joins x without space

num = random.randrange(1, 100, 1)
# num = random.randint(1, 100)  # Alternative way

"""

l1 = ['cat', 'lion', 'elephant']
print([len(l) for l in l1])

for l in l1[:]:
    print("Length is", len(l))
    print("Reverse:", l[::-1])
print(l1[::-1]) 
l1.sort()
print(l1)  # print(l1.sort()) won't work, as l1.sort() returns void
l1.reverse()
print(l1)  # print(l1.reverse()) won't work, as l1.reverse() returns void

print("################ 1 #####################")
print()

l2 = list(range(5))
print(l2)
l3 = l2[1:6]
print(l3)
l3 = l2[1:-2]
print(l3)

print("################# 2 ####################")
print()

a, b = 0, 1
print(a, b, end=' ')
while a <10:    
    a, b = b, a + b       
    print(b, end=' ')

print()
print("############### 3 ######################")
print()

a, b, n = 0, 1, 0
print(a, b, end=' ')
while n <10:        
    a, b = b, a + b
    print(b, end=' ')    
    n = n+1

print()
print("############### 4 ######################")
print()

print(list(range(2,10))[::-1])  # reverse the list
l4 = list(range(10, 2, -1))
l5 = list(range(10, 2, -1))
l6 = []
print(l4+l5)

for i in l4:
    l6.append(i+10)
print(l6)

print(r"Hello \n world!!")
print("Hello \n world!!")

print()
print("@@@@@@@@@@@@@@@ 5 @@@@@@@@@@@@@@@@@@@@@@")
print()

import random

"""
num = random.randrange(1, 100, 1)
# num = random.randint(1, 100)  # Alternative way
guess = -1

while(num != guess):
    try:
        guess = int(input("Enter something: "))
    except ValueError as e:
        print(e)
        print("Enter proper number")
        continue
    if guess > num:
        print("Your guess is high")
    elif guess < num:
        print("Your guess is Low")
    else:
        print("Right Guess")

print()
print("############## 6 #######################")
print()  """

print(type(range(1, 100)))
x = list(range(1, 100))
#print(x)
print(type(x))
print(type(random.randrange(1, 100, 1)))
print(list(range(random.randrange(1, 100, 1))))

import math
print("%.4f" %math.pi)
print("%.2f" %math.cos(30))

print()
print("############## 7 #######################")
print()

print([n**3 for n in range(1,5) if n != 3])

# Find (a3 + b3) for a, b in (1,20)
l7 = [i**3 + j**3 for i in range(1,20) for j in range(1,20) if i<=j]
l7.sort() # sorts collection and returns void
print(l7) 
print()

l8 = [str(i) for i in l7]
print(l8)
print()
print([i+ ":"+ str(l8.count(i)) for i in l8 if l8.count(i) >1])


# Find (a3 + b3) for a, b in (1,20) - Using collections

import collections
cubes = [i**3 + j**3 for i in range(1,21) for j in range(1,21) if i<= j]
print("Cubes: ", cubes)
cubes_freq = collections.Counter(cubes)
print()
print(cubes_freq.most_common(5)) # top 5 most common

print()
print("############## 8 #######################")
print()

import itertools
it1 = list(itertools.product(range(1,21), range(1,21))) # product for num pair
#print(it1) # has duplicate pairs
#print()

it2 = [i for i in it1 if i[0] <= i[1]]
print(it2)
print()

y = [2, 3, 5, 6, 22, 3]
y.sort()
print(y)
s = list(str(y)) #Splits the string into chars
print(s)
print(s.count('2'))

print()
print("############## 9 #######################")
print()

# Find the number of permutations of word "UNISIT" 
# where two I's don't appear next to each other

l9 = list(itertools.permutations('UNISIT'))
print(l9)
print(len(l9)) # not count
print()

not_together = [i for i in l9 if 'II' not in ''.join(i)]  # ''.join(x) joins x without space
print(not_together)
print(len(not_together)) # len(), not count()





   
    
    



