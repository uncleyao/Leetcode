"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""


#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        length = self.getLength(head)
        k = k % length
        q = length - k
        p = 0
        pi1 = head
        while p < q-1:
            pi1 = pi1.next
            p+=1
        pi2 = head
        while pi2.next:
            pi2 = pi2.next
        pi2.next = head
        result = pi1.next
        pi1.next = None
        return result
        
        
    
    
    def getLength(self, head):
        length = 0
        while head:
            length+=1
            head = head.next
        return length
