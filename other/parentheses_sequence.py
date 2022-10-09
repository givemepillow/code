def generate(n: int, string: str = "", opened: int = 0, closed: int = 0):
    if len(string) == 2 * n:
        return print(string)
    if opened < n:
        generate(n, string + '(', opened + 1, closed)
    if closed < opened:
        generate(n, string + ')', opened, closed + 1)


generate(n=3)
