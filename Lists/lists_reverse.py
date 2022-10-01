amount = int(input("How many integers? "))
numbers = []

for i in range(amount):
    number = int(input("Enter an integer: "))
    numbers.append(number)

numbers.reverse()
print()
print(*numbers)