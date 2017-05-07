__author__ = 'yyao'

'''
Implement int sqrt(int x).
Compute and return the square root of x.
'''
"""
So called Newton Method
x: f(x) = 0
approaching:
xn+1 = xn - f(xn)/f`(xn)
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return False

        ans = x
        eps = 0.0001
        while abs(ans*ans)-x>eps:
            ans = (ans+x/ans)/2
        return ans
