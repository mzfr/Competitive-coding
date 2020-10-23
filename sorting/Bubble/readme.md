## Bubble Sort

This compare the adjacent elements of the array. So there are like passes in this algorithm. 

Basically in the first pass element at (1,2), (2,3) and so in this way all the elements which are adjacent to each other will be compared. Then in the next pass same thing will be repeated.

This can only be done using two loops one which keeps track of the loops and the next one which will do the comparision.

__Worst case Time Complexity__ : O(n^2)
__Best case Time Complexity__ : O(n)

But best case depends on the way bubble sort is implemented. Like there could be one if condition which check wether any swaps were made in the past pass, if no then stop since there is no need to go further and the array is already sorted now. 
