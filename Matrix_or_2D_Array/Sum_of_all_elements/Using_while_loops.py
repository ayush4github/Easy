def sum_of_all_elements_of_matrix(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    total_sum = 0
    row_index = 0
    while row_index < number_of_rows:
        column_index = 0
        while column_index < number_of_columns:
            total_sum = total_sum + matrix[row_index][column_index]
            column_index +=1
        row_index +=1
    print(total_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_all_elements_of_matrix(matrix)