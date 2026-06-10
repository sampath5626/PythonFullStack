'''
INHERITENC
----------
--> This allows one class to aquire the properties and methods of another
class...

Type
----
1.Single Inheritence
---------------------
--> A class inhert frorm the single parent

class Father:
    def Land(self):
        print("My father have 5 accer")
class sam(Father):
    def my_land(self):
        print("I have 2 accer")

nan = sam()
nan.Land()


2.Multiple Inheritence
------------------------
-->A class inherits more than one parent class

class Father:
    def Land(self):
        print("My father have 5 accer")
class mother:
    def gold(self):
        print("My mother have 1kg of gold")
class sam(Father,mother):
    def my_land(self):
        print("I have nothing")

nan = sam()
nan.Land()
nan.gold()

3.Multi-level Inheritence
--------------------------
--> A class Inherts from sa  parent class and another class inherts
from that child class

class grandfather:
    def land(self):
        print("My grandfather have 5 accer of land")
class Father(grandfather):
    def flat(self):
        print("My father have flat at vizag")
class son(Father):
    def Ntg(self):
        print("I own both of their properties")
al = son()
al.land()
al.flat()
=============================================================================
class car:
    def engine(self):
        print("4 sroke petrol engine")

class typee:
    def model(self):
        print("mercidecs 400ec")
class benz(car,typee):
    def clour(self):
        print("matee black")

carr = benz()
carr.engine()
carr.model()
=============================================================================
4.Hierarchical Inheritence
---------------------------
-->Multiple child classes inherts from a single parent..

class father:
    def Land(self):
        print("10 accer of land")

class sam(father):
    def mine(self):
        print("JOB")
class jas(father):
    def bro(self):
        print("JOBLESS")

man1 = jas()
man1.Land()

man2 = sam()
man2.Land()

5.Hybrid Inheritance
----------------------
-->This is the combination of two or more types of inheritance
                                                     
class A:
    def some(self):
        print('Class A')
class B(A):
    def any(self):
        print('Class B')
class C(A):
    def so(self):
        print('Class C')
class D(B,C):
    def all(self):
        print('Class d')
jam = D()
jam.some()                                                      

**super() method
----------------
-->super() is used to acess methods and constructor of the parent class from
the child class

class parent:
    def display(self):
        print("Parent Method")
        
class child(parent):
    def display(self):
        super().display()
        print('Method Child')
        
ant = child()
ant.display()

'''
class Person:
    def __init__(self,name):
        self.name = name
class stu(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll

    def show(self):
        print(f"Name :{self.name}")
        print(f"Roll :{self.roll}")
v = stu('sam',10)
v.show()





































