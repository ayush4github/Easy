import numpy as np
def subtract_two_matrices(matrix1, matrix2):
    array1 = np.array(matrix1)
    array2 = np.array(matrix2)
    result = array1-array2
    for row in result:
        print(row)
matrix1 = [
    [10, 20, 30],
    [40, 50, 60]
]
matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]
subtract_two_matrices(matrix1, matrix2)