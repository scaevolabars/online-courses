#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def primaryDiagonal(arr):
    s = []
    for i, l in enumerate(arr):
        s.append(l[i])
    return s  

    

def secondaryDiagonal(arr):
    s = []
    for i, l in enumerate(arr):
        s.append(l[len(l) - i - 1])
    return s 

def diagonalDifference(arr):
    return abs(sum(primaryDiagonal(arr)) - sum(secondaryDiagonal(arr)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
