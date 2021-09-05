def is_leap_year(year):
    return True if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0) else False


def correct(day, month, year):
    the_31_days = (1, 3, 5, 7, 8, 10, 12)
    if month < 13:
        if month in the_31_days:
            return True
        elif day > 29 and month != 2:
            return True
        elif day == 29 and month == 2:
            return True if is_leap_year(year) else False
        else:
            return True
    else:
        return False


x, y, z = map(int, input().split())
print(1 if y == x or correct(x, y, z) is not correct(y, x, z) else 0)
