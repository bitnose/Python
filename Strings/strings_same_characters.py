# inputs two strings. 
# remove blanks from the strings and then detect if the strings contain exactly the same set of characters. 
# The program should print "Same characters" if this is true. Otherwise, the program should print "Different characters".

# The characters are not required to be in the same order in both strings. 
# For example, "A1234A" and "AA2413" contain the same set of characters. 
# "BORROW" and "BROW" do not contain the same set of characters.

first = str(input("Enter first string: "))
second = str(input("Enter second string: "))

print("Same characters" if sorted(first.strip().lower()) == sorted(second.strip().lower()) else "Different characters")