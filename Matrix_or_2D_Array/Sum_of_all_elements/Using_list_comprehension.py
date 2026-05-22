def sum_of_all_elements_in_matrix(matrix):
    elements = [element for row in matrix for element in row]
    total_sum = sum(elements)
    print(total_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_all_elements_in_matrix(matrix)