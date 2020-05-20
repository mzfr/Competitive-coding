"""
https://www.hackerrank.com/challenges/2d-array/

SOLUTION:
since the dimension is fixed so we can run the loop till 4
that is because to form an hour glass we will need 3 array.

one way to do this is to just get one value at a time by doing 
something like:

arr[i][j]+arr[i][j+1] ......

but we can get the values directly by using the slicing.

"""
import math
import os
import random
import re
import sys


def hourglassSum(arr):
    _list = []
    for i in range(4):
        for j in range(4):
            # get the top and base values of hour glas
            top_base_sum = sum(arr[i][j : j + 3] + arr[i + 2][j : j + 3])
            # Single value that will be in mid of hourglass
            total_sum = top_base_sum + arr[i + 1][j + 1]
            _list.append(total_sum)

    return max(_list)

if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
