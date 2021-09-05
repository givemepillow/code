d = int(input())
x1, x2 = map(int, input().split())


def nearest(): print(2) if (d / 2) < x1 else print(3) if (d / 2) < x2 else print(1)


print(0) if 0 <= x1 <= d and d - x1 >= x2 >= 0 else nearest()
