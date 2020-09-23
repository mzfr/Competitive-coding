## Pairs

__URL__: https://www.hackerrank.com/challenges/pairs/submissions/code/161352379

## Solution

This is really nice problem and can be very deceiving at the beginning.

The solution1 have the complexity of `O(n)` and have space complexity of `O(n)`, now here the time complexity cannot be reduced but in the optiomal solution we will be able to finish the problem in `O(1)` space complexity.

The solution2 is optimal because it doesn't take extra space and the reason behind it is that we take two variables and move them in one way (left to right). And every step we check the difference of those two variables if diff is equals to `K` then we just increase the count(or print the pair if needed). If diff is less then `k` that means we increase the variable `j`, if diff is greater then we increase the `i`.

The thing is solution2 only works on sorted array meaning we need to sort the array before we do this operation.
