"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

Rules:
4 section, and each one less than 256

"""

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.dfs(s,[],result)
        return result
    
    def dfs(self,seq,current,result):
        if not seq and len(current)==4:
            result.append(".".join(current))
            return
        for i in range(1,min(3,len(seq))+1):
            new_s = seq[:i]
            if len(current)<4 and self.is_valid(new_s):
                self.dfs(seq[i:],current+[new_s],result)
            else:
                return
    
    def is_valid(self,s):
        if not s:
            return False
        return s=="0" or s[0]!="0" and 0<=int(s)<256
        
