string = input()

length = len(string)
count = 0
if length != 1:
    index = length // 2
    left = string[0:index]
    right = string[index + (length % 2):length][::-1]
    for s1, s2 in zip(left, right):
        if s1 != s2:
            count += 1

print(count)
