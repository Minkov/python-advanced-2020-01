def read_matrix(cells_delimiter):
    (rows_count, columns_count) = map(int, input().split(', '))
    return [list(map(int, input().split(cells_delimiter))) for _ in range(rows_count)]

def find_best_submatrix(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    best_sum = None
    best_start = None

    for row in range(rows_count - 1):
        for col in range(columns_count - 1):
            current_sum = matrix[row][col] + \
                          matrix[row][col + 1] + \
                          matrix[row + 1][col] + \
                          matrix[row + 1][col + 1]
            if best_sum:
                if best_sum < current_sum:
                    best_sum = current_sum
                    best_start = (row, col)
            else:
                best_sum = current_sum
                best_start = (row, col)

    (row, col) = best_start
    best_submatrix = [
        [matrix[row][col], matrix[row][col + 1]],
        [matrix[row + 1][col], matrix[row + 1][col + 1]]
    ]

    return (best_sum, best_submatrix)


matrix = read_matrix(', ')

(best_sum, best_submatrix) = find_best_submatrix(matrix)

[print(' '.join(map(str,row))) for row in best_submatrix]
print(best_sum)