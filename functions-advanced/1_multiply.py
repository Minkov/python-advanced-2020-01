def multiply(*args):
    result = 1

    for x in args:
        result *= x

    return result


tests = [
    [[1, 2, 3, 4, 5, 6, 7], 5040],
    [[1, -2], -2],
    [[-1, -2], 2],
    [[-1, 0], 0],
    [[-1], -1],
    [[-1.13, 2], -2.26],
]


def handle_result(args, expected_result):
    result = multiply(*args)
    if result != expected_result:
        print(args, expected_result)


results = [handle_result(args, expected_result) for
           (args, expected_result) in tests]
