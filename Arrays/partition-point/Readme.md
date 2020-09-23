## Partition point of an array

Partition point in an unsorted array of integer would be that element who has all the smaller element to it's left and all greater element to it's right.

EX: 5,4,3,6,9,8,7
In this `6` is the partition point because all element to the left of 6 are smaller than 6 but all the element to the right are greater than 6.

## Solution

Now there is a simple `O(n^2)` approach. Another `O(n)` approach would be to use extra space. 

What we do is, we make two arrays, one store all the greatest element from the array traversing from left to right. Another would store the smallest value going from right to left.

Ex: If the array was `5,4,3,6,9,8,7` then

array1 - Greater element from left(GEL) will be -> `5,5,5,6,9,9,9`
array2 - smaller element from right will(SER) be -> `3,3,3,6,7,7,8`

Now we find the element in array which satisfy the condition: GEL[i-1] < a[i] > SER[i+1]

***

Keeping this idea in mind what I have done is instead of making two list I made 1 list for all the greater element and instead of making another list for smaller element I kept track of smaller element using a variable.
