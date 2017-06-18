"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.get_partition(s,[],result)
        return result
    
    def get_partition(self,seq,cur,result):
        if not seq:
            result.append(cur)
        
        for i in range(len(seq)):
            if self.is_palidrome(seq[:i+1]):
                self.get_partition(seq[i+1:],cur+[seq[:i+1]],result)
        
    def is_palidrome(self,s):
        return s== s[::-1]
