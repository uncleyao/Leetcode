"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
"""

"""
There are so many ways, this is DP
"""

import sys

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [sys.maxint for _ in xrange(n+1)]
        result[0] = 0
        for i in range(1,n+1):
            j = 1
            while j*j <= i:
                result[i] = min(result[i],result[i-j*j]+1)
                j+=1
        return result[-1]
