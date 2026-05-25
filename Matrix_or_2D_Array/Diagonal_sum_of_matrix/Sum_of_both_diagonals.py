def sum_of_both_diagonals(matrix):
    size = len(matrix)
    total = 0
    for row_index in range(size):
        total = total + matrix[row_index][row_index]
        total = total + matrix[row_index][size-1-row_index]
    if size % 2 != 0:
        middle_element = matrix[size//2][size//2]
        total = total - middle_element
    print(total)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_both_diagonals(matrix)