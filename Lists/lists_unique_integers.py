def unique_integers(a):
    return set(a)

def main():
    numbers = []
    for i in range(5):
        number = int(input("Enter an integer: "))
        numbers.append(number)

    print(*(unique_integers(numbers)), sep=", ")
    print(*(sorted(numbers)), sep=", ")

if __name__ == "__main__":
    main()
