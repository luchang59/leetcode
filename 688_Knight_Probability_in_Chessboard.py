"""
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability that the knight remains on the board after it has stopped moving.

Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
 
Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
"""

class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1
        directions = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for d in directions:
                        nr, nc = r + d[0], c + d[1]
                        if 0 <= nr < N and 0 <= nc < N:
                            dp2[nr][nc] += val
            dp = dp2
        
        res = 0
        for i in range(N):
            for j in range(N):
                res += dp[i][j]
        
        return res / (8 ** K)