## Move all zero to end/front of the array

__URL__:: https://www.geeksforgeeks.org/move-zeroes-end-array/

## Solution

__CASE 1__

In this we move all the zero of the array to the end of the array. To do this we take two variable `i` and `c` and we traverse the array. If the `arr[i]` is not `0` then we update the `arr[c]` with `arr[i]` and increment `c`. Now this means that if intial element aren't `0` then we are putting the same value at the same place. But once we get a `0` than `c` won't increment and then a swap will happen. In the end make all the element after `c` index `0`.

Time complexity - `O(n)`
Space complexity - `O(1)`

__CASE 2__

We move all the zero to the front of the array.

If the first thing you think is just to move all `0` at the end than reverse the array then it's wrong. 

Ex:

arr --> `2, 8, 7, 0, 0, 3, 6, 0, 0, 1`
After moving all `0` at the end ---> `2, 8, 7, 3, 6, 1, 0, 0, 0, 0` 
After reversing ---> `0, 0, 0, 0, 1, 6, 3, 7, 8, 2`

And this is not what we need.

The solution would be to just traverse the array backwards with the same logic.
