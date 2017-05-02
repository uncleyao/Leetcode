'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dics = {}
        dict = {}
        for ws in s:
            if ws in dics:
                dics[ws]+=1
            else:
                dics[ws]=1
        
        for wt in t:
            if wt in dict:
                dict[wt]+=1
            else:
                dict[wt]=1
            
        return dict==dics
