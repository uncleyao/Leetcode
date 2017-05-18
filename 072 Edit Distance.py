"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        result = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]
        for i in range(1,len(word1)+1):
            result[0][i]=i
        for j in range(1,len(word2)+1):
            result[j][0] =j
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1]==word1[j-1]:
                    result[i][j]=result[i-1][j-1]
                else:
                    result[i][j] = 1 + min(result[i-1][j],result[i][j-1],result[i-1][j-1])
        return result[-1][-1]
