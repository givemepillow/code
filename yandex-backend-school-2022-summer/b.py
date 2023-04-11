n = int(input())
jobs = {}
jobs_candidates = {}
while n:
    n -= 1
    s, m = input().split(',')
    jobs[s] = int(m)
    jobs_candidates[s] = []
k = int(input())
next_stage = []
while k:
    k -= 1
    c, q, r, p = input().split(',')
    jobs_candidates[q].append((c, int(r), int(p)))
for s in jobs:
    next_stage += sorted(jobs_candidates[s], key=lambda x: (x[1], -x[2]), reverse=True)[:jobs[s]]
next_stage.sort(key=lambda x: x[0])
for c, r, p in next_stage:
    print(c)
