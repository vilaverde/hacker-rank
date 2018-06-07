#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(a):
    diag_a = 0
    diag_b = 0
    m_size = len(a)

    for i in range(m_size):
        diag_a = diag_a + a[i][i]
        diag_b = diag_b + a[i][m_size - (i + 1)]

    return abs(diag_a - diag_b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    fptr.write(str(result) + '\n')

    fptr.close()

