"""

Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a = set('QWERYUIOP')
        b = set('ASDFGHJKL')
        c = set('ZXCVBNM')    
        ans = []
        for w in words:
            t = set(w.upper())
            if a&t==t or b&t==t or c&t==t:
                ans.append(w)
        return ans
