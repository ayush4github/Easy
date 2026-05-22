def sum_of_each_row(matrix):
    for row in matrix:
        row_sum = 0
        for element in row:
            row_sum = row_sum + element
        print(row_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_each_row(matrix)