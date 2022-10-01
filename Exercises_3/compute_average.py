sum = 0
counter = 0
number = float(input("Enter first number: "))

while number > 0:
    sum = sum + number
    counter += 1
    number = float(input("Enter next number: "))

    valid = "OK" if int(number) in range(
        1, 8) else "Please enter an integer between 1 and 7"
    print(valid)

try:
    print(f"The average is {sum/counter:.2f}")
except ValueError:
    print("Nothing to be calculated.")
