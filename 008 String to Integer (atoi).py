"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        if not str:
            return 0
        str  = str.strip()
        flag = 1
        if str[0] in ['+','-']:
            if str[0] == '-':
                flag = -1
            str = str[1:]
        if not str or not str[0].isdigit():
            return 0
        for i,v in enumerate(str):
            if not v.isdigit():
                str = str[:i]
                break
        result = 0
        for v in str:
            result += ord(v)- ord('0')
            result*=10
        result /=10
        result *= flag
        
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        return result
