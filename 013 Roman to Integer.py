'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
'''


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        maps = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        result = 0
        for i in range(len(s)):
            if i > 0 and maps[s[i-1]] < maps[s[i]]:
                result -= maps[s[i-1]]
                reuslt += maps[s[i]]-maps[s[i-1]]
            
            else:
                result += maps[s[i]]
        return result
