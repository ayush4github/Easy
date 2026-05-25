import numpy as np
def primary_diagonal_sum_using_numpy(matrix):
    array = np.array(matrix)
    diagonal_sum = np.trace(array)
    print(diagonal_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
primary_diagonal_sum_using_numpy(matrix)