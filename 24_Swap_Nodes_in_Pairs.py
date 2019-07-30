class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        # iteration solution:
        if not head: return head
        
        dummy = prev = ListNode(-1)
        dummy.next = head

        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            head = head.next
            prev.next = tmp
            prev = tmp.next
        
        return dummy.next

        # recursion solution:
        if not head or not head.next: return head
            
        tmp = head.next
        head.next = self.swapPairs(tmp.next)
        tmp.next = head
        return tmp 