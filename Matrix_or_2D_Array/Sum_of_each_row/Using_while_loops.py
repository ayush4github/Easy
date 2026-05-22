def sum_of_each_row(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    row_index = 0
    while row_index < number_of_rows:
        row_sum = 0
        column_index = 0
        while column_index < number_of_columns:
            row_sum = row_sum + matrix[row_index][column_index]
            column_index +=1
        print(row_sum)
        row_index +=1
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_each_row(matrix)