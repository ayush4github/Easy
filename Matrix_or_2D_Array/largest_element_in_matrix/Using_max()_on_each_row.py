def largest_element_in_matrix(matrix):
    largest_element = matrix[0][0]
    for row in matrix:
        row_maximum = max(row)
        if row_maximum > largest_element:
            largest_element = row_maximum
    print(largest_element)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
largest_element_in_matrix(matrix)