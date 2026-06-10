'''
OOPs--> Object Oriented Programing system
====
1.class
--------
A class is a blueprint or a templet used to create object
Example:
class parent :
    name = "Charan"

2.object
---------
-->An object is an instance of a class



Example:
class stu:
    def edu(self):
        print("Iam studing B-tech")
    def sports(self):
        print("cricket")
        print("volley ball")
    
s1 = stu()
s1.sports()

Attributes
----------
--> Attributes are the variables that belong to a class or an object
Example:
class stu:
    name = 'Charaaaaaaaaaaaaan'
    age = 32
s1 = stu()
print(s1.name)
print(s1.age)

methods
-------
-->The funtions defined inside the class is methods
class PFs_DA:
    def pyhton(self):
        PFs_DA = "Batch-03"
        print("This PFS and DA batch03")
    def flask(self):
        PFs = "Batch-03"
        print("flask is only for PFs")
al = PFs_DA()
al.pyhton()
al.flask()

Constructor  (__init__)
------------------------
-->A contructor is a special method that is automaically called when an
object is created

class ATM:
    def __init__(self,balance,name):
        self.balance = balance
        self.name = name


    def Bal_check(self):
        print(f"{self.name} total balance is {self.balance}")

    def nam(self):
        print(self.name)
ca= ATM(balance = 100000, name = "Charan Sai" )
ca.Bal_check()
ca.nam()

Access Specifiers
-----------------
1.Public
---------
--> This can be accessed from anywhere in the program
Example:
class stu:
    name = "sam"
a1 = stu()
print(a1.name)

2.Protected
------------
-->This is represented using a single underscor(_)
Example:
class stu:
    _name = "sam"
a1 = stu()
print(a1._name)

3.Private
----------
-->This is represented using a double underscore(__) 
class stu:
    __name = "sam"

s1=stu()
print(s1._stu__name)

Encapsulation
--------------
-->Is the process of binding data and menthods together 

'''

class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def depo(self, amount):
        self.__balance += amount

    def get_balace(self):
        return self.__balance

acc = Bank(1000)
acc.depo(10000)
print(acc.get_balace())































