'''

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for s in nums:
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
        
        for k in dic:
            if dic[k]>len(nums)/2:
                return k
