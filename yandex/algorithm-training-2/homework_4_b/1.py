n = int(input())

result = dict()
for i in range(n):
    d, a = map(int, input().split())
    if d in result.keys():
        result[d] += a
    else:
        result[d] = a

for d in sorted(result.keys()):
    print(d, result[d])
