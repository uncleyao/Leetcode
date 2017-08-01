"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ###be very careful about this part
        if not s or s[0]=='0':
            return 0
        f = [0 for _ in xrange(len(s)+1)]
        f[0] = 1
        f[1] = 1       
        for i in range(2,len(s)+1):
            if int(float(s[i-1])) !=0:
                f[i] = f[i-1]
                if int(float(s[i-2:i])) <= 26 and int(float(s[i-2:i]))>=10:
                    f[i]+= f[i-2]
            else:
                if s[i-2] in ('1','2'):
                    f[i] = f[i-2]
                else:
                    return 0
        return f[-1]
