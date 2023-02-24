import statistics


def above_average(numbers):

    above_avg = []
    average = statistics.mean(numbers)

    for x in numbers:
        if x > average:
            above_avg.append(x)

    return sorted(above_avg)


def main():

    numbers = []
    a = int(input("Enter an int: "))

    while a != 0:
        numbers.append(a)
        a = int(input("Enter an int: "))

    if len(numbers) > 0:
        print(f"\n{above_average(numbers)}")
    else:
        print()
        print(numbers)


main()
