def parse_row(string):
    return map(int, string.split(', '))


rows_count = int(input())
matrix = [parse_row(input()) for _ in range(rows_count)]

result = [[x for x in row if x % 2 == 0] for row in matrix]

print(result)
