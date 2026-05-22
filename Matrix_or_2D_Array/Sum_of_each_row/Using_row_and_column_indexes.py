def sum_of_elements_of_each_row(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    for row_index in range(number_of_rows):
        row_sum = 0
        for column_index in range(number_of_columns):
            row_sum = row_sum + matrix[row_index][column_index]
        print(row_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_elements_of_each_row(matrix)