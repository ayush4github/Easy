def standard_boundary_traversal(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    #Top row
    for column_index in range(number_of_columns):
        print(matrix[0][column_index], end = " ")
    #Right column
    for row_index in range(1, number_of_rows):
        print(matrix[row_index][number_of_columns-1], end = " ")
    #Bottom row
    for column_index in range(number_of_columns-2, -1, -1):
        print(matrix[number_of_rows-1][column_index], end = " ")
    #Left column
    for row_index in range(number_of_rows-2, 0, -1):
        print(matrix[row_index][0], end = " ")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
standard_boundary_traversal(matrix)