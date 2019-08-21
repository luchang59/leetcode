"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        def reverse(node, count):
            prev = node
            
            while count > 0:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
                count -= 1
            
            return node, prev
        
        if not head or k in (0, 1): return head
        
        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1
            if count >= k: break
        
        if count < k: return head
        nxt, cur = reverse(head, k)
        head.next = self.reverseKGroup(nxt, k)
        return cur