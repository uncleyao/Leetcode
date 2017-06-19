"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 
        n = len(s)
        if n ==1:
            return s
        ret = s[0]
        for i in range(0,n):
            cur = self.get_palindrome(s,i,i)
            if len(cur) > len(ret):
                ret = cur
            cur = self.get_palindrome(s, i, i+1)
            if len(cur) > len(ret):
                ret = cur
        return ret
        
    def get_palindrome(self, s, start, end):
        while start >=0 and end < len(s) and s[start] == s[end]:
            start-=1
            end+=1
        return s[start+1:end]
