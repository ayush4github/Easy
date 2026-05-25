def transpose_of_matrix(matrix):
    transpose = [list(column) for column in zip(*matrix)]
    for row in transpose:
        print(row)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose_of_matrix(matrix)