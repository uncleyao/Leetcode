"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dic = {}
        dic2 = {}
        for i, v in enumerate(s):
            if v not in dic:
                dic[v] = [i]
            else:
                dic[v].append(i)
        for j, n in enumerate(t):
            if n not in dic2:
                dic2[n] = [j]
            else:
                dic2[n].append(j)
        return sorted(dic.values()) == sorted(dic2.values())
