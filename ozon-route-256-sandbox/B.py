t = int(input())
for _ in range(t):
    data = {}
    input()
    for p in map(int, input().split()):
        if p in data:
            data[p] += 1
        else:
            data[p] = 1
    _sum = 0
    for k, v in data.items():
        _sum += (v - v // 3) * k
    print(_sum)
    data.clear()


