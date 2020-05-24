"""
https://www.hackerrank.com/challenges/alternating-characters/

SOLUTION:
Simple solution, just plus the count if the character 
at i and i+1 matches. No need to remove the character
since we are just going it over once.

"""
import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
