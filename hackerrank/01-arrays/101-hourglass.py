#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    rows = len(arr) - 2
    cols = len(arr[0]) - 2
    sum = []
    for i in range(rows):
        for j in range(cols):            
            sum.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i+1][j + 1] + arr[i+2][j + 0] + arr[i+2][j + 1] + arr[i+2][j + 2])
    
    return max(sum)

if __name__ == '__main__':
    fptr = open("hourglass.txt", 'w')

    arr = []

    # arr = [[0, 4, 3], [0, 1, 0], [8, 6, 6]]
    arr = [[1, 1, 1, 0, 0, 0],
           [0, 1, 0, 0, 0, 0],
           [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0],
           [0, 0, 0, 2, 0, 0],
           [0, 0, 1, 2, 4, 0]]

    result = hourglassSum(arr)
    print(str(result))
    fptr.write(str(result) + '\n')

    fptr.close()