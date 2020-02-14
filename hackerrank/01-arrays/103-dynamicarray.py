#!/bin/python3

def query1(sl, la, x, y):
    n = len(sl)
    i1 = (x ^ la) % n
    seq = sl[i1]
    seq.append(y)
    return la


def query2(sl, la, x, y):
    n = len(sl)
    i2 = (x ^ la) % n
    seq = sl[i2]
    size = len(seq)
    i2 = y % size
    val = seq[i2]
    return val


def dynamicArray(n, queries):
    lastAnswer = 0
    seqList = [[] * n for i in range(n)] 
    result = []
    for q in queries:
        if q[0] == 1:
            lastAnswer = query1(seqList, lastAnswer, q[1], q[2])
        else:
            lastAnswer = query2(seqList, lastAnswer, q[1], q[2])
            result.append(lastAnswer)
    return result


queries = []
with open("103-data.txt", 'r') as f:
    idx = 0
    for line in f:
        if idx == 0:
            first_multiple_input = line.rstrip().split()
        else:
            queries.append(list(map(int, line.rstrip().split())))
        idx += 1

n = int(first_multiple_input[0])
q = int(first_multiple_input[1])

result = dynamicArray(n, queries)

print('Expected:', 855677723, 'Got:')
print('\n'.join(map(str, result)))