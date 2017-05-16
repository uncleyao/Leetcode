"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.dfs(nums,[],result)
        return result
    
    def dfs(self,nums,current,result):
        if not nums:
            result.append(current)
        ind = 0
        while ind <len(nums):
            self.dfs(nums[:ind]+nums[ind+1:],current+[nums[ind]],result)
            while ind <len(nums)-1 and nums[ind]==nums[ind+1]:
                ind+=1
            ind+=1
