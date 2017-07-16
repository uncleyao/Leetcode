"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""

class Solution(object):
    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftind = [0 for _ in height]
        rightind = [0 for _ in height]
        leftmaxind = 0
        rightmaxind = 0
        for i,v in enumerate(height):
            leftmaxind = max(leftmaxind,v)
            leftind[i] = leftmaxind
        for i,v in reversed(list(enumerate(height))):
            rightmaxind = max(rightmaxind,v)
            rightind[i] = rightmaxind
        result = 0
        for i in range(len(height)):
            result += max(min(leftind[i],rightind[i])-height[i] ,0)
        return result

    def trap(self, height):
        leftmax,rightmax = 0,0
        result = 0
        i,j = 0,len(height)-1
        while i <j:
            if height[i]<=height[j]:
                leftmax = max(leftmax,height[i])
                result += leftmax-height[i]
                i+=1
            else:
                rightmax = max(rightmax,height[j])
                result += rightmax-height[j]
                j-=1
        return result
        
