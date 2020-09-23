## Spiral printing of a matrix

__URL__: https://www.hackerrank.com/contests/cs1300-odd-2014/challenges/spiral-order
	https://www.hackerrank.com/contests/zoho-pr/challenges/spiral-traversal

## Solution

The solution should work in non-square matrix as well.

Again there are multiple ways, actually ideas are kind of similar but the way of implementation is different.

One solution in python would be:

```python
spiral = lambda a: list(a[0]) + spiral(zip(*a[1:])[::-1]) if a else []
```

The problem with the above solution is that it takes `O(n^3)` since we are traversing the whole array for each iteration.

__Optimal Solution__

The solution present in solution.py follow the idea of having 4 pointers which gives starting row(sr), end row(er), starting column(sc) and end column(ec).

First we go from sc->ec, then sr->er, then we check conditions and repeat the process.
