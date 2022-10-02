"""
Фермер Василий выбирает землю для покупки. Предмет торгов – прямоугольное поле шириной n и высотой m, которое состоит из участков, где 1 - плодородный участок, а 0 – неплодородный. Василий может либо купить регион поля любого размера, либо отказаться от покупки, если доступных для покупки регионов нет.


Условия покупки следующие:

– Регион – это прямоугольник, ограничивающий соприкасающиеся участки плодородной почвы

– Участки "соприкасаются" если они соседние друг для друга – сверху, снизу, справа, слева и по диагонали

  1 0 1
  0 1 1
  1 0 1
  0 0 0
  0 1 0
На примере выше соприкасаются все участки, кроме нижнего, то есть регионов здесь 2, один площадью 9, другой площадью 1

– Регионы могут пересекаться между собой:

  1 1 1 1 1
  1 0 0 0 1
  1 0 1 0 1
Здесь тоже два региона, один площадью 15 (все поле), другой площадью 1

– Минимальное количество плодородных участков в регионе для покупки – 2

– Покупатель платит только за общую площадь купленного региона


Василий берет кредит на покупку, поэтому хочет потратить деньги как можно оптимальнее – купить тот регион, в котором будет максимальное соотношение плодородной земли к общей площади региона. Если есть несколько регионов с одинаковой «эффективностью», то Василий хочет купить бóльший из них по площади.

Нужно определить площадь региона, который стоит купить фермеру


Входные данные (поступают в стандартный поток ввода)
Первая строка – целые числа n, m через пробел (2≤n≤100, 2≤m≤100)

Далее m строк, в каждой из которых по n цифр 0 или 1, разделенных пробелами

Все входные данные наших тестов всегда соблюдают указанные параметры, дополнительные проверки не требуются


Выходные данные (ожидаются в стандартном потоке вывода)
Одно целое число, площадь наилучшего региона, или 0, в случае отказа от покупки
"""

from array import array

max_x, max_y = map(int, input().split())
matrix = [array('h', (map(int, input().split()))) for _ in range(max_y)]

visited = set()
to_visit = []
ratio, square = 0, 0


def define(coord_y, coord_x):
    left = right = coord_x
    up = bottom = coord_y
    to_visit.clear()
    to_visit.append((coord_y, coord_x))
    while to_visit:
        coords = to_visit.pop()
        if coords in visited:
            continue
        visited.add(coords)
        y, x = coords
        if bottom < y:
            bottom = y
        if up > y:
            up = y
        if right < x:
            right = x
        if left > x:
            left = x

        if y + 1 < max_y and matrix[y + 1][x]:  # go bottom
            to_visit.append((y + 1, x))
        if x + 1 < max_x and matrix[y][x + 1]:  # go right
            to_visit.append((y, x + 1))
        if y - 1 >= 0 and matrix[y - 1][x]:  # go up
            to_visit.append((y - 1, x))
        if x - 1 >= 0 and matrix[y][x - 1]:  # go left
            to_visit.append((y, x - 1))
        if y + 1 < max_y and x + 1 < max_x and matrix[y + 1][x + 1]:  # go bottom & right
            to_visit.append((y + 1, x + 1))
        if y - 1 >= 0 and x - 1 >= 0 and matrix[y - 1][x - 1]:  # go up & left
            to_visit.append((y - 1, x - 1))
        if y + 1 < max_y and x - 1 >= 0 and matrix[y + 1][x - 1]:  # go bottom & left
            to_visit.append((y + 1, x - 1))
        if y - 1 >= 0 and x + 1 < max_x and matrix[y - 1][x + 1]:  # go up & right
            to_visit.append((y - 1, x + 1))
    return up, right, bottom, left


def count_rate(up, right, bottom, left):
    _rt, _sq = 0, 0
    for y in range(up, bottom + 1):
        for x in range(left, right + 1):
            if matrix[y][x]:
                _rt += 1
            _sq += 1
    return _rt / _sq, _sq


for _y in range(max_y):
    for _x in range(max_x):
        if matrix[_y][_x] and (_y, _x) not in visited:
            rt, sq = count_rate(*define(_y, _x))
            if sq > 2:
                if rt > ratio or (rt == ratio and sq > square):
                    ratio, square = rt, sq
print(square)
