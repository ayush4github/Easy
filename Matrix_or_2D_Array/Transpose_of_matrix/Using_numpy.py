import numpy as np
def transpose_of_matrix(matrix):
    array_converted_matrix = np.array(matrix)
    transpose = array_converted_matrix.T
    print(transpose)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose_of_matrix(matrix)