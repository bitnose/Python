from curses.ascii import NUL


def sum_every_other(numbers):
    sum = 0
    for i in range(0, len(numbers), 2):
        sum += numbers[i]
    
    if sum==0:
        return None

    return sum

def main():
    arr = [0, 2, 0, 4, 0, 6, 0]
    print(sum_every_other(arr))

if __name__ == "__main__":
    main()