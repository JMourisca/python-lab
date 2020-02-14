import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 * i for i in range(n+1)]
    for q in queries:
        idx1 = q[0]
        idx2 = q[1] 
        k = q[2]
        arr[idx1] += k
        if idx2 + 1 < len(arr):
            arr[idx2 + 1] -= k

    maxRes = 0
    count = 0
    for res in arr:
        count += res
        if count > maxRes:
            maxRes = count
            
    return maxRes

if __name__ == '__main__':

    queries = []

    # for data.txt: 2497169732
    with open("105-data.txt", 'r') as f:
        idx = 0
        for line in f:
            ln = list(map(int, line.rstrip().split()))
            if idx == 0:
                n = ln[0]
                m = ln[1]
            else:
                queries.append(ln)
            idx += 1
    
    result = arrayManipulation(n, queries)
    print(str(result))
