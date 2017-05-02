'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        current = nums[0]
        m= current
        for i in range(1,len(nums)):
            if current < 0:
                current = 0
            current +=nums[i]
            m = max(m,current)
        return m
        
