"""
https://www.hackerrank.com/challenges/repeated-string/problem


SOLUTION:
The idea behind the solution is that first we count the number 
of 'a' in the given string, then we multiple it with the number 
even length that is possible in the given "n" and in the end we 
add the count of "a" that remains(as a remainder).

Ex:
s - aba
n - 10

The string would be "abaabaabaa" now we know that "aba"*3 + "a"
would give this string. So we just did that but in more generalized 
form.

We count the number of "a" in the given "s", then we find how many times
we would have to multiple it to receive a number equal or less then "n"
and then if there is any remaining string we add the count of "a" from
the remainder.
"""
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    length = len(s)
    numOfA = s.count("a") * (n // length) + s[: n % length].count("a")
    return numOfA


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + "\n")
    fptr.close()
