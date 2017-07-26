"""
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
"""

from math import sqrt

class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        
        ###Use list as input to pop and append
        self.dfs([n],result)
        return result
    
    def dfs(self,cur,result):
        if len(cur) >1:
            result.append(list(cur))
            
        ## pop it b/c the last will be used to divide    
        n = cur.pop()
        start = 2 if not cur else cur[-1]
        for i in range(start,int(sqrt(n))+1):
            if n%i==0:
                cur.append(i)
                cur.append(n/i)
                self.dfs(cur,result)
                cur.pop()  ##This is used for start with a new i
                
