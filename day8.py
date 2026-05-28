'''
elif:
-----

stu_Name = input("Enter Student Name : ")
stu_marks = int(input("Enter student Marks"))
if stu_marks >= 90:
    print("A+")
elif stu_marks >=80:
    print("A")
elif stu_marks >=70:
    print("B+")
elif stu_marks >=60:
    print("B")
elif stu_marks >=50:
    print("C+")
elif stu_marks >=35:
    print("Pass")
else:
    print("Failed")
-------------------------------------------------------------------------------

num = input("enter any three numbers :").split()
num1 = int(num[0])
num2 = int(num[1])
num3 = int(num[2])

if num1>num2 and num1>num3:
    print("{num1} number is greater")
elif num2>num1 and num2>num3:
    print(f"{num2} number is greater ")
else:
    print(f"{num3} number is greater")

----------------------------------------------------------------------------
SBI_bank = {"ATM PIN":"4536"}

pin = input("Enter 4 digit number :")
if len(pin)==4:
    if pin in SBI_bank["ATM PIN"]:
        print("Welcome to SBI ATM")
    else:
        print("Invalid Pin")
else:
    print("Enter 4 digit PIN")

*forloop
--------
--> used to itterate over a sequence

a = input()
for j in (a):
    print(j)

range()
-------
range is in-built function used to generate numbers in squence manner

syntax -->range(start,end,range)

else in for
------------
--> Once the itteration completed this else will be

break
------
-->used to exit from the loop based on condition  

continue
--------
-->Used to skip the current itteration based on the condition

pass
------
for i in range (2,100):
    if i%5 == 0:
        if i==40:
            pass
        print(i,end=",")
while
======
while is a combination of for and if conditions

'''

i = 1
while i<5:
    print(i)
    i += 1























