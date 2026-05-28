'''
assert
------
--> This is debugging statement used to test whether the condition is true


FUNCTIONS
---------
-->A function is a block of code which only exicute when it is called
-->We can pass data known as parameters into a function
-->To aviod repeated lines in code

def function_name(parameters):
    ------------
    ------------
functionaa_name(arguments)

Example
--------
num = 8
def even(num):
    if num%2==0:
       print(f"{num} even")
    else:
        print(f"{num} odd")
even(num)
even(5434)

Ways to pass argumrnts:
-----------------------
1.Required arguments
--------------------


def even(num,num2):
    if num%2==0:
       print(f"{num} even")
    else:
        print(f"{num} odd")
even(100,63)

def even(num,num2,num3):
    if num%2==0:
       print(f"{num} even")
    else:
        print(f"{num} odd")
even(100,63)

2.Default arguments
--------------------
def even(name= "sam",age=45):
    print(name)
    print(age)
even("bunty")
even("chanti")
even("chanti",78)

3.Keyword arguments
------------------------
-->We can set arguments with key = value syntax. By this, the order of
arguments does not matter.

4.Variable lenght arguments
---------------------------
-->Adding a star(*) before the parameter name in the function ,recive a
tuple of argumnets and can acess item with their indexs

def even(*name):
    print(name)
even("chanti","bunty","sonti")

5.



count = 0
for i in range (2,100):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count +=1
    if count ==2:
        print(f"{i}",end =",")'''
       
for i in range (2,100):
    for j in range (2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")


























