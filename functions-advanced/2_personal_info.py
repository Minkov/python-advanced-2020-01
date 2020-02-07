def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'


info = {"name": "George", "age": 20, "town": "Sofia", }
print(get_info(**info))

print(get_info(town='Burgas', name='Pesho', age=7))
