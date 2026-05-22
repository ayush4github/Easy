from itertools import chain
def sum_of_all_elements_of_matrix(matrix):
    total_sum = sum(chain.from_iterable(matrix))
    print(total_sum)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_all_elements_of_matrix(matrix)