## Largest non-negative Subarray

__URL__:: https://www.interviewbit.com/problems/max-non-negative-subarray/

## Solution

#### Case 1

In this case we just need to print the length of the maximum non-negative array present in the given array. For this approach we just loop over the array and for every +ve value increment the count and for negative value set the count back to zero.

The time complexity would be `O(n)` and the space complexity would be `O(1)`.

#### Case 2

In this we need to print the element of the largest non-negative subarray. In this instead of maintaining a count we just add the positive values to an array until we find the negative number. When we do we compare this new array with another empty array(which would in the end contain the max length sub-array).

Time complexity remains `O(n)` but space complexity changes.

#### Case 3

In this we are supposed to return the same thing we did in case2 but also if say the length of subarrays are same then we return that subarray which results in higher sum.

Ex: `arr = [0, 1, 1, 0, -2, -4, 0, 1, 0]` in this we return `[0,1,1,0]` because sum of its elements is `2`.
