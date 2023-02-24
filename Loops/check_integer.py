number = input("Enter an integer: ")
try:
    number = int(number)
    print("OK")
except ValueError:
    print(f"'{number}' is not an integer")
