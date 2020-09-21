## Remove duplicates from the array

__URL__: https://www.hackerrank.com/contests/doyoulikeit/challenges/remove-duplicates-from-sorted-array/problem

## Solution

The very obvious soltution is to just loop over all the and see if the element already exists in the hashmap if yes then we increment the value otherwise add that element to the hashmap with value=1.

```python
for i in arr:
    if i not in hashmap:
    	hashmap[i] = 1
    else:
    	hashmap[i] += 1
```

This is a small example of that. But in python we can just simply make a `set()` of that array and it would give us the same output. Also the time complexity
would stay the same.

If you need the count of the number of time the character/element appeared then the hashmap method is solid.

so the simplest cod for this would be 

```python
_ = input()
arr = input().split()
print(len(set(arr)))
```
