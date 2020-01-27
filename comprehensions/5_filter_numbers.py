def is_valid(number):
    min_number = 2
    max_number = 10
    results = [x for x in range(min_number, max_number + 1) if number % x == 0]
    return True if results else False


n = int(input())
m = int(input())

result = [x for x in range(n, m + 1) if is_valid(x)]
print(result)