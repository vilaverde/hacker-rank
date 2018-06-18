#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = -63
    for i in range(4):
        for j in range(4):
            t = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            m = arr[i+1][j+1]
            b = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if t + m + b > max_sum:
                max_sum = t + m + b

    print(max_sum)
