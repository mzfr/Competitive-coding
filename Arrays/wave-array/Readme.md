## Wave array

__URL__:: https://www.interviewbit.com/problems/wave-array/

## Solution

A wave array is the one in which the following pattern exists:

```
a[0] > a[1] < a[2] > a[3]
```

The solution that we follow is that we check the numbers in pairs first and then we check the last element of pair 1 and first element of next pair.(To cover the edge cases)
