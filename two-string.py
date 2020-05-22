"""
https://www.hackerrank.com/challenges/two-strings/ 

SOLUTION:

It very simple we basically use counter to separate
the strings and then find the intersection between them.
If there was some value after intersection we return YES
otherwise NO
"""
import math
import os
import random
import re
import sys
from collections import Counter


def twoStrings(s1, s2):
    if Counter(s1) & Counter(s2):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + "\n")

    fptr.close()
