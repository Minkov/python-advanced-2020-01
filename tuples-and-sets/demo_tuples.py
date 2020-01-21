dd = {
    3.14: [1, 2, 3],
    1.23: 3,
}

for key in dd.keys():
    print(key)

for value in dd.values():
    print(value)

for key, value in dd.items():
    print(key, value)