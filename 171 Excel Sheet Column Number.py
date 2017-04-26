'''
Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
'''

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = ord("A")
        number = 0
        n = len(s)
        for i,word in enumerate(s):
            number = number + (ord(word)-base+1) * pow(26,n-i-1)
        return number
        
if __name__ == "__main__":
    assert Solution().titleToNumber('A') == 1
    assert Solution().titleToNumber('AB') == 28 
