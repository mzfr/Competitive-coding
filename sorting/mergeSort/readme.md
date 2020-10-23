## Merge Sort

* Merge Sort recursively splits the array in half till each element is a single value-d array.
    - Since a single value is always sorted.

* Then it merges all the elements comparing which element to place first in the resultant array.

* This is well suited for Linked List.

### Questions

Some questions that are some how related to or based on merge sort.

* Find the union or intersection of two arrays?
    - The same trick we used in merge function can be used here.

* If there is an array which is half sorted and half unsorted, how would you sort the whole array?
    - Again method of merge function

* Find the inversion pair in an array?
    - Inversion pair is if pair is not in the same other as it would be in the sorted array.
        - If array is [5, 12, 15, 7], so in this there are two pair i.e (12, 7) and (15, 7)
        - Because in sorted array they would have been 7, 12 and 7, 15
    - Way to solve this is that in the merge function we will have to make modifications like do something if right element is smaller in merge function etc
        - https://www.geeksforgeeks.org/python-program-for-count-inversions-in-an-array-set-1-using-merge-sort/
