"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

"""

class Solution(object):
    def __init__(self):
        self.result = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(k,j):
            for i in range(k):
                if board[i] == j or abs(k-i) == abs(board[i]-j):
                    return False
            return True
        
        def nqueen(depth):
            if depth == n:
                self.result+=1
                return
            for i in range(n):
                if check(depth,i):
                    board[depth] = i                    
                    nqueen(depth+1)
        
        board = [-1 for _ in range(n)]
        nqueen(0)
        return self.result
        
