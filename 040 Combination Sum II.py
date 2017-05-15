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

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        result = []
        self.combinationT(candidates,target,[],result)
        return result
        
    def combinationT(self, candidates, target, current, result):
        s = sum(current) if current else 0
        if s > target:
            return
        elif s== target:
            result.append(current)
        inv = 0
        while inv < len(candidates):
            self.combinationT(candidates[inv+1:],target,current+[candidates[inv]],result)
            while inv < len(candidates)-1 and candidates[inv]==candidates[inv+1]:
                inv+=1
            inv+=1


if __name__=="__main__":
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
