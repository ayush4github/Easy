import numpy as np
def add_two_matrices(matrix1, matrix2):
    array1 = np.array(matrix1)
    array2 = np.array(matrix2)
    result = array1 + array2
    print(result)
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix2 = [
    [7, 8, 9],
    [1, 2, 3]
]
add_two_matrices(matrix1, matrix2)