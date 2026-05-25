def diagonal_sum_of_matrix(matrix):
    diagonal_sum = 0
    for index in range(len(matrix)):
        diagonal_sum = diagonal_sum + matrix[index][index]
    print(diagonal_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum_of_matrix(matrix)