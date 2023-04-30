a, b = map(int, input().split())
if b % a != 0:
    print(0)
else:
    n = b // a
    c = 0
    d = 2
    while d * d <= n:
        if n % d == 0:
            while n % d == 0:
                n //= d
            c += 1
        d += 1
    if n > 1:
        c += 1
    print(2 ** c)
