import collections

class Solution:
    def slidingWindowMaximum(self, nums, k):

        n = len(nums)
        res = []
        
        if n * k == 0: return []
        
        if k == 1: return nums

        queue = collections.deque()
        index = 0

        def update(i):
            if queue and queue[0] == i - k:
                queue.popleft()
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()

        for i in range(k):
            update(i)
            queue.append(i)
            if nums[i] > nums[index]:
                index = i

        res.append(nums[index])

        for i in range(k, n):
            update(i)
            queue.append(i)
            res.append(nums[queue[0]])
        
        return res