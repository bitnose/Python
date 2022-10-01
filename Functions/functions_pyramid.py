def print_pyramid(height: int):

    result = 1
    for i in range(1, height+1):
        print((height - i) * " " + result * "*")
        result += 2


def main():
    try:
        height = int(input("Enter pyramid height:"))
        print_pyramid(height)

    except (ValueError):
        print("Enter correct value.")


main()
