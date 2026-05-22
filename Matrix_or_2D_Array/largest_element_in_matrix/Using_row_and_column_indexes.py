def largest_element_in_matrix(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    largest_element = matrix[0][0]
    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            if matrix[row_index][column_index] > largest_element:
                largest_element = matrix[row_index][column_index]
    print(largest_element)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
largest_element_in_matrix(matrix)