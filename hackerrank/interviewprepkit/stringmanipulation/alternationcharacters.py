#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    
    news = ''.join(i for i, _ in itertools.groupby(s))
    
    return len(s)-len(news)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
