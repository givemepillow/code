result = dict()
with open("input.txt", "r") as f:
    for read in f.readlines():
        data = read.split()
        d, a = data[0], int(data[1])
        if d in result.keys():
            result[d] += a
        else:
            result[d] = a

for d in sorted(result.keys()):
    print(d, result[d])
