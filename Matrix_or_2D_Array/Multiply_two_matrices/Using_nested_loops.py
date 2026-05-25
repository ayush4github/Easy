def multiply_two_matrices(matrix1, matrix2):
    number_of_rows = len(matrix1)
    number_of_columns = len(matrix2[0])
    common_size = len(matrix2)
    result = []
    for row_index in range(number_of_rows):
        row = []
        for column_index in range(number_of_columns):
            value = 0
            for index in range(common_size):
                value = value + (matrix1[row_index][index]*matrix2[index][column_index])
            row.append(value)
        result.append(row)
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