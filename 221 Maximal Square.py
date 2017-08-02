"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        for i in range(m):
            matrix[i] = map(int,matrix[i])
        toleft = [[0 for _ in xrange(len(matrix[0])+1)] for _ in xrange(m+1)]
        totop = [[0 for _ in xrange(len(matrix[0])+1)] for _ in xrange(m+1)]
        
        maxax = 0
        dp = [[0 for _ in xrange(len(matrix[0])+1)] for _ in xrange(m+1)]
        for i in range(1,m+1):
            for j in range(1,len(matrix[0])+1):
                if matrix[i-1][j-1] == 0:
                    continue
                toleft[i][j] += toleft[i-1][j]+matrix[i-1][j-1]
                totop[i][j] += totop[i][j-1]+matrix[i-1][j-1]
                dp[i][j] = min(dp[i-1][j-1]+1,toleft[i][j],totop[i][j])
                maxax = max(maxax,dp[i][j])
        return maxax*maxax
