# https://coderun.yandex.ru/seasons/first_2023/tracks/backend/problem/Kolya%20and%20data%20centers?compiler=python
# Коля и датацентры
import heapq


class MinMaxHeap:

    def __init__(self, n: int):
        self.min_heap = [(0, dc) for dc in range(n)]
        self.max_heap = [(0, dc) for dc in range(n)]

    def push(self, DC_I: int, RxA: int):
        heapq.heappush(self.min_heap, (RxA, DC_I))
        heapq.heappush(self.max_heap, (-RxA, DC_I))

    def pop_min(self):
        heapq.heappop(self.min_heap)

    def pop_max(self):
        heapq.heappop(self.max_heap)

    @property
    def min(self):
        return self.min_heap[0]

    @property
    def max(self):
        return self.max_heap[0]


N, M, Q = map(int, input().split())

datacenters_A = [set() for k in range(N)]
datacenters_R = [0 for _ in range(N)]
datacenters_RxA = [0 for _ in range(N)]
heap = MinMaxHeap(N)
results = []
for _ in range(Q):
    match input().split():
        case ['RESET', i] if (i := int(i) - 1) >= 0:
            datacenters_A[i].clear()  # Сброс выключенных серверов
            datacenters_R[i] += 1  # Увеличиваем кол-во перезагрузок ДЦ.
            datacenters_RxA[i] = datacenters_R[i] * M  # Обновляем параметр.
            heap.push(i, datacenters_RxA[i])
        case ['DISABLE', i, j] if (i := int(i) - 1) >= 0 and (j := int(j) - 1) >= 0:
            datacenters_A[i].add(j)  # Новый выключенный.
            datacenters_RxA[i] = datacenters_R[i] * (M - len(datacenters_A[i]))  # Обновляем параметр.
            heap.push(i, datacenters_RxA[i])
        case ['GETMAX']:
            while datacenters_RxA[heap.max[1]] != -heap.max[0]:
                heap.pop_max()
            results.append(heap.max[1] + 1)
        case ['GETMIN']:
            while datacenters_RxA[heap.min[1]] != heap.min[0]:
                heap.pop_min()
            results.append(heap.min[1] + 1)

print(*results, sep='\n')
