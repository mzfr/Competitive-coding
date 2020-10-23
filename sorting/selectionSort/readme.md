## Selection Sort

* In this sorting algorithm, we find the maximum element of the array and then replace it with the last element of that array. This is continued until till the whole array is sorted.
    - We can do the reverse as well i.e take min and put at the first place.
* It always have time complexity of O(n<sup>2</sup>)
* One thing to keep in mind about this algorithm is that it takes the minimum number of swaps out of all the sorting algorithms.


Ex: If the given array was: `[23, 45, 67, 1, 43, 78, 21, 4]`

```
[1, 45, 67, 23, 43, 78, 21, 4]
[1, 4, 67, 23, 43, 78, 21, 45]
[1, 4, 21, 23, 43, 78, 67, 45]
[1, 4, 21, 23, 43, 78, 67, 45]
[1, 4, 21, 23, 43, 78, 67, 45]
[1, 4, 21, 23, 43, 45, 67, 78]
[1, 4, 21, 23, 43, 45, 67, 78]
[1, 4, 21, 23, 43, 45, 67, 78]
```
