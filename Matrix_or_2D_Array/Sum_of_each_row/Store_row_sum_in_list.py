def sum_of_elements_of_each_row(matrix):
    row_sums = []
    for row in matrix:
        row_sums.append(sum(row))
    print(row_sums)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_elements_of_each_row(matrix)