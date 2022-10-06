try:
    price = float(input("Enter price: "))
    VAT = 0.24
    total_price = price * (1 + VAT)
    print(f"The price with VAT is {total_price:.2f}")

except ValueError:
    print("Invalid price")
