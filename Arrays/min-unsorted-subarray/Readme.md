## Minimum length unsorted array

__URL__:: https://www.interviewbit.com/problems/maximum-unsorted-subarray/

## Solution

The solution given is of time complexity `O(n)`.

We start with finding the first element which would be unsorted. We did that by searching the element after which the smaller value appear(call it `l`). In similar manner we find the last element that should be in the unsorted array(call it `r`).

Once we found those element we consider the `l` as the max value and `r` the min value. Now we loop over the unsorted section and then if the found element is greater then `max` value so we update the max value with the newly found one. Also we check if the element is smaller than the `min` value, if so update the min. 

Then in the last we make sure that no element in the LHS sorted section is bigger than the `min` value, if yes then update the `l`. Do the same with RHS sorted section and max value.

In the end just print `l` and `r`.
