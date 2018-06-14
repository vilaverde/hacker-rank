#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, n, k):
    sx = sorted(x)
    t = 0
    i = 0

    while i < n:
        t = t + 1
        location = sx[i] + k

        while (i < n and sx[i] <= location): i = i + 1
        location = sx[i-1] + k

        while (i < n and sx[i] <= location): i = i + 1

    return t

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x,n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

