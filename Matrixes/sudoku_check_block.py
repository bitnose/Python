def block_ok(matrix, row_index, column_index):

    for row in :
            matrix[row_index]
            matrix[row_index+1]
            matrix[row_index+3]


    # column_index - 3
    # row_index 
    for x in range(1, 10):
        count = 0
        for row in row_index:
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
        [7, 0, 5, 0, 6, 0, 4, 0, 6],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]]


    print(block_ok(sudoku, row_index=0, column_index=0))
    print(block_ok(sudoku, row_index=3, column_index=6)) 
    print(block_ok(sudoku, row_index=6, column_index=3))

if __name__ == "__main__":
    main()

# False
# True
# True