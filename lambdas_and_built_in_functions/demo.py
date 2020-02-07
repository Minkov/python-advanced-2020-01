from functools import reduce

ll = [55] + list(range(10)) + [-1]
# 0, 2, 4, 6, 8

names = ['Gosho', 'Pesho', 'Stamat', 'asen']
print(min(ll))
print(max(ll))

print(sorted(names))
print(min(names))
print(max(names))


def step(aggregated_value, current_value):
    if current_value % 2 == 0:
        return aggregated_value + current_value
    return aggregated_value


print(ll)
print(reduce(lambda av, cv: av + cv if cv % 2 == 0 else av, ll, 0))
