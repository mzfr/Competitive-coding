"""
https://www.hackerrank.com/challenges/flipping-bits/

SOLUTION:

basically we need to do all those operations
or we can just do XOR. that large number is 2**32
we did 32 cause we need 32 bit long.
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    return n ^ 4294967295

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
