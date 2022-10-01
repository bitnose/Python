names = []
surname = input("Enter a surname (ok ends): ")

while surname != "ok":
    names.append(surname)
    surname = input("Enter a surname (ok ends): ")

#remove duplicates
surnames = list(set(names))
surnames.sort()
print()
print(*surnames, sep=", ")