def print_matrix_column_wise(matrix):
    for column in zip(*matrix):
        for element in column:
            print(element, end = " ")
        print()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_column_wise(matrix)