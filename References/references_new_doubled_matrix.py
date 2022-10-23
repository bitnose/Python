from copy import deepcopy


def new_doubled_matrix(matrix):
    doubled_matrix = deepcopy(matrix)

    for row in range(len(doubled_matrix)):        
        for col in range(len(doubled_matrix[row])):
           doubled_matrix[row][col] = doubled_matrix[row][col] * 2
            
    return doubled_matrix
            
def main():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = new_doubled_matrix(m1)
    print(m1)
    print(m2)
main()