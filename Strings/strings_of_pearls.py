from tokenize import String
a = input("Enter first string: ")
pearl_count = None

try:
    while str(a).lower() != "quit": 
        if a.lower() == "pearl":
            pearl_count += 1
        a = input("Enter second string: ")
    
    print()
    if pearl_count != None:
        print(f"{pearl_count} pearls")
    print("Bye!")

except ValueError:
    print(f"'Is not a string")