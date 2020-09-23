## Sorting in one scan

__Question__: Sort an array of 0's, 1's, 2's in O(n) time complexity and one scan.

## Solution

The solution is quite simple. Just take 3 variables low, mid, high. Low and mid are pointing to the first index and the high point to the last index or we can say `(len of array - 1)`. Now we traverse the array, if we find a `0` then swap the mid with low and then increase both low and mid. If we come across 2 then we swap `mid` with `high` and then decrement the `high`. If none is the case then just increment the `mid`.
