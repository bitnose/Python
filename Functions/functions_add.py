def add(a: float, b: float) -> int:
    result = a + b
    return int(0.5 + result)


def main():
    try:
        a = float(input("Enter a float: "))
        b = float(input("Enter a float: "))
        result = add(a, b)
        print(result)

    except (ValueError):
        print("Wrong value")


main()
