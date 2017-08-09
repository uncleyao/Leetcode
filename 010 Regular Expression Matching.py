"""
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true
"""
### DFS

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        S = s
        P = p
        if not S and not P:
            return True
        if S and not P:
            return False
        if not S and P:
            if len(P)>=2 and P[1] == '*':
                return self.isMatch(S,P[2:])
            else:
                return False
        if len(P)>=2 and P[1] == '*':
            if S[0] == P[0] or P[0] == '.':
                return self.isMatch(S,P[2:]) or self.isMatch(S[1:],P[2:]) or self.isMatch(S[1:],P)            
            else:
                return self.isMatch(S,P[2:])        
        else:
            if S[0] == P[0] or P[0] == '.':
                return self.isMatch(S[1:],P[1:])
            else:
                return False
