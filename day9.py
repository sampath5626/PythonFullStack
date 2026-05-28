
'''
a = int(input("enter a table number :"))
for i in range (1,11):
    m =a*i
    print(f"{a}x{i}={m}")
---------------------------------------------------------------------------

#palandrome
-----------
c = input()
v = ""
for i in c:
    v = i+v
print(v)
if v == c:
    print(f"{c} is a plandrome")
else:
    print(f"{c} is not a plandrome")
---------------------------------------------------------------------------

#Amstrong
----------
num = 163
ams = 0
lenght = len(str(num))
for i in str(num):
    ams += int(i)**lenght
    
if ams == num:
    print(f"{num} is a amstrong")
else:
    print(f"{num} is not a amstrong")
print(ams)
---------------------------------------------------------------------------

#Perfect number
---------------
num = 28
pf =0
for j in range(1,num):
    if num%j==0:
        pf+=j
if pf == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} not a perfect number")
---------------------------------------------------------------------------

#Prime number
--------------
a = int(input("Enter a number to check wheather is a prime or not :"))
c = 0
for i in range (1,a+1):
    if a%i==0:
        c+=1
if c == 2:
    print(f"{a} is a prime number")
else :
    print(f"{a} is not a prime number")
---------------------------------------------------------------------------


s = 5
for i in range(1,s+1):
    for j in range(1,i+1):
        print("*",end="")
    print()


s = 5
c = 0
for i in range(1,s+1):
    for j in range(1,i):
        c+=1
        print(c,end=" ")
    print()

s = 5
c = 0
for i in range(1,s+1):
    for j in range(1,i+1):
        c+=1
        print(j,end=" ")
    print()

s = 5
c = 0
for i in range(s,0,-1):
    for j in range(i):
        c+=1
        print("*",end=" ")
    print()
    
num = 5
for j in range(1,num+1):
    print(" "*(num-j), end ="")
    for i in range(1,j+1):
        print("*",end=" ")
    print()





















































