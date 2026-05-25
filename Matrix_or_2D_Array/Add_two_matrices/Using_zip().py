def add_two_matrices(matrix1, matrix2):
    result = []
    for row1, row2 in zip(matrix1, matrix2):
        row=[]
        for element1, element2 in zip(row1, row2):
            row.append(element1+element2)
        result.append(row)
    for row in result:
        print(row)
matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]
matrix2 = [
    [7, 8, 9],
    [1, 2, 3]
]
add_two_matrices(matrix1, matrix2)