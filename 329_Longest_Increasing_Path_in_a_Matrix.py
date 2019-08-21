"""
Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:
Input: nums = [[9,9,4], [6,6,8], [2,1,1]] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: nums = [[3,4,5], [3,2,6], [2,2,1]] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""
import collections
class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix: return 0

        R, C = len(matrix), len(matrix[0])
        memo = [[0] * C for _ in range(R)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        res = 0

        def backTrack(r, c):
            if memo[r][c] != 0: return memo[r][c]
            for d0, d1 in directions:
                nr, nc = r + d0, c + d1
                if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] < matrix[r][c]:
                    memo[r][c] = max(memo[r][c], backTrack(nr, nc))
            memo[r][c] += 1
            return memo[r][c]
        
        for i in range(R):
            for j in range(C):
                res = max(res, backTrack(i, j))
        
        return res
        
        # Topological Solution
        # if not matrix: return 0
        
        # m, n = len(matrix), len(matrix[0])
        # directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # hmap = {}
        # queue = collections.deque()
        # for i in range(m):
        #     for j in range(n):
        #         cnt = 0
        #         for dx, dy in directions:
        #             x, y = i + dx, j + dy
        #             if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
        #                 cnt += 1
        #         hmap[(i, j)] = cnt
        #         if cnt == 0:
        #             queue.append((i, j))
        # # print(hmap)
        # step = 0
        # while queue:
        #     size = len(queue)
        #     for k in range(size):
        #         i, j = queue.popleft()
        #         for dx, dy in directions:
        #             x, y = i + dx, j +dy
        #             if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j] and (x, y) in hmap:
        #                 hmap[(x, y)] -= 1
        #                 if hmap[(x, y)] == 0:
        #                     queue.append((x, y))
        #     # print(hmap)
        #     # print(queue)
        #     step += 1
        # return step