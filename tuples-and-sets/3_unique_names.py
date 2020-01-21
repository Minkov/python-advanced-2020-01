n = int(input())

# names = {input() for _ in range(n)}
names = []
for _ in range(n):
    names.append(input())

unique_names = list(set(names))

[print(name)
 for name
 in sorted(unique_names, key=names.index)]

