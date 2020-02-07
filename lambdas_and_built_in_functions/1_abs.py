# numbers = map(float, input().split(' '))
# result = map(abs, numbers)
# print(list(result))

# numbers = map(float, input().split(' '))
# result = map(round, numbers)
# print(list(result))

# numbers = map(int, input().split(' '))
# result = filter(lambda x: x % 2 == 0, numbers)
# print(list(result))

# numbers = map(int, input().split(' '))
# result = sorted(numbers)
# print(result)

numbers = list(map(int, input().split(' ')))
min_number = min(numbers)
max_number = max(numbers)
numbers_sum = sum(numbers)

print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {numbers_sum}')
