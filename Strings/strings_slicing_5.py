# inputs a string and a character from the user. 
# The program should examine the inputted string and print all 4-character substrings,
# which start with the inputted character. 
# Substrings can overlap. If no such substring exists in the string, the program should not print anything more.
# NB! You should use a loop and slicing in this exercise.

text = str(input("Enter a string: "))
char = str(input("Enter a character: "))
index = 0

for a in text:
    if a == char:
        substring = text[index:(index+4)]
        if len(substring) == 4:
            print(substring)
    index += 1 


