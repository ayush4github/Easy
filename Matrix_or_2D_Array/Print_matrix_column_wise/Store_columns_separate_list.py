def print_matrix_column_wise(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    column_wise_matrix = []
    for column_index in range(number_of_columns):
        column = []
        for row_index in range(number_of_rows):
            column.append(matrix[row_index][column_index])
        column_wise_matrix.append(column)
    for column in column_wise_matrix:
        print(column)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_column_wise(matrix)