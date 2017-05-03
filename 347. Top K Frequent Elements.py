"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #dic = collections.Counter(nums)
        dic = {}
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        dicfreq = [[] for i in range(len(nums)+1)]
        for s in dic:
            dicfreq[dic[s]].append(s)
        result = []
        i = len(dicfreq)-1
        while i >= 0 and len(result) < k:
            result.extend(dicfreq[i])
            i-=1
        return result
