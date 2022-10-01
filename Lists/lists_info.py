numbers = []

for i in range(5):
    number = int(input("Enter an integer: "))
    numbers.append(number)

numbers.sort(reverse=True)
print(f"\ncount:{len(numbers):3d}")
print(f"min:{min(numbers):5d}")
print(f"max:{max(numbers):5d}")
print(f"sum:{sum(numbers):5d}")