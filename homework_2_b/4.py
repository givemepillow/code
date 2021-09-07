L, K = map(int, input().split())

legs = tuple(map(int, input().split()))

left_mid = L // 2 + (L % 2) - 1
right_mid = L // 2

left_leg, right_leg = 0, 0

for l in range(left_mid, 0, -1):
    if l in legs:
        left_leg = l
        break


for r in range(right_mid, L):
    if r in legs:
        right_leg = r
        break

print(left_leg, right_leg) if right_leg != left_leg else print(left_leg)
