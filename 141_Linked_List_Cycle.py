class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        # O(N) space solution: brute force solution
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.curr
        return False

        # O(1) Space solution: Two Pointers.
        if not head: return False
        
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next: return False
            slow = slow.next
            fast = fast.next.next
        return True