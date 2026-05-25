def secondary_diagonal_sum(matrix):
    total = 0
    size = len(matrix)
    for row_index in range(size):
        total = total + matrix[row_index][size-1-row_index]
    print(total)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
secondary_diagonal_sum(matrix)