"""https://www.hackerrank.com/challenges/pairs/

SOLUTION:
My first thought was just to add and then check
if that value is present in the arr like:

    for i in arr:
        if i+k in arr:
            count += 1

but this is O(n^2) since searching also takes time.

So to improve that we first made a Counters dictionary
which will contain the value as well as their number of occurence
but as given in question the occurence will be alway 1, so now
searching from dict won't be any issue it will give as the 
complexity of O(N)
"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def pairs(k, arr):
    _dict = Counter(arr)
    count = 0

    for i in arr:
        count += _dict[i+k]
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
