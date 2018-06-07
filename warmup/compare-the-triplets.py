#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(a, b):
    a_points = 0
    b_points = 0

    a_points += (a[0] > b[0]) + (a[1] > b[1]) + (a[2] > b[2])
    b_points += (b[0] > a[0]) + (b[1] > a[1]) + (b[2] > a[2])

    return a_points, b_points


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = solve(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
