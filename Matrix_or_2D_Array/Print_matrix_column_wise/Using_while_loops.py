def print_matrix_column_wise(matrix):
    number_of_rows = len(matrix)
    number_of_column = len(matrix[0])
    column_index = 0
    while column_index < number_of_column:
        row_index = 0
        while row_index < number_of_rows:
            print(matrix[row_index][column_index], end = " ")
            row_index +=1
        print()
        column_index +=1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_column_wise(matrix)