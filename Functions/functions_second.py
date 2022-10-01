def print_rectangle(height: int, weight: int):

    for i in range(height):
        print(weight * "*")


def main():

    try:
        height = int(input("Enter height: "))
        weight = int(input("Enter weight: "))
        print_rectangle(height=height, weight=weight)

    except (ValueError):
        print("Enter an integer.")


main()
