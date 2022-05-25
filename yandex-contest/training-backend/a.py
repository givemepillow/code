# https://contest.yandex.ru/contest/28412/


def a(n, volumes):
    if n == 1:
        return 0
    for v1, v2 in zip(volumes[:-1], volumes[1:]):
        if v1 > v2:
            return -1
    return max(volumes) - min(volumes)


print(a(int(input()), list(map(int, input().split()))))

# tests
assert a(2, [1, 1]) == 0
assert a(5, [1, 1, 1, 1, 5]) == 4
assert a(1, [1]) == 0
