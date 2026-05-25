def diagonal_sum_of_matrix(matrix):
    diagonal_sum = 0
    for row_index in range(len(matrix)):
        for column_index in range(len(matrix[0])):
            if row_index == column_index:
                diagonal_sum = diagonal_sum + matrix[row_index][column_index]
    print(diagonal_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum_of_matrix(matrix)
