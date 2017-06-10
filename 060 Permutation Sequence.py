"""
The set [1,2,3,…,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if not n:
            return ""
        result = ""
        product = 1
        nums  = []
        for i in range(1,n+1):
            nums.append(i)
            product*= i
        if k > product:
            return ""
        k -=1
        
        for j in range(n,0,-1):
            product/=j
            index = k//product
            result += str(nums[index])
            del nums[index]
            k = k % product
        return result
