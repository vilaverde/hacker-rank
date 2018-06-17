#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    b = ""
    while n > 0:
        b = str(n % 2) + b
        n = int(n / 2)

    max_c1 = 0
    counter = 0
    for d in b:
        if d == "1":
            counter = counter + 1
            if counter >= max_c1:
                max_c1 = counter
        else:
            counter = 0

    print(max_c1)

