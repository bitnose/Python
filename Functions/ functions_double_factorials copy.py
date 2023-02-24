def double_factorial(number: int) -> int:
    result = 1
    if number >= 0:
        for i in range(number, -1, -2):
            if
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
 
# Function to find double
# factorial of given number
def doublefactorial(n):
    res = 1;
    for i in range(n, -1, -2):
        if(i == 0 or i == 1):
            return res;
        else:
            res *= i;
     
