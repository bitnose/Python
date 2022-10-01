gigs = int(input("Number of gigs: "))
gigs_per_set = int(input("Gigs to be played with the same set of strings: "))
price = float(input("Price of a set of guitar strings: "))
# x = 0 if x > 10 else x + 1
# x on nolla jos x on isompi kuin 10, muuten lisää yksi


if gigs_per_set != 0:
    new_set = gigs / gigs_per_set
    even = gigs % gigs_per_set == True
else:
    new_set = 1
    cost = price

print(f"\nThe guitarist needs {new_set:.1f} new sets of strings")
print(f"The total cost is {cost:.2f} euros.")
