
    # 1. Get the numbers between 1-9
    # 2. Counter to count how many times numbers appear: Each time set up to zero when new iteration starts. 1 -> 2 etc
    # 3. Loop through the selected rows. 
    # 4. Loop through the selected columns 
    # 5. Check how many times the number appears in given columns.
    # 6. If appears more than one, stop execution and return False. Else keep iterating. 
    
def block_ok(matrix, row_index: int, column_index: int):

    if row_index not in (0, 3, 6) or column_index not in (0, 3, 6):
        return False

    for numb in range(1, 10):
        count = 0
        for row in matrix[row_index:row_index+3]:
            for col in row[column_index:column_index+3]:
                if col == numb:
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


    print(block_ok(sudoku, row_index=0, column_index=0))
    print(block_ok(sudoku, row_index=3, column_index=6)) 
    print(block_ok(sudoku, row_index=6, column_index=3))

if __name__ == "__main__":
    main()

# False
# True
# True