## Missing array in number

__URL__: https://www.hackerrank.com/contests/test-contest-39/challenges/missing-number-in-array/

## Solution

Solution1.py contains a code which is very simple to understand and is based on a simple mathematic formula. What we did was first we calculated the sum of all the element of the array. Then we use the formula `(n+1)*(n+2)//2`, this formula is for finding the sum of `n` numbers. Here we take `n` as the length of the array. Then we subtract both of them and we'll get the missing number.

The time complexity would be `O(n)` since for finding the sum of array we will have to loop over it. But this is a bad technique in case the array is really big. 

__Optimal Solution__

Use XOR. We will first XOR all the element of array and store the output in a variable. Then we will XOR all the element till `n`. Then later XOR both the variables.
