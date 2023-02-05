n, m = map(int, input().split())
procs = [[v, 0] for v in map(int, input().split())]
procs.sort(key=lambda i: i[0])
current_time, energy = 0, 0
min_end_time = 0
for _ in range(m):
    t_moment, t_work = map(int, input().split())
    current_time = t_moment
    if min_end_time > current_time:
        continue
    for item in procs:
        if item[1] <= current_time:
            end_time = current_time + t_work
            item[1] = end_time
            _, min_end_time = min(procs, key=lambda i: i[1])
            energy += t_work * item[0]
            break

print(energy)
