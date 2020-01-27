def in_range(value, max_value):
    return 0 <= value < max_value


n = 6

row_dirs = [0, +1, 0, -1]
col_dirs = [+1, 0, -1, 0]

matrix = [[None] * n for _ in range(n)]

dir = 0
row = 0
col = 0

for count in range(n * n):
    matrix[row][col] = count + 1
    next_row = row + row_dirs[dir]
    next_col = col + col_dirs[dir]
    if not in_range(next_row, n) \
            or not in_range(next_col, n) \
            or matrix[next_row][next_col]:
        dir += 1
        dir %= 4
    row += row_dirs[dir]
    col += col_dirs[dir]

[print(row) for row in matrix]
