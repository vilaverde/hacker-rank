#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, n, arr):
    for s in range(n):
        for j in range(s+1, n):
            if arr[s] + arr[j] == m:
                return s+1, j+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, n, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()

