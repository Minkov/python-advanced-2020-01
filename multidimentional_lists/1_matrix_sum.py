def read_matrix():
    (rows_count, columns_count) = map(int, input().split(', '))
    return [list(map(int, input().split(', '))) for _ in range(rows_count)]


def sum_matrix(matrix):
    the_sum = 0
    rows_count = len(matrix)

    for row_index in range(rows_count):
        the_sum += sum(matrix[row_index])

    return the_sum


# matrix = [
#     [7, 1, 3, 3, 2, 1],
#     [1, 3, 9, 8, 5, 6],
#     [4, 6, 7, 9, 1, 0],
# ]

matrix = read_matrix()

print(sum_matrix(matrix))
print(matrix)
