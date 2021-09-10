from functools import cmp_to_key

result = dict()
with open("input.txt", "r") as f:
    for read in f.readlines():
        words = read.split()
        for word in words:
            if word in result.keys():
                result[word] += 1
            else:
                result[word] = 1


def compare(t1, t2):
    if t1[0] == t2[0]:
        if t1[1] > t2[1]:
            return -1
        else:
            return 1
    else:
        if t1[0] > t2[0]:
            return 1
        else:
            return -1


word_rate = [w for w in sorted([(result[word], word) for word in result.keys()], reverse=True, key=cmp_to_key(compare))]
print(*[t[1] for t in word_rate], sep='\n')
