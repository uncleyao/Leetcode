"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.dfs(root,0)
    
    def dfs(self,root,cur):
        if not root.left and not root.right:
            return root.val + 10*cur
        val = 0
        if root.left:
            val+=self.dfs(root.left,10*cur+root.val)
        if root.right:
            val+=self.dfs(root.right,10*cur+root.val)
        return val
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.dfs(root,0)
    
    def dfs(self,root,cur):
        if not root.left and not root.right:
            return root.val + 10*cur
        val = 0
        if root.left:
            val+=self.dfs(root.left,10*cur+root.val)
        if root.right:
            val+=self.dfs(root.right,10*cur+root.val)
        return val
        
