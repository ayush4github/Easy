def sum_of_elements_of_matrix(matrix):
    total_sum = 0
    for row in matrix:
        total_sum = total_sum + sum(row)
    print(total_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_elements_of_matrix(matrix)