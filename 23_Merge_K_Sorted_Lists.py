class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):

        N = len(lists)
        interval = 1
        while interval < N:
            for i in range(0, N - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if N > 0 else lists

    def merge2Lists(self, l1, l2):
        dummy = curr = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        if l1: curr.next = l1
        if l2: curr.next = l2
        return dummy.next 


    """
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    0,    2,    4,    6,    8,
    0,          4,
    0,
    
    """