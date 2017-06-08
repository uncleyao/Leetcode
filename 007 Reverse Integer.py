"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x<0:
            flag = -1
        else:
            flag = 1
        result = 0
        x = x*flag
        while x>=10:
            result*=10
            result += x%10
            x = x//10
        result = result*10 + x%10

        
        if result > 2147483647:
            return 0
        return result*flag
