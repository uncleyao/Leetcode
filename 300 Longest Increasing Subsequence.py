"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        f = [1 for _ in xrange(len(nums))]
        maxresult = 1
        for i in range(1,len(nums)):
            f[i] = max(f[j]+1 if nums[i]> nums[j] else 1 for j in range(i))
            maxresult = max(maxresult,f[i])
        return maxresult
        
