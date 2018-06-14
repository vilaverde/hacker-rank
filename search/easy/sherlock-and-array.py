#!/bin/python3

import sys

def solve(a):
    l = 0
    r = len(a) - 1
    left  = a[l]
    right = a[r]

    while l < r:
        if right > left:
            l += 1
            left  = left + a[l]
        elif left > right:
            r -= 1
            right = right + a[r]
        else:
            l += 1
            left  = left + a[l]
            r -= 1
            right = right + a[r]

    if left == right:
        return 'YES'
    else:
        return 'NO'

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
