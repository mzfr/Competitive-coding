## All triplet having zero sum

__URL__:: https://www.hackerrank.com/contests/launchpad-1-winter-challenge/challenges/find-triplets-that-sum-to-x/problem

## Solution

The brute force method takes `O(n^3)` and then there is another way which involves using hashmap but in the even though the time complexity will be reduced to `O(n^2)` but the space complexity with increase.

The optimal solution where time complexity would be `O(n^2)` and space complexity will be `O(1)` would be that we take an element `x` which is the value of the first element after sorting the given array. Then we take two pointer a `l` which points to index `1` ahead of `x` and another pointer `r` which starts from the end of the array.

Now we check the sum of `x + arr[l] + arr[r]`, whether it's greater or smaller or equal to `0`. If equal than just print those values and increment in `l` and decrement in `r`. Other wise if it's greater than `0` then we increase the `l` else we decrease the `r`.

