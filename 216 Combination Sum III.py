"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used
and each combination should be a unique set of numbers.
Ensure that numbers within the set are sorted in ascending order.
Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]
Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]
"""

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.combine(k,n,[],result)
        return result
        
    def combine(self,k,n,current,result):
        if k==0 and n==0:
            result.append(list(current))
            return
        
        if k> n or 9*k<n:
            return
        start = 1
        if current:
            start = current[-1]+1
        for i in range(start,10):
            current.append(i)
            self.combine(k-1,n-i,current,result)
            current.pop()
        
