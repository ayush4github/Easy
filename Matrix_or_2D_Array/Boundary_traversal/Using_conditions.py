def boundary_traversal_using_conditions(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            if (
                row_index == 0 
                or row_index == number_of_rows -1
                or column_index == 0
                or column_index == number_of_columns -1
                ):
                print(matrix[row_index][column_index], end = " ")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
boundary_traversal_using_conditions(matrix)