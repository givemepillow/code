n, m = map(int, input().split())


def next_position():
    while True:
        middle = m // 2 + (m % 2)
        count = m
        left, right = middle, middle
        if m % 2 == 1:
            left_diff, right_diff = -1, 1
        else:
            left_diff, right_diff = 1, -1
        yield middle
        while count > 1:
            left += left_diff
            yield left
            count -= 1
            if count == 1:
                break
            right += right_diff
            yield right
            count -= 1


pos = next_position()

for _ in range(n):
    print(next(pos))
