"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.dfs(nums,[],result)
        return result
    
    def dfs(self,nums,current,result):
        result.append(current)
        i = 0
        while i < len(nums):
            self.dfs(nums[i+1:],current+[nums[i]],result)
            while i < len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1
            
