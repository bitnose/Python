first = input("Enter first string: ")
second = input("Enter second string: ")
subset_found = False

if second != "":
    for a in second:
        if a in first:
            subset_found = True
        else:
            subset_found = False
            break
    print(f"Subset" if subset_found else "Not subset")
else:
    print("Nothing to be checked")

