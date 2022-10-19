# First inputs a string. 
# Then the program should detect if the string reads the same backward as forward.
# If this is true, the program should print "Yes". 
# Otherwise, the program should print "No".
# For example, "12XOX21" reads the same backward as forward.
# NB! You should use slicing in this exercise. 
# After inputting a string, you can check it in a single if statement.

a = str(input("Enter a string: "))
print("Yes" if (a[::-1]) == a else "No")