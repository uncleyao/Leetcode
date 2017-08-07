"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(root,sum,[],result)
        return result
        
    def dfs(self,root,sum,cur,result):
        if not root:
            return
        cur.append(root.val)
        sum -= root.val
        if sum == 0 and root.left is None and root.right is None:
            result.append(cur)
        if root.left:
            self.dfs(root.left,sum,list(cur),result)
        if root.right:
            self.dfs(root.right,sum,list(cur),result)
        
        
        
        
