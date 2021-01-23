#!/bin/python3

import math
import os
import random
import re
import sys

def retsumhourglass(arr):
    first = sum(arr[0])
    last = sum(arr[-1])
    middle  = arr[1][1]
    return first + last + middle  
      

def hourglassSum(arr):
    total = []
    n = len(arr)
   
    for i in range(n-2):
        for j in range(n-2):
            submatrix = [[arr[m][k] for k in range(i,i+3)] for m in range(j,j+3)]
            total.append(retsumhourglass(submatrix))
           
    
    return max(total)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
