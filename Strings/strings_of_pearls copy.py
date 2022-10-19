from tokenize import String
a = input("Enter first string: ")
pearl_count = 0
pearl = "pearl"

try:
    word = str(a).lower()
    if word == pearl: 
        pearl_count += 1
    a = input("Enter second string: ")

except ValueError:
    print(f"'{word}' is not an integer")
    

print("Bye!")