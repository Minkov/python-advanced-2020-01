def solve(str):
    s = []
    for ch in str:
        s.append(ch)

    reversed_str = ''

    while s:
        reversed_str += s.pop()

    return reversed_str


print(solve('I love Python'))
print(solve('Stacks and Queues'))

# I love Python
# I love Python
