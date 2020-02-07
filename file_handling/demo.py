file_path = 'demo.py'

file = open(file_path, 'r')

index = 1
while True:
    line = file.readline()
    if not line:
        break
    print(f'{index}: {line}', end='')
    index += 1

print('-' * 50)

file = open(file_path, 'r')
for line in file:
    print(line, end='')