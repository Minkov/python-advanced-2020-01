def read_matrix(cells_delimiter):
    n = int(input())
    return [list(map(int, input().split(cells_delimiter))) for _ in range(n)]

def calculate_sum(matrix, row_func, col_func):
    the_sum = 0
    n = len(matrix)
    for x in range(n):
        row = row_func(x, n)
        col = col_func(x, n)
        the_sum += matrix[row][col]
    return the_sum

def calculate_primary_diagonal_sum(matrix):
    return calculate_sum(matrix, lambda x, n: x, lambda x, n: x)


def calculate_seconday_diagonal_sum(matrix):
    return calculate_sum(matrix, lambda x, n: x, lambda x, n: n - x - 1)


matrix = read_matrix(' ')

print(calculate_primary_diagonal_sum(matrix))
# print(calculate_seconday_diagonal_sum(matrix))
