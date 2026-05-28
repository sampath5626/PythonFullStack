'''
List comprehensio
------------------
--> List comprehension offers a shortest syntax when we want to create a new list from existing list

syntax : --> varible_name = [expression loop condition]

old = [1,2,3,4,5,5,6,7,8]
new = [so if so%2!=0 else "even"for so in old]
print(new)

Generators
-----------
-->Generators in python are a special type of itterable, allowing users to iterate over data efficiently
withoout storing everything in memory...
-->They generate values lazily using yield keyword

Why to use generators
---------------------
-->Generators do not store the entiredata set in the memory, they generate values on the fly or runtime
-->To avoiding unessary storage of data speed up execution.

How it works
-------------
--> It looks like normal function but uses the yeild keyword instead of return
--> when the function is called, it does not execute immediately. insted it return a
generator object which can be iterated using loop or the next() function

def simple():
    print("start")
    yield 1
    yield 2
    yield 3
    print("end")

gen = simple()
print(next(gen))
print(next(gen))
print(next(gen))

'''
def any(num):
    for i in range(1,num+1):
        yield i*i
a = any(5)
print(next(a))
print(next(a))
print(next(a))

def sqr(num):
    result = []
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(5))
'''
def fabi(num):
    a = 0
    b = 0
    num = int(input())
    for i in range(num)
    num = (a+b)
    
    print(a,b,num)

'''
so= 'cahran is good boi'
nan = ""
count = 0
for j in so:
    if j not in "AEIOUaeiou":
        nan += j
        count += 1
print(count)
print(nan)




























