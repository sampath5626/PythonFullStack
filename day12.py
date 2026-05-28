'''
BUILT IN FUNCTIONS
------------------
print()
input()
len()
type()
max()
min()

Recuesive Function
-------------------
A recursive function that calls itself to solve a problem by breaking it
into small or simple sub-problems

def fac(num):
    if num==1:
        return 1
    return num*fac(num-1)
print(fac(5))

return()
---------
this ends a function execution and sends a value back to the code that called
the function

def add(a,b):
    return a+b
res = add(4,5)
print(res)

lambda function()
-----------------
-->A lambda function is small annonamus function
-->a lambda can take "n" no of arguments, but only one expression

suntax-lambda arguments : expression

b = lambda a,b: b/a
print(b(2,6))
'''


