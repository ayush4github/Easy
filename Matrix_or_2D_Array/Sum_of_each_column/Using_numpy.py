import numpy as np
def sum_of_each_column(matrix):
    column_sums = np.sum(matrix, axis=0)
    print(column_sums)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_each_column(matrix)