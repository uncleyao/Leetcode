# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.current_node = None
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return head
        
        self.current_node = head
        lenth = self.getlength(head)
        return self.sortedListdfs(0,lenth-1)
    
    def sortedListdfs(self,start,end):
        if start > end:
            return
        mid = (start+end)/2
        left_sub = self.sortedListdfs(start,mid-1)
        root = TreeNode(self.current_node.val)
        self.current_node = self.current_node.next
        right_sub = self.sortedListdfs(mid+1,end)
        root.left = left_sub
        root.right = right_sub
        return root
    
    def getlength(self,head):
        count = 0
        while head:
            head = head.next
            count+=1
        return count
        
