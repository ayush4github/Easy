def print_matrix_row_wise(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            print(matrix[row_index][column_index], end = " ")
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_row_wise(matrix)