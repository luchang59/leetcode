class Solution:
    def trap(self, height):
        res = 0
        stack = []

        for i in range(len(height)):
            while stack and height[i] > stack[-1]:
                bot = stack.pop()
                if not stack:
                    break
                width = i - stack[-1] - 1
                length = min(height[i], height[stack[-11]]) - height[bot]
                res += width * length
            stack.append(i)

        return res