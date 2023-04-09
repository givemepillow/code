n, m, q = map(int, input().split())

data_centers = {q_i: [[1 for _ in range(m)], 0, 0] for q_i in range(1, n + 1)}

R_x_A = {0: [k for k in range(1, n + 1)]}

for _ in range(q):
    data = input()
    if data.startswith('RESET'):
        i = int(data.split()[1])
        data_centers[i][1] += 1
        for j in range(m):
            data_centers[i][0][j] = 1

        R_x_A[data_centers[i][2]].remove(i)
        if not R_x_A[data_centers[i][2]]:
            del R_x_A[data_centers[i][2]]

        current_R_x_A = data_centers[i][1] * m
        data_centers[i][2] = current_R_x_A

        R_x_A.setdefault(current_R_x_A, []).append(i)
        R_x_A[current_R_x_A].sort()

    elif data.startswith('DISABLE'):
        _, i, j = data.split()
        i, j = int(i), int(j)
        data_centers[i][0][j - 1] = 0

        R_x_A[data_centers[i][2]].remove(i)
        if not R_x_A[data_centers[i][2]]:
            del R_x_A[data_centers[i][2]]

        current_R_x_A = data_centers[i][1] * sum(data_centers[i][0])
        data_centers[i][2] = current_R_x_A

        R_x_A.setdefault(current_R_x_A, []).append(i)
        R_x_A[current_R_x_A].sort()

    elif data.startswith('GETMAX'):
        print(R_x_A[max(R_x_A)][0])
    elif data.startswith('GETMIN'):
        print(R_x_A[min(R_x_A)][0])
