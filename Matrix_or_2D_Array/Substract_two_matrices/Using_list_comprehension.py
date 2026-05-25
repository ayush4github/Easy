def subtract_two_matrices(matrix1, matrix2):
    result = [[matrix1[row_index][column_index]-matrix2[row_index][column_index] for column_index in range(len(matrix1[0]))] for row_index in range(len(matrix1))]
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