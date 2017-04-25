'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
'''
## use dictionary to calculate all counts, and then find the only has 1


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
            
        num = {}
        for v in s:
            if v in num:
                num[v]+=1
            else:
                num[v] =1
        
        for i in range(len(s)):
            if num[s[i]] ==1:
                return i
        return -1
