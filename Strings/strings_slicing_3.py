
# First inputs a string. 
# Print all substrings of the string, which start from the first position in the string. 
# The substrings should be printed as shown in the example output.
# You should use slicing in this exercise. 
# Hint: A loop is useful here.

input = str(input("Enter a string: "))

for a in range(len(input)):
    print(input[:a+1])