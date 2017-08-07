"""
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        result = []
        self.dfs(root,"",result)
        return result
    
    def dfs(self,root,cur,result):
        if root is None:
            return
        if cur == "":
            cur = str(root.val)
        else:
            cur = cur + "->" + str(root.val)
        if root.left is None and root.right is None:
            result.append(cur)
        self.dfs(root.left, str(cur),result)
        self.dfs(root.right,str(cur),result)
