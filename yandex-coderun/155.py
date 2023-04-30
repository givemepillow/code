# Уникальные элементы
n = int(input())
unique = {}
count = 0
for number in map(int, input().split()):
    unique.setdefault(number, 0)
    unique[number] += 1
    if unique[number] == 1:
        count += 1
    elif unique[number] == 2:
        count -= 1

print(count)
