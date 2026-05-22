def sum_of_each_row(matrix):
    row_sums = [sum(row) for row in matrix]
    print(row_sums)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_each_row(matrix)