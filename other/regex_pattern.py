def match(s: str, p: str) -> bool:
    if len(p) == 0:
        return True if len(s) == 0 else False
    elif len(s) == 0:
        return False if p[0] != '*' else True
    elif p[0] == '*' and len(p.replace('**', '*')) == 1:
        return True
    elif p[0] == '*':
        p = p[1:]
        s = s[s.find(p[:p.find('*')]):]
        for i in range(len(s)):
            if match(s[i:], p):
                return True
        return False
    elif p[0] == '.' or p[0] == s[0]:
        return match(s[1:], p[1:])
    return False


print(match('123ggio090ggdsfjewjwek90kjdshfjf9091', '...g*0*909.'))
