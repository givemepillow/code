n = int(input())
length = 0
max_length = 0
while n:
    n -= 1
    number = int(input())
    if number:
        length += 1
    else:
        max_length = length if max_length < length else max_length
        length = 0
print(length if max_length < length else max_length)
