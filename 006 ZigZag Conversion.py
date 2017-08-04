"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        nums = len(s)
        maxtrix = [[] for _ in xrange(numRows)]
        i= 0
        while i < nums:
            try:
                for j in range(numRows):
                    maxtrix[j].append(s[i])
                    i+=1
                for j in range(numRows-2,0,-1):
                    maxtrix[j].append(s[i])
                    i+=1
            except IndexError:
                break
        lst = []
        for ma in maxtrix:
            lst.append("".join(ma))
        return "".join(lst)
