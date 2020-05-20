"""
https://www.hackerrank.com/challenges/ctci-array-left-rotation/

SOLUTION:

This is very easy problem, all we need to do is
remove the last element first and then add that
the first position.

First I was slicing inside a loop which increased
the complexity.

Another way would be to use for loop but then in
that case instead of using slice use pop.

for i in range(d):
    first = a[0]
    a.pop(0)
    a.append(first)

@ashish-012 did it this way.
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def rotLeft(a, d):
    return a[d:] + a[:d]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
