"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        ro  = []
        pre = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i not in ro:
                        ro.append(i)
                    if j not in pre:
                        pre.append(j)
                
        for i in ro:
            matrix[i]=[0]*len(matrix[0])
        for j in pre:
            for i in range(len(matrix)):
                matrix[i][j]=0
        
            
