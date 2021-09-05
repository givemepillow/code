def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return True if (year % 400) == 0 else False
        else:
            return True
    else:
        return False


def may_be_correct(day, month, year):
    the_31_days = (1, 3, 5, 7, 8, 10, 12)

    if day > 28 and month < 13:
        if month in the_31_days:
            return True
        elif day > 29 and month != 2:
            return True
        elif day == 29 and month == 2:
            return True if is_leap_year(year) else False
        else:
            return False
    elif month < 13:
        return True
    else:
        return False


x, y, z = map(int, input().split())

first = may_be_correct(x, y, z)
second = may_be_correct(y, x, z)

print(1 if ((first or second) and first is not second) or y == x else 0)
