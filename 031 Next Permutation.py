"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        target = 0
        change = 0
        for i in range(length-1,0,-1):
            if nums[i]> nums[i-1]:
                target = i-1
                break
        for i in range(length-1,-1,-1):
            if nums[i]>nums[target]:
                change = i
                break
        nums[target],nums[change] = nums[change], nums[target]
        if target == change == 0:
            nums.reverse()
        else:
            nums[target+1:] = reversed(nums[target+1:])
