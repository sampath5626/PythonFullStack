'''
num = 0
num_2 = 1
def fabonacci(num,num_2):
    limit= int(input("enter the limit : "))
    print(num,num_2,end=" ")
    for i in range(1,limit):
        num_3 = num+num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=" ")
fabonacci(num,num_2)

any = list(map(int,input("enter the values : ").split(" ")))
#any = [2,5,7,9,2,7,7]
new =[]
def dup(any,new):
    for j in any:
        if j not in new:
            new.append(j)
    print(new)
dup(any,new)

count = 0
so =input().split()
def word_str(so,count):
    for i in so:
        count += 1
    print(count)
word_str(so,count)

def van(num1,num2):
    pass
van(2,3)
'''
a = input("enter ur name")
b = int(input())
print(f"my name is {a} and my age is {a+b} ")
