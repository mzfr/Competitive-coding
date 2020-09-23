"""
https://www.hackerrank.com/challenges/mark-and-toys/

SOLUTION:
Really nothing to explain in this, just simple
sort the prices and keeps of subtracting from the 
k value and keep on counting the time we subtracted.

"""
import math
import os
import random
import re
import sys


def maximumToys(prices, k):
    toys = 0
    prices.sort()
    for i in prices:
        if k-i > 0:
            k = k-i
            toys += 1
    return toys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
