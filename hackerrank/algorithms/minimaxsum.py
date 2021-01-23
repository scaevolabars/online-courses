#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the miniMaxSum function below.

# ALTERNATIVE SOLUTION
# nums = [int(x) for x in input().strip().split(' ')]
# print(sum(nums) - max(nums), sum(nums) - min(nums))
#

def miniMaxSum(arr, r = 4):
    l = list(map(sum,itertools.combinations(arr, r)))
    return [min(l), max(l)]

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    print(*miniMaxSum(arr))
