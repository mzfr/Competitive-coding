"""
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

SOLUTION:

First I thought of using the itertools.combination to get all the combinations
and then find their minimum difference but that had a high complexity and some
of the test cases were failing so instead of that approach I did the following:

1) Sort the given list
2) assume the minimum difference to be between the first two element
3) Then compare all the other diff with that minimum
"""
import math
import os
import random
import re
import sys

def minimumAbsoluteDifference(arr):
    arr.sort()
    minimum = abs(arr[0]-arr[1])
    for i in range(len(arr)-1):
        diff = abs(arr[i]-arr[i+1])
        if minimum > diff:
            minimum = diff
    return minimum
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
