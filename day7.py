'''

F-String
---------


STATEMENS
=========
* CONDITIONAL STATEMENTS
* CONTROL STATMENTS
* LOOP STATMENTS

CONDITIONAL STATEMENTS
-----------------------
-if -->  to check statement is true or not
-if-else --> else in the if statement, incase the condition becomes flase then
it will enter into fall-back(else), it will execute whatever inside it

example :

age = int(input("Enter you age : "))
if age >= 18:
    print("You are eligible to vote")
else:
    print(f"you have to wait for still {18 - age} more years")
    

year = int(input("Enter a year :"))
if (year % 4 ==0 and year % 100!= 0) or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
    

vowel = input("ente a alphabet")
if vowel in "AEIOUaeiou":
    print(f"{vowel} is a vowel")
else:
    print(f"{vowel} is a consonent")
    
num = int(input("Enter a number :"))
if num>=0:
    print(f"{num} is a positive num")
else:
    print(f"{num} is a negitive num")


num = int(input("Enter a number :"))
if num%3==0 and num%5==0:
    print(f"{num} is a divisible by 3 and 5")
else:
    print(f"{num} is not ")


    
-nested if --> e
-elif

num 




'''
























