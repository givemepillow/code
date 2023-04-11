result = None
title = []
for _ in range(2):
    title.clear()
    n = int(input())

    s = input().split()
    a = list(map(int, input().split()))

    for s_i, a_i in zip(s, a):
        title.extend([s_i] * a_i)

    if result is None:
        result = int(''.join(title), 2)
    else:
        result ^= int(''.join(title), 2)

print(sum(i for i, v in enumerate(bin(result), start=1 + (len(title) - len(bin(result)))) if v == '1'))
