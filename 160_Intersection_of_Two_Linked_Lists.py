class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # O(M + N) time complexity, O(M) or O(N) space complexity
        if not headA or not headB: return
        
        dic = set()
        curr = headA
        while curr:
            dic.add(curr)
            curr = curr.next
        
        curr = headB
        while curr:
            if curr in dic: return curr
            curr = curr.next
        
        return
        # O(M + N) time complexity, O(1) space complexity

        if not headA or not headB: return
        
        curr = headA
        while curr: curr = curr.next
        curr.next = headB

        fast = slow = headA
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = headA
                while fast != slow:
                    slow, fast = slow.next, fast.next
                curr.next = None
                return slow
        curr.next = None
        return None