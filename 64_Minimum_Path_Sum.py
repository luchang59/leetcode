"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

class Solution:
    def minPathSum(self, grid) -> int:
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        R, C = len(grid), len(grid[0])
        dp = [[0] * C for _ in range(R)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, R):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for j in range(1, C):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            
        for i in range(1, R):
            for j in range(1, C):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                
        return dp[-1][-1]