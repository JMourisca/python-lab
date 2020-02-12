#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    size = len(arr) - 2
    sum = 0
    for i in range(size):
        print(i)
        # sum += arr[i + 0] + arr[i + 1] + arr[i + 2] + arr[i + 4] + arr[i + 6] + arr[i + 7] + arr[i + 8] 
    
    return sum

if __name__ == '__main__':
    fptr = open("hourglass.txt", 'w')

    arr = []

    # for _ in range(3):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [[0, 4, 3], [0, 1, 0], [8, 6, 6]]

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()