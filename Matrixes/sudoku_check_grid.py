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

def row_ok(matrix, row_index):

    for x in range(1, 10):
        if matrix[row_index].count(x) > 1:
            return False
    return True


def grid_ok(matrix):

    for x in range(len(matrix)):
        if row_ok(matrix, x) == False:
            return False
        
        if column_ok(matrix, x) == False:
            return False

    for x in range(0, 7, 3):
        for y in range(0, 7, 3):
            if block_ok(matrix, x, y) == False:
                return False
                
    return True
    
        
def main():
    sudoku_1 = [[9, 0, 0, 0, 8, 0, 3, 0, 0], 
        [2, 0, 0, 2, 5, 0, 7, 0, 0], 
        [0, 2, 0, 3, 0, 0, 0, 0, 4], 
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0], 
        [7, 0, 5, 0, 6, 0, 4, 0, 0], 
        [0, 0, 7, 8, 0, 3, 9, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    sudoku_2 = [[2, 6, 7, 8, 3, 9, 5, 0, 4], 
        [9, 0, 3, 5, 1, 0, 6, 0, 0], 
        [0, 5, 1, 6, 0, 0, 8, 3, 9], 
        [5, 1, 9, 0, 4, 6, 3, 2, 8], 
        [8, 0, 2, 1, 0, 5, 7, 0, 6], 
        [6, 7, 4, 3, 2, 0, 0, 0, 5], 
        [0, 0, 0, 4, 5, 7, 2, 6, 3], 
        [3, 2, 0, 0, 8, 0, 0, 5, 7], 
        [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]
    print(grid_ok(sudoku_1)) # False 
    print(grid_ok(sudoku_2)) # True

if __name__ == "__main__":
    main()

