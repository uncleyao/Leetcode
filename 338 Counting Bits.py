"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].
可以发现，[0,1]各加1，就是后两项[1,2];[0，1，1，2]各加1，就是后四项[1,2,2,3]。依此类推，前2^n项各加1，就可以生成前2^(n+1)项


"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ret = [0]
        i = 0
        cur = len(ret)
        while len(ret) <= num:
            if i== cur:
                i = 0
                cur = len(ret)
            ret.append(1+ret[i])
            i+=1
        return ret
