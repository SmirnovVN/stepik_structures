def check(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    c = 0
    for i in s:
        c += 1
        if i in brackets.values():
            stack.append((i, c))
        elif i in brackets:
            if stack and stack[-1][0] == brackets[i]:
                del stack[-1]
            else:
                return c

    if not stack:
        return 'Success'
    else:
        return stack[-1][1]


# s = input()
# print(check(s))
assert check("[]") == 'Success'
assert check("{[]}()") == 'Success'
assert check("{") == 1
assert check("{[}") == 3
assert check("foo(bar);") == 'Success'
assert check("foo(bar[i);") == 10
assert check("]]]") == 1
assert check("( [ ]") == 1
assert check("(((((((((())))") == 6
