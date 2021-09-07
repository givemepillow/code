n = int(input())
print(sum(list(reversed(sorted(map(int, input().split()))))[1:]))