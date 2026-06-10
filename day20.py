'''
Polymorphism
------------
This means 'many forms'.. it allows the same function, method , or operator
to behave differently dependding on the object

1.Method overloading
--------------------
-->Method overloading means defining multiple methods in the samr name but different
parameter

eg-1:
-----
class calcu_:
    def add(self, a, b, c=0):
        return a + b + c

an = calcu_()
print(an.add(23,6))
print(an.add(23, 6, 34))

eg-2:
-----
class calcu_:
    def add(self, a, b):
        return a + b + c
    def add(self, a, b, c=0):
        return a + b + c

an = calcu_()
print(an.add(23,6))
print(an.add(23, 6, 34))

eg-3:
-----
class calcu_:
    def add(self, *num):
        return sum(num)
    
an = calcu_()
print(an.add(23,6))

2.Method overriding
-------------------
-->This occur in a child class provides its own implementation of a method
already defined in a parent class..

class Animal:
    def sound(self):
        print("Animal makes a sound")
class dog(Animal):
    def sound(self):
        print("Dog barks")

god = dog()
god.sound()

3.Operator overloading
----------------------
-->This allows operaters such as +,-,* etc.. to perform different actions for
user-defined objects

class stu:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks + other.marks
so = stu(4)
so1 = stu(56)
print(so+so1)

note:-
----
-->The operator inside the methos will overload a special or operater
given in the call


Abstraction
-----------
-->this is the process of hiding internal implementation details and
showing only essential features to the user
-->It focuses on what an object does rather that how it does it...


'''
from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass

class Rec(shape):
    def _init_(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return 2*(self.a * self.b)

an = Rec(10, 5)
print(an.area())












