## Maximum difference unsorted array

__URL__:: https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

```
Maximum difference between two elements such that larger element appears after the smaller number
```

## Solution

We consider a maxdiff which contain difference of element of array at index 1 and 0. And we take the very first element as the minimum element of array. Than we loop over the array and check if difference of current element and `minimum` element is greater than the `maxdiff` or not. If yes than update maxdiff. Than we update the minimum value in case the current element is smaller than existing minimum value.

The time complexity would be `O(n)` and space complexity will be `O(1)`.

If we are asked to print those element than we can add another loop like:

```python
for i in arr:
    if i-min_ == maxdiff:
        print(i, min_)
        break
```
Complexity would still remain the same.
