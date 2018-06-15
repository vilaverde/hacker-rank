#!/bin/python3

T  = int(input())
pb = {}

for i in range(T):
    k, v = str(input()).split()
    pb[k] = v

q = str(input())
while q:
    if q in pb:
        print('%s=%s' % (q, pb[q]))
    else:
        print('Not found')

    q = str(input())
