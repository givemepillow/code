# d + (a + (b + c) = (a + b) + c + d -- 5
# a + b = b + a -- -1
# (a((b + c) = ab + bc -- -1


# Почти правильная последовательность скобок - т.е. достаточно
# убрать одну скобку и последовательность стане валидной.


f = open('input.txt', 'r')
s = f.read()
f.close()


def check():
    all_open = 0
    all_close = 0
    close_index = -1
    open_index = -1
    open_number = 0
    for i in range(len(s)):
        if s[i] not in '()':
            i -= 1
            continue
        if s[i] == ')':
            all_close += 1
            if not open_number:
                if close_index == -1:
                    close_index = i
                else:
                    return -1
            else:
                open_number -= 1
                if not open_number:
                    open_index = -1
        else:
            all_open += 1
            open_number += 1
            if open_index == -1:
                open_index = i
        if all_close - all_open > 1:
            return -1
    if all_open - all_close > 1:
        return -1
    if (close_index == -1 and open_index == -1) or (close_index != -1 and open_index != -1):
        return -1
    if close_index != -1:
        index = close_index
        current = index - 1
        while current != -1:
            if s[current] == '(':
                break
            elif s[current] == ')':
                index = current
            current -= 1
        return index + 1
    elif open_index != -1:
        index = open_index
        current = index - 1
        while current != -1:
            if s[current] == ')':
                break
            elif s[current] == '(':
                index = current
            current -= 1
        return index + 1
    else:
        return -1


print(check())
