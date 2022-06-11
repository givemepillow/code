S = input()
Q = input()

rate = {}
answers = {}
for i in range(len(S)):
    if S[i] not in rate:
        rate[S[i]] = 0
    if S[i] == Q[i]:
        answers[i] = 'correct'
    else:
        rate[S[i]] += 1
        answers[i] = ''

for i in range(len(Q)):
    if answers[i]:
        continue
    else:
        if Q[i] in rate and rate[Q[i]]:
            answers[i] = 'present'
            rate[Q[i]] -= 1
        else:
            answers[i] = 'absent'

for j in range(len(S)):
    print(answers[j])
