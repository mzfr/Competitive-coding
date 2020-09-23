"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string

SOLUTION:
First we use Counter to get frequencies of all the characters,
then we put them in a list and find the max and min value of that
list.

Then we apply conditions:

1) if max == min i.e if all the values are same then return YES
2) if max - min ==  1 i.e if the difference between min max is 1
3) max count is 1 and min count is not 1 i.e if list was [3,2,2,2]
then we would see the condition becomes true since 3 is max and have 
appearance only once and 2 have multiple appearance.
4) Vice versa of 3rd condition.

"""
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def isValid(s):
    freq = Counter(s)
    vals = list(freq.values())
    _max = max(vals) 
    _min = min(vals)
    if _max == _min or _max-_min == 1 and (vals.count(_max) == 1 and vals.count(_min) != 1) or (_min == 1 and vals.count(_min) == 1 and vals.count(_max) != 1): 
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
