"""
ONLY One buy and sell!!!!!
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        minprice , maxsofar = prices[0],0
        for i in range(1,len(prices)):
            if prices[i]< minprice:
                minprice = prices[i]
            else:
                maxsofar = max(prices[i]-minprice,maxsofar)
        return maxsofar
