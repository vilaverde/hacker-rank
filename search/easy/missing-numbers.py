#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    arr_count = [0] * 101
    brr_count = [0] * 101
    offset = min(brr)

    for n in arr:
        arr_count[n - offset] += 1

    for n in brr:
        brr_count[n - offset] += 1

    m_numbers = []
    for i in range(101):
        if arr_count[i] != brr_count[i]:
            m_numbers.append(i + offset)

    return sorted(m_numbers)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

