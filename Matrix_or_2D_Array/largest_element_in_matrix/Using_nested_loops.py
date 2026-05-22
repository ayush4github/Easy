def largest_element_matrix(matrix):
    largest_element = matrix[0][0]
    for row in matrix:
        for element in row:
            if element > largest_element:
                largest_element = element
    print(largest_element)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
largest_element_matrix(matrix)