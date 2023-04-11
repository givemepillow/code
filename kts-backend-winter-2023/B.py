def B(string):
    substring = set()
    max_substring_len = 0
    for char in string:
        if char not in substring:
            max_substring_len = max(max_substring_len, len(substring) + 1)
        else:
            substring.remove(char)
        substring.add(char)
    return max_substring_len


print(B(input()))

assert B('') == 0
assert B('abcabc') == 3
assert B('abc') == 3
assert B('aaaaa') == 1
assert B('a') == 1
assert B('abcabcd') == 4
