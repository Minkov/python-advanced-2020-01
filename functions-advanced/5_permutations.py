def permutations(index, values, on_result):
    if index == len(values):
        on_result(values)

    for i in range(index, len(values)):
        values[index], values[i] = values[i], values[index]
        permutations(index + 1, values, on_result)
        values[index], values[i] = values[i], values[index]


def format_result(values):
    return ''.join(values)


permutations(0, list(input()),
             lambda x: print(format_result(x)))
