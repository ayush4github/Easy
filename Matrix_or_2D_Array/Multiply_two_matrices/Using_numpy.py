import numpy as np
def multiply_two_matrices(matrix1, matrix2):
    array1 = np.array(matrix1)
    array2 = np.array(matrix2)
    result = np.matmul(matrix1, matrix2)
    for row in result:
        print(row)
matrix1 = [
    [1, 2],
    [3, 4]
]
matrix2 = [
    [5, 6],
    [7, 8]
]
multiply_two_matrices(matrix1, matrix2)