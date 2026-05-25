def multiply_two_matrices(matrix1, matrix2):
    result = [[sum(matrix1[row_index][index]*matrix2[index][column_index] for index in range(len(matrix2))) for column_index in range(len(matrix2[0]))] for row_index in range(len(matrix1))]
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