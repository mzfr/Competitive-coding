## Maximum distance

__URL__:: https://www.interviewbit.com/problems/max-distance/

## Solution

We take two additional array one called `lmin` which store the minimum value going from left to right. Another one called `rmax` does the same but for maximum value.

After that we take two pointers `i` and `j` pointing on starting of `lmin` and `rmax` respectively and we check if the value of `lmin[i]` is smaller than `rmax[j]` if yes then we take out the max count else we increment `i`.
