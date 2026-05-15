# 1. progarm to convert 24h clock into normal clock
'''
time = "20:37"
parts = time.split(":")
print(parts)
hour = int(parts[0])
mins = int(parts[1])
#if hours >= 12:
print(f"{time} is converted into {hour - 12}:{mins} pm")
    
print(hour)
print(mins)

'''
'''
LIST
-----
--> LIST is collection of differnt data type
-->[]and seperated by ","
--> example : any = [1,"python",[1,2]]
              print(any)
              
a = [1,"python", [1,2,[34,"this python 3rd class",78]],
                  ["python is a language",89],34,[3,4]]
print(a[2][2][1][5])
print(a[3][1])

methods
--------
append()
--------
-->this method is used to add new item into list and it will be in
the last  index position

any = [1,2,3]
any.append(6)
print(any)

extend()
-------
-->This method is used to add itterable into list and it will in the
last index position, each value or substring is each index in the list

syntax--> variable_name.extend(itterables)

pop()
-----
--> used to remove the item from the list, but will mention here
index position in the pop method

remove()
--------


STRING IS IMMUTABLE
------------------
EXAMPLE ;
CO = "PYHON IS EASY"
print(co.replace("PYHON","JAVA"))
print(co)

Immutable
----------
--> Could not able to modify on that particular variable
eg: int, str

Mutable
--------
--> Can able to modify on that particular variable
eg: list




'''

any =[1,2,3,"int"]
any.remove("int")
print(any)




















