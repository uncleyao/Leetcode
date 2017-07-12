"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    We can use (n-1)%26 instead, then we get a number range from 0 to 25.
"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        while n>0:
            result+=chr(ord('A')+(n-1)%26)
            n = (n-1)//26
        return result[::-1]
