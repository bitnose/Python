def double_factorial(number: int) -> int:
    result = 1
    if number >= 0:
        even = 2 if number % 2 == 0 else 1
        for i in range(even, number+1, 2):
            finalresult = result * i

            return finalresult
    else:
        print("Please enter a non-negative integer")


def main():
    for i in range(10):
        result = double_factorial(i)
        print(f"{i}!! = {result}")


main()

# 0!! is 1        5!! = 1 x 3 x 5 = 15       6!! = 1 x 2 x 4 x 6 = 48
