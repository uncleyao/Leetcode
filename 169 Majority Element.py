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

 ### linear solution
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = None
        for n in nums:
            if count == 0:
                result = n
            if result == n:
                count +=1
            if result != n:
                count -=1
        return result
