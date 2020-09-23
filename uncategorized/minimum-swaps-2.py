"""
https://www.hackerrank.com/challenges/minimum-swaps-2

SOLUTION:

The logic behind this is that once the list is sorted we will get
1 on index 0, 2 on index 1 and so on.

Now what we do is if the element is 4 then we move it to that index i.e
4 has to be on index 3 so we just swap that with that index.
We do it until the time currect element is on correct index, so if the 
a[i] == i+1 i.e 1 == index 1 that time we increase the value of i.

For better understanding see this image: https://i.imgur.com/l00K4BK.jpg
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    count = 0
    i = 0
    while(i < len(arr)-1):
        if arr[i] != i+1:
            j = arr[i]
            arr[i], arr[j-1] = arr[j-1], arr[i]
            count += 1
        else:
            i += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
