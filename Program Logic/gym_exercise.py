visits = int(input("Enter the number of days of gym visits per year: "))
day_pass = float(input("Enter price for a day pass: "))
membership = int(input("Enter yearly membership fee: "))
cost = visits * day_pass

# membership on kalliimpi
if cost < membership:
    print(f"Buying day passes is {membership-cost:.2f} euros cheaper")

elif cost > membership:
    print(
        f"Paying the yearly membership fee is {cost-membership:.2f} euros cheaper")
else:
    print("There is no price difference")
