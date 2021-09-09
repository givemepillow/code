n = int(input())

answer = ""
yes = set([i for i in range(1, n + 1)])
no = set()
while True:
    read = input()
    if read == "HELP":
        break
    numbers = set(map(int, read.split()))
    answer = input()
    if answer == "NO":
        no |= numbers
    elif answer == "YES":
        yes.intersection_update(numbers)

yes -= no
print(*sorted(yes))