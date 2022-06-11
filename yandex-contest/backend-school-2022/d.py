N, M = map(int, input().split())
floor = {}
s_i, s_j = 0, 0
for i in range(1, N + 1):
    line = input()
    floor[i] = {}
    for j in range(1, M + 1):
        floor[i][j] = line[j - 1]
        if floor[i][j] == 'S':
            s_i, s_j = i, j

stack = [(s_i, s_j)]
while stack:
    i, j = stack.pop()
    if i + 1 <= N and floor[i + 1][j] == '.':
        floor[i + 1][j] = 'D'
        stack.append((i + 1, j))
    if i - 1 > 0 and floor[i - 1][j] == '.':
        floor[i - 1][j] = 'U'
        stack.append((i - 1, j))
    if j + 1 <= M and floor[i][j + 1] == '.':
        floor[i][j + 1] = 'R'
        stack.append((i, j + 1))
    if j - 1 > 0 and floor[i][j - 1] == '.':
        floor[i][j - 1] = 'L'
        stack.append((i, j - 1))

for row in floor.values():
    print(*row.values(), sep='')
