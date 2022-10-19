from typing import List

#Function to count occurences in a two dimensional array
def count_occurrences(m, n:int):
    count = 0
    for row in m:
        for column in row:
            if column == n:
                count += 1
    return count

def main():
    m = [[1, 2, 3], [1, 2, 2], [1, 1, 1], [1, 2, 1]]
    print(count_occurrences(m, 1))
    print(count_occurrences(m, 2))
    print(count_occurrences(m, 5))

main()