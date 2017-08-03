"""
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        ans = []
        maxdp,max_index = 1,0
        dp = [1 for _ in xrange(len(nums))]
        dpindex = [-1 for _ in xrange(len(nums))]
        for i in range(len(nums)):
            for j in range(i-1,-1,-1):
                if nums[i]%nums[j]==0 and dp[j]+1 > dp[i]:
                ## dp[i] is the largest number of elements
                ## dpindex[i] backtwards, get the elements before the last one (reverse linked list)
                    dp[i] = dp[j]+1
                    dpindex[i] = j
                if maxdp < dp[i]:
                    maxdp,max_index = dp[i],i
        while max_index!=-1:
            ans.append(nums[max_index])
            max_index = dpindex[max_index]
        return ans
