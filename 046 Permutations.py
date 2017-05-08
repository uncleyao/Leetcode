
"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Use function loop

"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.get_permute(nums,[],result)
        return result
    
    def get_permute(self,seq,current,result):
        length = len(seq)
        if length == 0:
            result.append(current)
            
        for ind,val in enumerate(seq):
            self.get_permute(seq[:ind]+seq[ind+1:],current+[val],result)
