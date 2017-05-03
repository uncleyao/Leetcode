"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = [1]*len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
            
        right = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1]*nums[i+1]
        
        for i in range(0,len(nums)):
            nums[i] = left[i]*right[i]
        return nums
