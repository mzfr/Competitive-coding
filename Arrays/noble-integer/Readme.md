## Noble number

__URL__:: https://www.interviewbit.com/problems/noble-integer/

## Solution

Just sort the array and then start to traverse the array one by one. If the next (n-i-1) elements are equal to the current number than we found the noble number. Here `i` is the index of the elements.

Ex: `9 3 18 12` if we sort this we get `3 9 12 18`. after this we see that the starting element is `3` and the next values are also 3.
