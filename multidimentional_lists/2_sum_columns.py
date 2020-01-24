def read_matrix(cells_delimiter):
    (rows_count, columns_count) = map(int, input().split(', '))
    return [list(map(int, input().split(cells_delimiter))) for _ in range(rows_count)]

def get_column_sums(matrix):
    rows_count = len(matrix)
    columns_count = len(matrix[0])
    column_sums = [0] * columns_count
    for row in range(rows_count):
        for column in range(columns_count):
            column_sums[column] += matrix[row][column]

    return column_sums

def print_list(l):
    [print(element) for element in l]

matrix = read_matrix(' ')
columns_sums = get_column_sums(matrix)
print_list(columns_sums)
