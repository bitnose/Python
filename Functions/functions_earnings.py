def compute_earnings(wage: float, hours: int):

    if hours > 40:
        overtime = (hours - 40) * wage * 1.5
        earnings = 40 * wage
        return overtime + earnings
    else:
        return hours * wage


def main():

    try:
        wage = float(input("Enter wage: "))
        hours = int(input("Enter hours: "))

        earnings = compute_earnings(wage, hours)
        print(f"The earnings are {earnings:.2f}")

    except (ValueError):
        print("Wrong value")


main()
