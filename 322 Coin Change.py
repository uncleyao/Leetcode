"""
"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the
fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.
Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)
Example 2:
coins = [2], amount = 3
return -1.
Note:
You may assume that you have an infinite number of each kind of coin.
"""

import sys

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        f = [sys.maxint for _ in xrange(amount+1)]
        f[0] = 0
        for i in range(amount+1):
            for k in coins:
                if k+i <=amount:
                    f[i+k]= min(f[i+k],f[i]+1) 
        return f[amount] if f[amount] < sys.maxint else -1
