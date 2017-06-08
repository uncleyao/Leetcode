"""
Determine whether an integer is a palindrome. Do this without extra space.
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <0:
            return False
        div =1
        while x/div>= 10:
            div*=10
        while x> 0:
            l = x//div
            val = x%10
            if l != val:
                return False
            x %= div
            x//=10
            div /= 100
        return True
