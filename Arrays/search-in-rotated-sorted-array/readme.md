## Search in rotated sorted array:

__URL__:: https://www.interviewbit.com/problems/rotated-sorted-array-search/

## Solution

The idea is just to stick with binary search but not in the whole array. First we find which side is rotated i.e find the mid and see if we have the rotated array on the left of mid or on the right of the mid. Once we have found that we apply binary search in the sorted section. 

Time complexity `O(log n)`
