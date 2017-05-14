__author__ = 'yyao'

"""
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, ..., ak) must be in non-descending order. (i.e., a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8,
A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""

class Solution:
    def combinationSum2(self,nums,target):
        nums.sort()
        result = []
        self.generate_n(nums,target,[],result)
        return result

    def generate_n(self,nums,target,current,result):
        if not nums or sum(current)>target:
            return
        if sum(current)== target:
            result.append(current)
        inv = 0
        while inv < len(nums):
            self.generate_n(nums[inv+1:],target,current+[nums[inv]],result)
            while inv+1 < len(nums) and nums[inv]==nums[inv+1]:
                inv+=1
            inv+=1


if __name__=="__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
