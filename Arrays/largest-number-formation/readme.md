## Largest Number formation

The question is that we are given an array and we need to return the maximum possible number from that.

Ex: 
If the given array is `["55", "566", "66", "9"]` Than the maximum number possible out of these digits is `96656655`.

If given array is `["2", "34", "4", "97", "9", "75", "46", "3"]` than the output would be `997754643432`.

## Solution

The simples idea is that we compare each element with each other and while comparing we check the following:

if `concat(arr[i], arr[i+1]) < concat(arr[i+1], arr[i])`. This means say if the numbers are `55` and `566` so we check if 
`55566 < 56655`, if yes then we swap their value in the array.

This is done with all the elements. The time complexity in this case will be `O(n^2)` and space complexity would be `O(1)`.
