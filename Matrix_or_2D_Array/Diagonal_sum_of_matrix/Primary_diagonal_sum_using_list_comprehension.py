def primary_diagonal_sum_using_list_comprehension(matrix):
    total = sum(matrix[index][index] for index in range(len(matrix)))
    print(total)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
primary_diagonal_sum_using_list_comprehension(matrix)