#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for i in range(1, n+1):
        fptr.write(("%" + str(n) + "s\n") % (i*'#'))

    fptr.close()

if __name__ == '__main__':
    n = int(input())

    result = staircase(n)
