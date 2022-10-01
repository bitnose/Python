def compute_discount(price: float, discount_percentage: float):
    return price*discount_percentage/100


def main():
    try:
        price = float(input("Enter price: "))
        discount_percentage = float(input("Enter discount percentage: "))
        discount = compute_discount(
            price=price, discount_percentage=discount_percentage)
        print(f"The discount is {discount:.2f} euros")

    except (ValueError):
        print("Value is not valid")


main()
