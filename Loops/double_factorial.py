try:
    number = int(input("Enter a non-negative integer: "))
    result = 1
    if number >= 0:
        even = 2 if number % 2 == 0 else 1
        for i in range(even, number+1, 2):
            result = result * i
        print(f"{number}!! = {result}")
    else:
        print("Please enter a non-negative integer")
except ValueError:
    print("Please enter a non-negative integer.")
