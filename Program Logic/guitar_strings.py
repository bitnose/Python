gigs = int(input("Number of gigs: "))
gigs_per_set = int(
    input("Gigs to be played with the same set of strings: "))
price = float(input("Price of a set of guitar strings: "))

if gigs_per_set != 0:

    full_set = gigs // gigs_per_set
    division = gigs % gigs_per_set
    print(f"{division}")

    if division != 0:
        full_set += 1
        print(f"{full_set}")

    cost = full_set * price

else:
    cost = price
    full_set = 1

print(f"\nThe guitarist needs {full_set:.0f} new sets of guitar strings")
print(f"The total cost is {cost:.2f} euros.")
