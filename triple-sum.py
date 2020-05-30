"""
https://www.hackerrank.com/challenges/triple-sum/

SOLUTION:

we sort all the array first so the smallest values
is in the starting and we will have to loop less.

Then we run those while loops. They are started with 
the b because in most cases that is the one which have 
less element and so we won't run into index error.

We are multiplying in the end because its possible to have
multiple triplet having similar ending.

if array were
a = 3,57
b = 3,6
c = 4,6,9

output:
3,6,4
3,6,6
5,6,4
5,6,6

we see 2 have ending with 6,4 and 2 have ending with 6,6
"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    i = j = k = 0
    ans = 0

    while j< len(b):
        while i < len(a) and a[i] <= b[j]:
            i += 1
        while k < len(c) and b[j] >= c[k]:
            k += 1
        
        ans += i*k
        j += 1
    
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
