'''
Regular Expression (RegEx)
--------------------------
-->RegEx is a sequence of char that form a searching pattern...
-->This can be used to check if a string contain athe specific search pattern
-->Python has built in package called "re". which can be used to work with
RegEx

Functions in re
---------------
1.Fimdall
2.search
3.fullmatch

Metachar
--------
"[]"-->a-z,A-Z.0-9 and any specify 
"."-->Here each dot is one char
"^"-->This look for the, string is starting with specified sequence or not
"$"-->This look for the, string is ending with specifed sequence or  not
"*"-->zero or more
"+"-->zero or one
"{}"-->

Special sequenc
---------------
\S --> No space
\s --> only space
\D --> non-digits
\d --> only-digits
\w --> matches any word char (letter, digits, underscore)
\W --> 
'''
import re
landline_no = input("Enter your land line number:")
hpw = re.fullmatch('[0][0-9]{9}',landline_no)
if hpw:
    print(f"{landline_no} is a landline number")
else:
    print(f"{landline_no} is not a landline number")
