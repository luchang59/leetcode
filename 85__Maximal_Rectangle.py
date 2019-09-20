"""
85. Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix: return 0

        def helper(heights):
            stack = []
            N = len(heights)
            res = 0
            for i in range(N):
                while stack and stack[-1][0] > heights[i]:
                    h, _ = stack.pop()
                    if stack: res = max(res, h * (i - 1 - stack[-1][1]))
                    else: res = max(res, h * i)
                stack.append((heights[i], i))
            
            while stack:
                h, _ = stack.pop()
                if stack: res = max(res, h * (N - 1 - stack[-1][1]))
                else: res = max(res, h * N)
            
            return res

        ans = 0
        R, C = len(matrix), len(matrix[0])
        heights = [0] * C

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, helper(heights))

        return ans