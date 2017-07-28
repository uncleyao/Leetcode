"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        imax, imin = nums[0],nums[0]
        r = imax
        i=1
        while i <len(nums):
            imaxthen = max(imax*nums[i],imin*nums[i],nums[i])
            iminthen = min(imin*nums[i],imax*nums[i],nums[i])
            r= max(r,imaxthen)
            imax = imaxthen
            imin = iminthen            
            i+=1
        return r
