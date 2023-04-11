def generate(n):
    if n == 0:
        return ['']
    result = []
    for i in range(n):
        for left in generate(i):
            for right in generate(n - 1 - i):
                result.append(f'({left}){right}')
    return result


for line in sorted(generate(int(input()))):
    print(line)
