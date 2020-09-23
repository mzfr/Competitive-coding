## Rotate a matrix 90 degree clockwise

__URL__: https://www.hackerrank.com/contests/cs1300-odd-2014/challenges/array-rotation

## Solution

The basica idea would be to just take out the transpose of the matrix and then reverse it. 

In python we can do this just by doing `list(zip(*matrix[::-1]))`.

__Explanation__:

* `[::-1]` - This would reverse the matrix, which is nothing but a list of lists. The important thing to remember here is that `[::-1]` make a copy of original. If you want to save space as well then use `reversed`.

* `*` - This will unpack the lists for zip()
* `zip()` - This will just take ever element from same index or array and then packs them together to give a `tuple`. If we pass [[1,2,3], [5,6,7]] in zip() function then it will make a tuple of `(1,5), (2,6), (3,7)`.

__Anticlockwise rotation__

One was is to use the below given `one-liner`.

```
new_matrix = [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
```

In this we are basically running two loops, the `len(m[0])-1` tells the starting point of the loop, `-1` tells the end point i.e the last element and the last `-1` tells the number with which the values would decrease.

Another shorter way to do an anticlockwise rotation is using the following oneliner

```
list(reversed(list(zip(*matrix))))
```
As you see above we don't use `[::-1]` that means the original is being modified in the memory.	

```
list(zip(*matrix))[::-1]
```

__The C/C++ method__

If you don't have the luxury of python or doesn't want to use those one liners then the simples code can be found in the solution.p

__The C/C++ method__

If you don't have the luxury of python or doesn't want to use those one liners then the simples code can be found in the solution.py. Even though it's written in python but the same code be edit to suit the C/C++ format.
