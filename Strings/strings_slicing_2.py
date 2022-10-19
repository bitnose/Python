# first inputs a string. 
# print the next to last character in the string. 
# If the string has less than two characters, the program should print "Too short string".

a = str(input("Enter a string: "))

if len(a) < 3:
    print("Too short string")
else: 
    print(a[-2])