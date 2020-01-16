from collections import deque


def solve_supermarket():
    names = deque()

    while True:
        command = input()
        if command == 'End':
            print(f'{len(names)} people remaining.')
            break

        if command == 'Paid':
            while names:
                print(names.popleft())
        else:
            names.append(command)


solve_supermarket()
