def transpose_of_matrix(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    transpose = []
    for column_index in range(number_of_columns):
        row = []
        for row_index in range(number_of_rows):
            row.append(matrix[row_index][column_index])
        transpose.append(row)
    print(transpose)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose_of_matrix(matrix)