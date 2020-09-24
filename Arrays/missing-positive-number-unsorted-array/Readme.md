## Smallest positive missing number in unsorted array

We are given an array which contains positive as well as negative number and we need to find the smallest missing positive number in that array.

Ex:

```
3, 1, 4, 6, 7, -2, -8, -12, 10
```
If this the given array then the smallest positive missing number would be `2`. 

## Solution

1) Move all the negative number to the starting of the array. From this step we get a index value which points to the first positive values. After this step the array would look like  `-2, -8, -12, 6, 7, 3, 1, 4, 10`.
2) Ignore all the negative numbers in the starting and traverse the loop from the first positive number.
3) While traversing check if the current index value is less than the length of new array having only positive number.
    - If yes then we change its value from positive to negative.
    - If no then do nothing
4) In the end we will have another array having the following arrangement:

```
-6, 7, -3, -1, 4, -10
```
5) Now just return the index of first positive number, after adding a 1 to it.
