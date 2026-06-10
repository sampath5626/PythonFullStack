'''
MODULES
--------
-->A module in python is a file that  contains python code such as
-variables
-functions
-classes
-statement

Two ypes of modules
--------------------
user-define
built-in

import math
print(math.sqrt(49))
print(int(math.pow(3,5)))

from math import sqrt
print(sqrt(78))

import math as m
print(m.pow(67,2))


import os
os.remove("functions.py")
os.mkdir("charan.py")
os.rmdir("charan.py")

import sys
print(sys.version)
print(sys.path)

import random
print(random.randint(1000,9999))


import collections
data = ['a','b','c','d']
print(collections.Counter(data))

from collections import Counter, defaultdict
data = ['a','b','c','d']
counter = Counter(data)
print(counter)

import collections
dd = collections.defaultdict(int)
dd['missing'] += 1
print(dd['missing'])
print(dd)
'''
