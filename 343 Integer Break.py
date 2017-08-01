"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: You may assume that n is not less than 2 and not larger than 58.
"""
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n+1)]
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = max(max(dp[i-j]*dp[j],j*dp[i-j],(i-j)*dp[j],j*(i-j)) for j in range(1,i//2+1))
        return dp[-1]
