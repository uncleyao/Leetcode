"""
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(k,j):
            for i in range(k):
                if board[i] == j or abs(k-i) == abs(board[i]-j):
                    return False
            return True
            
        
        def dfs(depth,cur,result):
            if depth == n:
                result.append(cur)
                return
            for i in range(n):
                if check(depth,i):
                    board[depth] = i
                    s = '.'*n
                    dfs(depth+1,cur+[s[:i]+'Q'+s[i+1:]],result)
        board=[-1 for _ in range(n)]
        result = []
        dfs(0,[],result)
        return result
