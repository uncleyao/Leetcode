class Solution(object):
##DFS
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if s in wordDict:
            return True
        for k in wordDict:
            if len(k) <=len(s) and k == s[:len(k)]:
                if self.wordBreak(s[len(k):],wordDict):
                    return True
                else:
                    continue
        return False
        
####DP
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        for i in range(len(dp)):
            if dp[i]:
                for w in wordDict:
                    try:
                        if dp[i+len(w)]:
                            continue
                        if s[i:i+len(w)] == w:
                            dp[i+len(w)] = True
                    except IndexError:
                        continue
        return dp[-1]
    
                    
