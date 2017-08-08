"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""

class Solution(object):
    def __init__(self):
        self.d = {}
        
    def canWin2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s not in self.d:
            flag = False
            for i in range(len(s)-1):
                if s[i:i+2] == '++':
                    if not self.canWin2(s[:i]+'--'+s[i+2:]):
                        flag = True
                        break
            self.d[s] = flag
        return self.d[s]
    
    def canWin(self,s):
        for i in range(len(s)-1):
            if s[i:i+2]=='++':
                if not self.canWin(s[:i]+'--'+s[i+2:]):
                    return True
        return False
                    
                    
