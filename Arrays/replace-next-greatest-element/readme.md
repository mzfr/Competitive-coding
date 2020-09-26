## Replace all element with greatest

__URL__:: https://www.geeksforgeeks.org/replace-every-element-with-the-greatest-on-right-side/

## Solution

We loop from the right to left and since there won't be an element to the right of the last element than it will has to be replaced with `-1`. Once we do that we keep track of the greatest element and updates the next value.

Time complexity -  `O(n)`
Space complexity - `O(1)`
