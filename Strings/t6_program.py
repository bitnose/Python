from email.policy import strict
from itertools import count
import re
from tracemalloc import stop


s = " "
s.upper()
print(s)
print(s.upper())

a = "a"
print(len(a))
# 1

b = "HELLO"
print(b.find("LL"))



text = " abcc  "
print(max(text))
print(text)
print(text.strip())
print(text.strip().capitalize())

text = "Version"
letter_count = 0
digit_count = 0
is_letters = False


s = "STOP" 
a=1
b=3 

# 7.0
print(s[a:b]) 
print(s[1:3]) 
print(s[:]) 
print(s[1:]) 
print(s[:1]) 
print(s[::2]) 
print(s[::-3]) 
print(s[::-1])

print()
print()
s = "A B C"
print(s.split())


print()
print()
# Creates two string variables
x = "1,2,3"
c = ","
#Prints the variable
print(x)
# Splits the string x using "," as a separator. Creates a list and assigns it to variable. 
y = x.split(c)
# Creates a string by joining the strings of the list together and adding "," separator and assigns it to variable.
z = c.join(y)
# Prints the z.
print(z)

a = ["4", "2", "9"]
b = ["4", "100"]
print(a > b)