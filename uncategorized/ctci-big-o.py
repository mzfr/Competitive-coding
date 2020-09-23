"""
https://www.hackerrank.com/challenges/ctci-big-o

SOLUTION:

In first condition we check that n != 1 and also
if n is divisible by 2 that means it's not a prime number.

Then in the loop we start with 3 and since we have checked
with 2 that means no need to go for any other even number 
that is why we jump 2 at a time in a loop.

The maine thing is math.sqrt(n)+1, first that would return float
and once we make it int() it will select the floor value in
the conversion. So it's possible we might miss some cases.
That is why we need to add 1

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the primality function below.
def primality(n):
    if n == 1 or (n%2 == 0 and n != 2):
        return "Not prime"
    else:
        for i in range(3, int(math.sqrt(n)+1), 2):
            if n % i == 0:
                return "Not prime"
                break
        else:
            return "Prime"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
