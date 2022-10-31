def swap(numbers):

    index = 0
    for i in range(len(numbers)//2):
        numbers[index], numbers[index+1] = numbers[index+1], numbers[index]
        index +=2
    
    return numbers
    


def main():

    numbers = []
    for i in range(7):
        number = int(input("Enter an integer: "))
        numbers.append(number)
    
    print(swap(numbers))
    

if __name__ == "__main__":
    main()
    