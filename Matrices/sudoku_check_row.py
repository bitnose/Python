# SUDOKU

# 0 = an empty square in a sudoko grid
# row is ok if each of the digits between 1 and 9 appears zero or one times on the row
# The row is not ok if any of the digits between 1 and 9 appears more than once on the row.

from pickle import FALSE


def row_ok(matrix, row_index):

    for x in range(1, 10):
        if matrix[row_index].count(x) > 1:
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
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]   
    print(row_ok(sudoku, row_index=0)) # True
    print(row_ok(sudoku, row_index=1)) # False
    print(row_ok(sudoku, row_index=8)) # True

if __name__ == "__main__":
    main()


