"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds
 
SOLUTION

This is a simple problem all. There are two cases the one where 
we skip a step else we just jump one after the other.

So for something like 00010 we can skip once in the first 3 zero's
and then one jump that means it will take only 2 jumps clear the stage.
"""
import math
import os
import random
import re
import sys


def jumpingOnClouds(c):
    # "i" is the variable which keeps the track of the
    # index or we can say the cloud that we are on
    i = jumps = 0
    length = len(c)

    # we go 1 less then the length cause the way
    # indexs are given to the arrays.
    while i < length - 1:
        # check if adding 2 to the current index would
        # go out of the array length or not. If we just
        # put the second condition then it will be give error
        # while checking last 2 values of array.
        if i + 2 < length and c[i + 2] == 0:
            i += 1

        jumps += 1
        i += 1

    return jumps


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + "\n")
    fptr.close()
