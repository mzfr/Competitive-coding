"""
https://www.hackerrank.com/challenges/ctci-fibonacci-numbers

SOLUTION:
No explanation needed

"""


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

    # Write your code here.

n = int(input())
print(fibonacci(n))
