n, i, j = map(int, input().split())

# Кол-во станций до последней и до первой.
i_forward = n - i
i_back = i - 1

j_forward = n - j
j_back = j - 1

first_way = (i_forward + j_back) % n
second_way = (i_back + j_forward) % n

print(first_way if first_way < second_way else second_way)




#stations = [s for s in range(1, n + 1)]


