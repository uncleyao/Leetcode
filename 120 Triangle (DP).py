"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

DP SOLUTION
create minpath[][]
dp from bottom to top
minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        minret = [[x for x in triangle[-1]]]
        for i in xrange(len(triangle)-2,-1,-1):
            minret.insert(0,[])
            for k in range(i+1):
                minret[0].append(min(minret[1][k],minret[1][k+1])+triangle[i][k])
        return minret[0][0]
