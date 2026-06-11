'''
                            FILE HANDLING:
                           ==============
File hander is an object of file to maintain several function of file like
creating, reading, updating, and deleting the file...

open a file
-----------
1.open
2.with open

name = open('filename','mode')
------
------
------
name.close()

modes
------
'r'--> is used read the file, error if file does not exit....
'a'--> is used to add the text into file, if file does not exit...
'w'--> is used to add the text into file but it will override of all txt
inside file. if the file doesnot exist will create with that name..
'x'-->ks used to create the file..but will throw error if we are used'r'
mode to crew
'r' mode to create.....

method
-------
write()
read()
-------
-->This method can read entire file chunk by chunk where we can specify
the size

readline()
-----------
-->Can read only one line at a time in a file

readlines
------------
--> it will read entire file and gives in a list where each line is each
index in a list
'''
import os
file = open("charan.txt","r")

print(file.readline())
charan.remove()

file.close()

