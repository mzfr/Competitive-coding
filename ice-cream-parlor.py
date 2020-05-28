"""
https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

SOLUTION:

It's an easy problem, take an empty dicitonaryjust loop over 
the given costs and if that cost is not in the dict add it 
after subtracting from the money we have, that would be the key
and the value would be the index of that element.

"""
#!/bin/python3

import math
import os
import random
import re
import sys


def whatFlavors(cost, money):
    remains = dict()
    for index, c in enumerate(cost):
        if c not in remains:
            remains[money - c] = index + 1
        else:
            print(remains[c], index + 1)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
