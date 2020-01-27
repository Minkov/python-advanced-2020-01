def parse_row(string):
    return map(int, string.split(', '))


rows_count = int(input())
matrix = [parse_row(input()) for _ in range(rows_count)]

flattened = [num for sublist in matrix for num in sublist]
print(flattened)
