def compare(s1, s2):
    if len(s1) != len(s2):
        return 0
    else:
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                return 0
    return 1


print(compare(sorted(input()), sorted(input())))
