def is_valid_expression(expression):
    cnt = 0

    for ch in expression:
        if ch == '(':
            cnt += 1
        elif ch == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0


print(is_valid_expression('(2 + 3) - (5 + (4))'))
print(is_valid_expression('(2 + 3)) - (5 + (4))'))
print(is_valid_expression('(2 + 3 - (5 + (4))'))
print(is_valid_expression('(()())'))
print(is_valid_expression(')(()())('))
