def read_until_command(end_command):
    commands = []
    while True:
        command = input()
        if end_command == command:
            return commands
        commands.append(command)


def solve(reservations, attending):
    not_attending = set(reservations) ^ set(attending)
    result = sorted(not_attending, key=reservations.index)
    print(len(result))
    [print(x) for x in result if x[0].isdigit()]
    [print(x) for x in result if not x[0].isdigit()]


# reservations = [
#     '7IK9Yo0h',
#     '9NoBUajQ',
#     'Ce8vwPmE',
#     'SVQXQCbc',
#     'tSzE5t0p',
# ]
# attending = [
#     '9NoBUajQ',
#     'Ce8vwPmE',
#     'SVQXQCbc',
# ]

reservations = read_until_command('PARTY')
attending = read_until_command('END')

solve(reservations, attending)
