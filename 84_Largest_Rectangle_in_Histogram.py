class Solution:
    def largestRectangleArea(self, heights) -> int:
        
        stack = []
        N = len(heights)
        res = 0
        
        for i in range(N):
            while stack and stack[-1][0] > heights[i]:
                h, _ = stack.pop()
                if stack: res = max(res, h * (i - i - stack[-1][1]))
                else: res = max(res, h * i)
            stack.append((heights[i], i))
        
        while stack:
            h, _ = stack.pop()
            if stack: res = max(res, h * (N - 1 - stack[-1][1]))
            else: res = max(res, h * N)
        return res