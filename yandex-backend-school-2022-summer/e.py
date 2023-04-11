def balance(skip: int) -> bool:
    file = open('input.txt', 'r')
    parenthesis_balance = 0
    i = -1
    while True:
        c = file.read(1)
        if not c:
            break
        i += 1
        if i == skip:
            continue
        if c == '{':
            parenthesis_balance += 1
        elif c == '}':
            if parenthesis_balance == 0:
                return False
            parenthesis_balance -= 1
    return not bool(parenthesis_balance)


def incorrect_parenthesis_index() -> int:
    first_close = -1
    last_open = -1
    file = open('input.txt', 'r')
    parenthesis_balance = 0
    i = -1
    while True:
        c = file.read(1)
        if not c:
            break
        i += 1
        if c == '(':
            if parenthesis_balance == 0:
                last_open = i
            parenthesis_balance += 1
        elif c == ')':
            if first_close == -1:
                first_close = i
            parenthesis_balance -= 1
    if parenthesis_balance == 1 and balance(last_open):
        return last_open + 1
    if parenthesis_balance == -1 and balance(first_close):
        return first_close + 1
    return -1


print(incorrect_parenthesis_index())
