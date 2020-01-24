def read_input():
    n = int(input())
    return (
        [input() for _ in range(n)],
        input()
    )


def find_position(matrix, symbol):
    for i in range(len(matrix)):
        line = matrix[i]
        if symbol in line:
            return (i, line.index(symbol))

    return None

(matrix, symbol) = read_input()

result = find_position(matrix, symbol)
if result:
    (row, col) = result
    print(f'({row}, {col})')
else:
    print(f'{symbol} does not occur in the matrix')
