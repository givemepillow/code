n, x = map(int, input().split())

crystals = {}
crystals_sum = 0
i = 0
max_price = 0
for v in map(int, input().split()):
    if crystals_sum > x:
        break
    i += 1
    crystals_sum += v
    crystals[crystals_sum] = i
    max_price = v

while x > crystals_sum:
    i += 1
    crystals_sum += max_price
    crystals[crystals_sum] = i


def count():
    current_crystals = 0
    days = 0
    while current_crystals < x:
        target = x - current_crystals
        while target > 0:
            if target in crystals:
                days += crystals[target]
                current_crystals += target
                break
            target -= 1
        if current_crystals == x:
            return days
        if target <= 0:
            return -1
        days += 1


print(count())
