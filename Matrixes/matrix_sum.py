from operator import index

def print_matrix_sum(m, n):
    for row in range(len(m)):
        for col in range(len(m[0])):
            x= m[row][col] + n[row][col]
            print(x, end=" ")
        print()  

def main():
    m1 = [[1, 2, 0], [2, 3, 4]]
    m2 = [[3, 2, 5], [6, 4, 3]]
    m3 = [[1, 1, 1, 1], [3, 3, 2, 1], [2, 2, 2, 2]] 
    m4 = [[2, 2, 2, 3], [2, 3, 1, 0], [1, 2, 3, 4]]
    
    print_matrix_sum(m1, m2)
    print()
    print_matrix_sum(m3, m4)
    
main()