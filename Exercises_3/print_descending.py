number = input("Enter an integer: ")
sum = 0

try:
    number = int(number)
    for i in range(number, 0, -1):
        sum = sum + i
        print(i, end=" ")
    print(f"\nThe sum is {sum}" if sum != 0 else "Nothing to be printed")

except ValueError:
    print("Nothing to be printed")
