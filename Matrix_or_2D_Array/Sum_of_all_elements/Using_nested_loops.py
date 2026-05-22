def sum_of_all_elements_of_matrix(matrix):
    total_sum = 0
    for row in matrix:
        for element in row:
            total_sum = total_sum + element
    print(total_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_all_elements_of_matrix(matrix)