#!/bin/python3

import math
import os
import random
import re
import sys

T = int(input())

for i in range(T):
    s = str(input())
    even = ''
    odd  = ''

    for i, c  in enumerate(s):
        if i % 2 == 0:
          even += c
        else:
          odd += c

    print(even + ' ' + odd)
