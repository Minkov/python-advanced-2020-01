def read_until_command(end_command):
    commands = []
    while True:
        command = input()
        if end_command == command:
            return commands
        commands.append(command)

def solve(commands):
    parking_lot = set()
    cars = []
    for command_string in commands:
        (command, car_number) = command_string.split(', ')
        cars.append(car_number)
        if command == 'IN':
            parking_lot.add(car_number)
        else:
            parking_lot.remove(car_number)
    cars = cars[::-1]
    result =sorted(parking_lot, key=lambda x: -cars.index(x))
    if result:
        [print(x) for x in result]
    else:
        print('Parking Lot is Empty')

# commands = [
#     'IN, CA2844AA',
#     'IN, CA1234TA',
#     'OUT, CA2844AA',
#     'IN, CA9999TT',
#     'IN, CA2866HI',
#     'OUT, CA1234TA',
#     'IN, CA2844AA',
#     'OUT, CA2866HI',
#     'IN, CA9876HH',
#     'IN, CA2822UU',
# ]

commands = read_until_command('END')
solve(commands)