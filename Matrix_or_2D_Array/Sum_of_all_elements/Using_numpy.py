import numpy as np
def sum_of_elements_of_matrix(matrix):
    total_sum = np.sum(matrix)
    print(total_sum)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
sum_of_elements_of_matrix(matrix)