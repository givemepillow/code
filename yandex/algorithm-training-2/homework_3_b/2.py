numbers = list(map(int, input().split()))
old = set()
answer = ""
for num in numbers:
    if num in old:
        answer += "YES\n"
    else:
        answer += "NO\n"
        old.add(num)
print(answer)
