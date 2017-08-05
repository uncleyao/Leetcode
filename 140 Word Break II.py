"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [[] for _ in xrange(len(s)+1)]
        dp[0].append("dummy")
        for i in range(len(s)):
            if not dp[i]:
                continue
            for w in wordDict:
                try:
                    if s[i:i+len(w)] == w:
                        dp[i+len(w)].append(w)
                except IndexError:
                    continue
        result = []
        self.dfs(dp,len(s),[],result)
        return result
    
    def dfs(self, dp, cur_index, cur, result):
        if cur_index == 0:
            result.append(" ".join(cur[::-1]))
            return 
        for prefix in dp[cur_index]:
            self.dfs(dp,cur_index-len(prefix),cur+[prefix],result)
