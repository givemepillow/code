"""
У HR Маши на столе лежат две стопки резюме, размерами n и m, в каждом из резюме указана зарплата,
числа a[0..n-1] для одной стопки, и b[0..m-1] для второй. Нулевой индекс указывает на верхнее резюме в стопке.


Маша устанавливает значение s максимальной суммы зарплат и предлагает очень активному стажеру Саше сыграть в игру:

- За каждый ход Саша может взять одно верхнее резюме из любой стопки и забрать себе в работу
- Саша считает сумму всех зарплат из резюме, которые он взял. Он может брать новые резюме из стопок только
таким образом, чтобы эта сумма не превышала s
- Игра заканчивается, если Саша больше не может брать резюме

Нужно выяснить, какое максимальное количество резюме Саша мог бы забрать себе в работу, если бы тоже знал зарплаты,
указанные в каждом резюме.

Входные данные (поступают в стандартный поток ввода)
Первая строка – целые числа n, m и s через пробел (1≤n≤10 000, 1≤m≤10 000, 1≤s≤200 000 000)

Далее идут строки с зарплатами резюме в стопках. Всего строк столько, сколько резюме в большей из стопок, на каждой строке один из вариантов:

- два целых числа a и b через пробел (1≤a≤10 000, 1≤b≤10 000),
- a и символ - (если во второй стопке больше нет резюме) через пробел (1≤a≤10 000)
- символ - (если в первой стопке больше нет резюме) и b через пробел (1≤b≤10 000)
Все входные данные наших тестов всегда соблюдают указанные параметры, дополнительные проверки не требуются


Выходные данные (ожидаются в стандартном потоке вывода)
Одно целое число, максимальное количество резюме
"""
n, m, s = tuple(map(int, input().split()))
n_array, m_array = [], []
n_sum, n_count = 0, 0
m_sum, m_count = 0, 0
while n or m:
    n_num, m_num = input().split()
    if n:
        n_num = int(n_num)
        if n_num + n_sum <= s:
            n_array.append(n_num)
            n_sum += n_num
            n_count += 1
            n -= 1
        else:
            n = 0
    if m:
        m_num = int(m_num)
        if m_sum + m_num <= s:
            m_array.append(m_num)
            m_sum += m_num
            m_count += 1
            m -= 1
        else:
            m = 0


def count_and_sum(array):
    current_sum = 0
    current_count = 0
    for v in array:
        if current_sum + v <= s:
            current_sum += v
            current_count += 1
        else:
            return current_count, current_sum, array[:current_count]
    return current_count, current_sum, array[:current_count]


def next_value(gen):
    try:
        value = next(gen)
    except StopIteration:
        return -1
    return value


def max_count(a_count, a_sum, a_list, b_list):
    a_gen = reversed(a_list)
    b_gen = iter(b_list)
    available_s = s - a_sum
    current_count = a_count
    a_value = next_value(a_gen)
    b_value = next_value(b_gen)
    iters = 0
    while True:
        iters += 1
        if b_value != -1 and available_s - b_value >= 0:
            available_s -= b_value
            current_count += 1
            b_value = next_value(b_gen)
        elif b_value != -1 and a_value != -1 and available_s - b_value + a_value >= 0:
            available_s = available_s - b_value + a_value
            a_value = next_value(a_gen)
            b_value = next_value(b_gen)
        else:
            break
    return current_count


m_count, m_sum, m_array = count_and_sum(m_array)
n_count, n_sum, n_array = count_and_sum(n_array)

print(max(max_count(n_count, n_sum, n_array, m_array), max_count(m_count, m_sum, m_array, n_array)))
