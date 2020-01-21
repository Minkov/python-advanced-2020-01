def solve(values):
    occurances = {}
    for value in values:
        if value not in occurances:
            occurances[value] = 0

        occurances[value] += 1

    for number, count in occurances.items():
        print(f'{number} - {count} times')


values_strings = input().split(' ')
values = [float(x) for x in values_strings]
solve(values)
