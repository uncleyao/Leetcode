"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result = [[0]*m]*n
        result[0] = [1]*m
        for i in range(1,n):
            result[i][0] = 1
        
        for i in range(1,n):
            for j in range(1,m):
                result[i][j] = result[i-1][j]+ result[i][j-1]
        return result[n-1][m-1]
