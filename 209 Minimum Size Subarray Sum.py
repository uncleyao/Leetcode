"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.
"""

import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        start = 0
        sums = 0
        end = 0
        minlen = sys.maxint
        while start < len(nums) and end < len(nums):
            while sums < s and end < len(nums):
                sums += nums[end]
                end+=1
            while sums >=s and start < end:
                minlen = min(minlen,end-start)
                sums-= nums[start]
                start+=1
        if minlen < sys.maxint:
            return minlen
        return 0
