"""
https://www.hackerrank.com/contests/codex-2-0-1/challenges/find-that-odd/problem

This method have a time complexity of O(n) but takes extra space to store the newly created
mapping.
"""

array = input().split()
hmap = {}

for i in array:
    if i not in hmap:
        hmap[i] = 1
    else:
        hmap[i] += 1

for k,v in hmap.items():
    if v%2 != 0:
        print(k)
