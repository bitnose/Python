count = int(input("How many surnames? "))
surnames = []

for i in range(count):
    surname = input("Enter a surname: ").capitalize()
    surnames.append(surname)

print()
print(*sorted(set(surnames)))