# Function to find double
# factorial of given number
def double_factorial(number: int):
    result = 1
    if number >= 0:
        even = 2 if number % 2 == 0 else 1
        for i in range(even, number+1, 2):
            result *= i
        return result
    else:
        print("Please enter a non-negative integer")
     
def main():
    for i in range(10):
        result = double_factorial(i)
        print(f"{i}!! = {result}")

main()

