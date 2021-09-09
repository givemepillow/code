numbers = list(map(int, input().split()))
d = dict()
for n in numbers: d[n] = 0
for n in numbers: d[n] += 1
result = ""
for n in d:
    if d[n] == 1: result += f"{n} "
print(result)
