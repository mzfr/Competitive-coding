## Pascal triangle

__URL__:: https://www.geeksforgeeks.org/pascal-triangle/

## Solution

There are two way to be doing this:

1) Just print without actually storing the triangle which would make space comlexity to `O(1)`.
2) Store the values of a pascal triangle, this make the complexity `O(n^2)`.

In both the cases the time complexity remains `O(n^2)`.

In case 1 we start by making an empty 2D array of NxN. Then we make two loops, one tells us the number of lines in the triangle and one tells us elements we should add in one line. 
Inside those loops we check for a condition which is, if the current element is `0` or is equal to the `line` number we currently are on than keep the value `1` else add the element of previous rows and set it to current values.

*** 
In the 2nd approach we do kind of similar thing but with a formula. Instead of storing we consider a varible say `C`. In this we don't check a condition but instead we use the following formula:

```
C = C * (current_line_number - current_column)/current_column
```

This is basically using the polynomial series formula.

```python
for line <= n:
    for col <= line:
        print(c)
        c = c*(line-col)//col
    print()
```

