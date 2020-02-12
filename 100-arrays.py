#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the reverseArray function below.
def reverseArray(a):
    i = len(a) - 1
    res = []
    while i >= 0:
        res.append(a[i])
        i -= 1
    return res

if __name__ == '__main__':
    fptr = open("result.txt", 'w')

    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))
 
    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
