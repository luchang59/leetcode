"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4

Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        基本原理是归并排序，先将list拆开，然后再sort，然后merge
        """
        
        def divide(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(left, right):
            dummy = curr = ListNode(-1)

            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    curr = curr.next
                    left = left.next
                else:
                    curr.next = right
                    curr = curr.next
                    right = right.next

            if left: curr.next = left
            if right: curr.next = right
            
            return dummy.next
        
        if not head or not head.next: return head
        
        mid = divide(head)
        right = self.sortList(mid.next)
        mid.next = None
        left = self.sortList(head)
        
        return merge(left, right)