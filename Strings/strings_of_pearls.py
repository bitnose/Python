from tokenize import String

a = str(input("Enter first string: ")).lower()
pearl_count = 0

if a == "quit":
    print("Bye!")
    
else:
    while a != "quit": 
        if a == "pearl":
            pearl_count += 1
        a = str(input("Enter next string: ")).lower()

    if pearl_count > 0:
        print(f"{pearl_count} pearls")
        print("Bye!")