#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    divider = float(len(arr))

    positives = round(sum([1 for p in arr if p > 0]) / divider, 6)
    negatives = round(sum([1 for p in arr if p < 0]) / divider, 6)
    zeros = round(sum([1 for p in arr if p == 0]) / divider, 6)

    return format(positives, '.6f'), format(negatives, '.6f'), format(zeros, '.6f')

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write('\n'.join(map(str, result)))
    fptr.close()
