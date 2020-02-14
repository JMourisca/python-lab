#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.
def matchingStrings(strings, queries):
    countStrings = dict.fromkeys(strings, 0)    
    for string in strings:
        countStrings[string] += 1
    
    res = []
    for q in queries:         
        if q in countStrings.keys():
            res.append(countStrings[q])
        else:
            res.append(0)
    return res



if __name__ == '__main__':
    fptr = open("104-result.txt", 'w')

    strings_count = 3

    strings = ['def','de','fgh']

    queries_count = 3

    queries = ['de','lmn','fgh']

    res = matchingStrings(strings, queries)

    print('\n'.join(map(str, res)))

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
