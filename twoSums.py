"""https://leetcode.com/problems/two-sum/

This code will only run on the leetcode portal and might cause issues locally
because lot of weird reasons.
"""


class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            n = target - num
            if n not in hashmap:
                hashmap[num] = ind
            else:
                return [hashmap[n], ind]
