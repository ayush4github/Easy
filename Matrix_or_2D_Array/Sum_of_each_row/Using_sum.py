def sum_of_each_row(matrix):
    for row in matrix:
        print(sum(row))
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_each_row(matrix)