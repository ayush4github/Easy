def subtract_two_matrices(matrix1, matrix2):
    number_of_rows = len(matrix1)
    number_of_columns = len(matrix1[0])
    result = []
    for row_index in range(number_of_rows):
        row = []
        for column_index in range(number_of_columns):
            difference = matrix1[row_index][column_index] - matrix2[row_index][column_index]
            row.append(difference)
        result.append(row)
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