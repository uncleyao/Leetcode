"""
Given a binary tree, flatten it to a linked list in-place.
For example,
Given
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
click to show hints.
Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        lst = []       
        self.dfs(root,lst)
        root.left = None
        lst = lst[1:]
        cur = root
        for node in lst:
            node.left = None
            node.right = None
            cur.right = node
         #set cur right
            cur = cur.right
    
    def dfs(self, root,lst):
        if root is None:
            return 
        lst.append(root)
        self.dfs(root.left,lst)
        self.dfs(root.right,lst)
