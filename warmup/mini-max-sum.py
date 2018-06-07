#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total = sum(arr)
    return total - max(arr), total - min(arr)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    result = miniMaxSum(arr)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr.write(' '.join(map(str, result)))
    fptr.close()
