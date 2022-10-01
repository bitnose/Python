selling_price = int(input("Enter the car's selling price: "))

if selling_price < 50000:
    bonus = selling_price * 0.01
    if bonus < 200:
        bonus = 200
else:
    bonus = selling_price * 0.015

print(f"The bonus is {bonus:.2f} euros.")
