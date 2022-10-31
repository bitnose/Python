def column_ok(matrix, column_index):

    # Print column
    for x in range(1, 10):
        count = 0
        for row in matrix:
            if row[column_index] == x:
                if count < 1:
                    count +=1
                else:
                    return False
    return True

    



def main():
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(column_ok(sudoku, column_index=0)) # False
    print(column_ok(sudoku, column_index=1)) # True
    print(column_ok(sudoku, column_index=8)) # True

if __name__ == "__main__":
    main()