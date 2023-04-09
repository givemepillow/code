n = int(input())
prev = None
while n:
    n -= 1
    number = int(input())
    if number != prev:
        print(number)
    prev = number
