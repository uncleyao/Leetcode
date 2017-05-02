'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=2:
            return n
        m = []
        m.append(1)
        m.append(2)
        for i in range(2,n):
            k = m[i-2]+ m[i-1]
            m.append(k)
        return m[-1]
