"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
"""
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.F = [0 for _ in xrange(len(nums)+1)]
        for i in range(len(nums)):
            self.F[i+1] = self.F[i] + nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.F[j+1] - self.F[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
