'''
SETS
-----
--> aA set a collection of unique and unordered elaments
--> dupilicate values are not allowed
--> Items are not stored in index order
--> represented in "{}"

METHODS
--------
union()
-------
-->it will give all values from 2 sets together in once
--> syntax: variable_name.union(another var)

intersection()
--------------
--> to get the commom elements from both sets 
--> syntax: variable_name.intersection(another var)

difference()
-------------
--> to get the different values from the set
syntax: variable_name.difference(another var)

symentric difference()
----------------------

add()
-----
-->to add new elements into set
syntax : variable_name.add(elemet)

update()
--------
--> to add multiple items into set
syntax:variable_name.update([elements])

*len()

*max()

*min()

*remove()
----------
(used to remove elment from the set but it
throw error if element is not found in the set)

*discard()
used to remove the element from the set but never
throw the error if element not find in the set

'''

a = {1,2,13,4,6,6,8,10,11}
b = {7,8,9,0,84,56}
print(a - b)
print(b.difference(a))
print(a.symmetric_difference(b))
print(a ^ b)
a.update([35,23])
a.remove(2)
print(a)
print(sum(a))





















