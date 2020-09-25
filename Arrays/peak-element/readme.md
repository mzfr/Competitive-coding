## Peak element

__URL__:: https://www.interviewbit.com/problems/find-a-peak-element/

## Solution

A normal way of checking elements at a[i+1] and a[i-1], where `i` is the current index of element, would take around `O(n)`. But we can actually have a better solution than this in `O(logn)` way.

For this we just need to find the first peak element and not all of them. We use a sort of binary search to check if the element 1 before the middle element is smaller or greater than the middle one. If it's greater that means the peak element has to be on the left of the middle one else on the right side.

The logic is quite very similar to that of a binary search but instead of comparing a searching element with middle one we are comparing a one right before middle.
