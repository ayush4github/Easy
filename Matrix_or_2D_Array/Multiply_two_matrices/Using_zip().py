def multiply_two_matrices(matrix_1, matrix_2):
    transpose_matrix_2 = list(zip(*matrix_2))
    result = []
    for row in matrix_1:
        result_row = []
        for column in transpose_matrix_2:
            value = 0
            for element_1, element_2 in zip(row, column):
                value = value + (element_1 * element_2)
            result_row.append(value)
        result.append(result_row)
    for row in result:
        print(row)
matrix_1 = [
    [1, 2],
    [3, 4]
]
matrix_2 = [
    [5, 6],
    [7, 8]
]
multiply_two_matrices(matrix_1, matrix_2)