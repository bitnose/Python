def positive_sum(numbers):

    sum = 0
    for i in range(len(numbers)):
        if numbers[i] >= 0:
            sum += numbers[i]
    return sum

def main():
    
    numbers = list()
    for i in range(5):
        number = int(input("Enter an integer: "))
        numbers.append(number)
    sum = positive_sum(numbers)
    print(f"\n{sum}")

main()