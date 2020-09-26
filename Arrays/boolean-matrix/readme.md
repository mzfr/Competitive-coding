## Boolean Matrix

__URL__:: https://www.geeksforgeeks.org/a-boolean-matrix-question/

## Solution

The solution one has the time complexity of `O(n*m)` and space complexity of `O(n+m)`. Basically we take two array one for the row and one for the column and then we check if any of the zeroth row or zeroth column is `1`is yes then we update those arrays.

In the end we use those array to edit the remaining part of the matrix.

***

Solution 2 is better because it can be done in space complexity of `O(1)`.

In this solution we uses right flag and column flag which is used to to know if any zeroth row or column have 1 in it or not. Then we use those flags to update the remaining matrix. In the end those flags helps to add any `1` in the zeroth  row or column
