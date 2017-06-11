"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums)/2
        leftvalue = self.sortedArrayToBST(nums[:mid])
        rightvalue = self.sortedArrayToBST(nums[mid+1:])
        root= TreeNode(nums[mid])
        root.left = leftvalue
        root.right = rightvalue
        return root
