def sum_of_each_column(matrix):
    for column in zip(*matrix):
        print(sum(column))
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_each_column(matrix)