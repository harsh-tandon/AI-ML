# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:48:39 2021

ctrl + c => to exit from help console

Tuples  (1. Immutable/ Fixed lists, 2. Slicing possible 3. Can't be appended, 4. Faster)
Tuple - (), List - [], Dictionaries - {}
Slicing
Dictionaries can't be sorted. Dictionaries use Hash table
Dictionaries - dict1.items(), dict1.keys(), dict1.values()
List can't be keys. But, tuple can be keys, as these are immutable.

Collections: collections.Counter('abcdeabc'), sorted(coll), sum(coll)
set(l); CSV files
lines = [i.strip() for i in lines]
Refer - Python pip - pypi.org -> details of all modules

"""

# Number of 9's between 1 and x
def no_of_9s(x):
    return str(x).count('9')

print(r"Sum of 9's =", sum([no_of_9s(i) for i in range(1, 101)]))

l1 = [2, 5, 2, 1]
print(sum(l1))

l2 = ['a', 'b', 'c']
print(l2)
print(''.join(l2))
print("Hello " + ",".join(l2))

print()
print("################# 1 ####################")
print()

l = []
l.append('a')
l.append('c')
l.append('d')
print(l)
l.pop(-1)
print(l)
l.insert(1, 'e') # ?l.insert
print(l)
print()

print()
print("################# 2 ####################")
print()

l3 = (1, 2.3, 'ab', 3, 5, 2.2)
print(l3)
# l3[2] = 'bc' #Can't be inserted/ updated
print(l3[2])
print(l3[::-1])  #Reverse
print(l3[1::2])  #Start: End: Incrementor

tuple_prime_nos_unsorted = (3, 5, 1, 7)
tuple_prime_nos = sorted(tuple_prime_nos_unsorted)

t_prime_plus_2 = tuple(i+2 for i in tuple_prime_nos)
print(t_prime_plus_2)

print()
print("################ 3 #####################")
print()

# Each tuple has name, Maths marks, Physics marks
s1 = ("John", 30, 40)
s2 = ("Heena", 10, 20)
s3 = ("Ram", 15, 50)
students = [s1, s2, s3]
print(students)

def get_maths_marks(s):
    return s[1]

def get_physics_marks(s):
    return s[2]

students.sort(key=get_maths_marks, reverse=True)
print(students)

# Get highest maths marks
print(get_maths_marks(students[0]))

# Get student with lowest maths marks
print(students[-1][0])

print()
print("@@@@@@@@@@@@@@@@@ DICTIONARIES @@@@@@@@@@@@@@@@@")
print()

dict1 = {1: 'All', 2: 'is', 3: 'well'}
print(dict1)
dict1[4] = 'earlier'
print(dict1)
print(type(dict1[1]))

dict1[2] = 'was' # mutable/ changable
print(dict1)

for k,v in dict1.items():
    print(k, v)

for k in dict1.keys():
    print(k)

for v in dict1.values():
    print(v)

print()
import collections

c = collections.Counter('abcdeabcdabcaba') # c has chars as key and occurances as values in str
print(c)
print(c.most_common(3)) # three most common elements
print()

print(sorted(c))        # list all unique elements
print(''.join(sorted(c.elements())))   # list elements with repetitions
print(sum(c.values()))  # total of all counts
print(c['a'])         # count of letter 'a'

print()
print("################ 4 #####################")
print()

# Find number of occurances of each letter - Sentence with all letters
s = "the quick brown for jumps over the lazy dog"
print(list(s))

occurances = {} # Dictionary
c = collections.Counter(s)
print()
print(c)
print()

# Find number of occurances of each word
words = "cat at bat fat mat RAT cat at bat rat"
word_freq = {}
for word in words.split():
    word = word.lower()
    if word in word_freq.keys():
        word_freq[word] = word_freq[word] + 1
    else:
        word_freq[word] = 1        
print(word_freq)
print()

# Using collections
words = "cat at bat fat mat RAT cat at bat rat"
print(collections.Counter(words.lower().split()))
print()

l = [1, 2, 3, 3, 4, 5, 10, 9, 4, 2, 4]
print(set(l))  # unique values in list, returns set {}
print([set(l)])  # whole set in list [{ }]
print(list(set(l)))  # pure list []

print()
print("@@@@@@@@@@@@@@@@@ CSV FILES @@@@@@@@@@@@@@@@@")
print()

f = open("marks.csv", "r")
lines = f.readlines()
print("f lines:", lines)
lines = [i.strip() for i in lines]
print("f lines:", lines)
print('Split:', [i.split(',') for i in lines])


