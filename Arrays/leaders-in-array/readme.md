# Leaders in array

__URL__: https://www.hackerrank.com/contests/gcfl3/challenges/leaders-in-array-2/problem

## Solution

The very first solution I could come up with was that we start to traverse the array from the left side, the last element will always be a `leader` because there is no element to it's left. Then we take a `MAX` value which for starting we can consider the last element of the array. Now loop over the array(in reverse) and check if the current value is greater then the `MAX` if yes then take that value as leader and update the value in `MAX`.

The time complexity would be `O(n)` and for space complexity you can just print the element right there, if that is the case then it would be O(1). But in my solution I am adding all the leaders to another list which would make the Space complexity to be O(n)
