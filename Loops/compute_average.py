sum = 0
counter = 0
number = float(input("Enter first number: "))

while number != 0:
    sum += number
    counter += 1
    number = float(input("Enter next number: "))

if counter == 0:
    print(f"Nothing to be calculated")
else:
    print(f"The average is {sum/counter:.2f}")

