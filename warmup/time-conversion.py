#!/bin/python3

import os
import sys
from time import strftime, strptime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    t = strptime(s, '%I:%M:%S%p')
    return strftime('%H:%M:%S', t)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

