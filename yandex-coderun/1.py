n = int(input())
array = [int(i) for i in input().split()]
array.sort()
distance = [0] * n
distance[1] = array[1] - array[0]
if n > 2:
    distance[2] = array[2] - array[0]
    for i in range(3, n):
        distance[i] = min(distance[i - 2], distance[i - 1]) + array[i] - array[i - 1]
print(distance[n - 1])
