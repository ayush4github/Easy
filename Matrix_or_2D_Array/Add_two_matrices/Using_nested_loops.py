def add_two_matrices(matrix1, matrix2):
    number_of_rows = len(matrix1)
    number_of_columns = len(matrix1[0])
    result = []
    for row_index in range(number_of_rows):
        row = []
        for column_index in range(number_of_columns):
            sum_of_elements = matrix1[row_index][column_index] + matrix2[row_index][column_index]
            row.append(sum_of_elements)
        result.append(row)
    for row in result:
        print(row)
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix2 = [
    [7, 8, 9],
    [1, 2, 3]
]
add_two_matrices(matrix1, matrix2)