#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    
    alice_s, bob_s = 0, 0
    for i,j in zip(a,b):
        score = i - j
        if score>0: alice_s+=1
        elif score==0: pass
        else: bob_s+=1
        
    return alice_s, bob_s    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
