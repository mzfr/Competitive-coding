## Bubble Sort

This compare the adjacent elements of the array. So there are like passes in this algorithm. 

Basically in the first pass element at (1,2), (2,3) and so in this way all the elements which are adjacent to each other will be compared. Then in the next pass same thing will be repeated.

This can only be done using two loops one which keeps track of the loops and the next one which will do the comparision.

__Worst case Time Complexity__ : O(n<sup>2</sup>)
__Best case Time Complexity__ : O(n)

But best case depends on the way bubble sort is implemented. Like there could be one if condition which check wether any swaps were made in the past pass, if no then stop since there is no need to go further and the array is already sorted now. 

Ex: 

If an array was: `[4, 7, 1, 9, 3]`

```
Pass 1 -->[4, 1, 7, 3, 9]
Pass 2 -->[1, 4, 3, 7, 9]
Pass 3 -->[1, 3, 4, 7, 9]
Pass 4 -->[1, 3, 4, 7, 9]
```
