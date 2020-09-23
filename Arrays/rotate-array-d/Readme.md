## Left Rotate array by d element

__URL__: https://www.hackerrank.com/challenges/ctci-array-left-rotation/submissions/code/159795430

## Solution

I think sometime you just need to stop worrying about the complexity and appreciate the simplicity.

```python
d = int(input())
arr = input().split()

result = arr[d:] + arr[:d]
print(" ".join(map(str, result)))
```

In this 4 lines of code 3 lines are just for input/output and formatting. The real stuff happesn in the `result = arr[d:] + arr[:d]`. Here we use `slice`. The time complexity of the code would be `O(nk)` and space complexity would be `O(n)`. The `k` in the time complexity would be the size of the `slice`, so if we increase the value of `d` in our code then yes it would consume more time.

The optiomal solution would be time complexity of `O(n)` and space complexity of `O(1)`. In that solution also we do similar thing as we did in the above solution the only difference is the complexity would be less. 

__Optiomal  Solution__

Say we have the array `1 2 3 4 5` and `d` is 4 so the output would be `5 1 2 3 4`. 

What we will do is that first we reverse the element from `0` to `d-1`. Then reverse the element `d` to `n-1` and then finally reverse the whole array. In this method we only get the maximum time complexity to be `O(n)` and space remains `O(1)` because we don't make any new array.
