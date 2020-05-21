"""
https://www.hackerrank.com/challenges/ctci-ransom-note

SOLUTION:

First I tried to solve this without any external library

for i in note:
    if i in magazine and note.count(i) <= magazine.count(i) :
        answer = "Yes"        
    else:
        answer = "No"
        break
    
    print(answer)

This is what it looked like but then some test cases were 
failing due to time. I think that is because "i in magazine"
would use some kind of loop and so will the count function
which increases the processing.

If you want to understand the logic then you can look at the
code above, Counter() function does the similar kind of things
but at once.
"""
import math
import os
import random
import re
import sys
from collections import Counter


def checkMagazine(magazine, note):
    if Counter(note) - Counter(magazine):
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
