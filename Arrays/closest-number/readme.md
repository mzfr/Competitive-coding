## Closest Number

__URL__: https://www.hackerrank.com/challenges/closest-numbers/problem

## Solution

The Solution for this problem would be that we can traverse over the sorted array(sort it if not sorted already). Then we caculate the absolute difference between all the element and will store the smallest. Then we loop over it again and take out all those elements which have difference equal to that number.

The time complexity would be `O(n)` and space complexity would stay `O(1)` if we print those pairs right away.
