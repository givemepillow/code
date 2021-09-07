buildings = list(map(int, input().split()))

market_indexes = [i for i, b in enumerate(buildings) if b == 2]

nearest_ways = []

for i, b in enumerate(buildings):
    if b == 1:
        nearest_ways.append(min([abs(j - i) for j in market_indexes]))

print(max(nearest_ways))
