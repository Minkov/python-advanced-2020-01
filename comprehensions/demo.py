matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]
print(flattened)

result = []
for sublist in matrix:
    [result.append(num) for num in sublist]

print(result)