numbers = []

for i in range(5):
    number = int(input("Enter an integer: "))
    numbers.append(number)

numbers.sort(reverse=True)
print()
print(*numbers)
