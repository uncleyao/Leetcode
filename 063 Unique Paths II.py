"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
"""

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] ==1 or obstacleGrid[m-1][n-1] ==1:
            return 0
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                elif i ==0:
                    dp[i][j] = dp[i][j-1] if obstacleGrid[i][j] == 0 else 0
                elif j == 0:
                    dp[i][j] = dp[i-1][j] if obstacleGrid[i][j] == 0 else 0
                else:
                    if obstacleGrid[i-1][j]==0 and obstacleGrid[i][j-1] == 0:
                        dp[i][j]= dp[i-1][j]+ dp[i][j-1]
                    elif obstacleGrid[i-1][j] == 0 and obstacleGrid[i][j-1]==1:
                        dp[i][j] = dp[i-1][j]
                    elif obstacleGrid[i][j-1] == 0 and obstacleGrid[i-1][j]==1:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j]= 0
        return dp[-1][-1]
