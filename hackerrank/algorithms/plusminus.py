#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = len(list(filter(lambda x: x > 0, arr)))
    neg = len(list(filter(lambda x: x < 0, arr)))
    zeros = len(list(filter(lambda x: x == 0, arr)))
    return list(map(lambda x: format(x/len(arr), '.6f'), [pos, neg, zeros])) 
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(*plusMinus(arr), sep = '\n' )
    
