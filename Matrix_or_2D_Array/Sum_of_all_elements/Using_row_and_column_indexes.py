def sum_of_all_elements_of_matrix(matrix):
    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])
    total_sum = 0
    for row_index in range(number_of_rows):
        for column_index in range(number_of_columns):
            total_sum = total_sum + matrix[row_index][column_index]
    print(total_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
] 
sum_of_all_elements_of_matrix(matrix)