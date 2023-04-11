def A(shelf_1: list, shelf_2: list):
    shelf_big = []
    i, j = 0, 0
    while i < len(shelf_1) or j < len(shelf_2):
        if i < len(shelf_1) and j < len(shelf_2):
            if shelf_1[i] <= shelf_2[j]:
                shelf_big.append(shelf_1[i])
                i += 1
            else:
                shelf_big.append(shelf_2[j])
                j += 1
        elif i < len(shelf_1):
            shelf_big.append(shelf_1[i])
            i += 1
        else:
            shelf_big.append(shelf_2[j])
            j += 1
    return shelf_big


print(*A(
    shelf_1=list(map(int, input().split())),
    shelf_2=list(map(int, input().split()))
), sep=' ')

assert A([0, 0, 0], [0, 0, 0]) == [0, 0, 0, 0, 0, 0]
assert A([7, 8, 9], [1, 2, 3]) == [1, 2, 3, 7, 8, 9]
assert A([], []) == []
assert A([1], [1]) == [1, 1]
assert A([2], [1]) == [1, 2]
