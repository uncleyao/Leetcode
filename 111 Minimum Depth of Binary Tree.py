"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root,0)
    
    def dfs(self,root,result):
        if not root:
            return result
        elif not root.left and root.right:
            return self.dfs(root.right,result+1)
        elif root.left and not root.right:
            return self.dfs(root.left,result+1)
        else:
            return min(self.dfs(root.left,result+1),self.dfs(root.right,result+1))
