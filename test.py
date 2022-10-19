try:
    age = int("text")
except ValueError:
    print("Not ineger")


print((1 < 10) == True)  # T
print(1 < 10 == True)  # F
print(False == 1 < 10)  # F
balance = 1000 * 1.05 - 1000 * 0.05 * 0.3
print(balance)

numbers = [3, 1, 4, 5]
numbers[1] = 5
numbers[4] = 2

for x in range(1, 10, 3):
    print(x)