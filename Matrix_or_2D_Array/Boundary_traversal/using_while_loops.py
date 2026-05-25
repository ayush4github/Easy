def boundary_traversal_using_while_loops(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    #Top row
    column_index = 0
    while column_index < number_of_columns:
        print(matrix[0][column_index], end = " ")
        column_index +=1
    #Right column
    row_index = 1
    while row_index < number_of_rows:
        print(matrix[row_index][number_of_columns-1], end = " ")
        row_index +=1
    #Bottom row
    column_index = number_of_columns -2
    while column_index >= 0:
        print(matrix[number_of_rows-1][column_index], end = " ")
        column_index -=1
    #Left column
    row_index = number_of_rows-2
    while row_index > 0:
        print(matrix[row_index][0], end = " ")
        row_index -=1
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
boundary_traversal_using_while_loops(matrix)