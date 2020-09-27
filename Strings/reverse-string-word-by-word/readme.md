## Reverse string word by word

__URL__:: https://www.hackerrank.com/contests/launchpad-1-winter-challenge/challenges/string-reverse-words/

## Solution

```python
_ = input()

string = input()

for i in string.split(' ')[::-1]:
    print(i, end=" ")
```

This is the solution. The complexity in this would be `O(n)`.

What we did was we split the string on whitespaces and than reverse the string. After that just frint those words.

***

The one thing in this is that if we use `split()` than there is one edge case that would fail. The edge case is when we give extra spaces in the input string and wants to retain them.

EX: the input is 
```
Hello    World!. 
```

As we can see there are multiple spaces in between and the expected output world be `World!.    Hello`

If we split this string just with `split()` than those white spaces will be ignored. That is why we are using `split(' ')`
