## Search in a sorted matrix

__URL__:: https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/

## Solution

There are two solutions:

* solution1.py - This contains the code that take `O(nlogn)` time complexity to search. Basically we just perform a binary search on each row(since they are sorted).

__Optimal Solution__

* solution2.py - In this searching technique we use a staircase method. Basically we start from the top right of the matrix and then we do the following:

    - If the X is greater then the element in matrix, then we do a increment in row.
    - If X is smaller then eleement of matrix, then we subtract from column count.

In this method the maximum can be we traverse a row and a column which would be `O(n+n)` i.e `O(n)`. Also we are not consuming any extra space.
