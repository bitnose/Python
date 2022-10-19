# first inputs a string from the user. The program should check if any character occurs more than once in the string.
# If there are no duplicate characters in the string, the program should print "No duplicates". 
# Otherwise, the program should print "Contains duplicate(s)".
# NB! You should not write a loop is here. We can solve this problem using a set.

a = str(input("Enter a string: "))
print("Different characters" if len(set(a)) == len(a) else "Same characters")