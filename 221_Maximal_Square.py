class Solution:
    def maximalSquare(self, matrix):

        # Dynamic programming, time O(mn), space O(mn)
        if not matrix: return 0

        rows = len(matrix) + 1
        cols = len(matrix[0]) + 1
        maxLength = 0
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    maxLength = max(maxLength, dp[i][j])
        
        return maxLength * maxLength

        # better Dynamic Programming, time O(mn), space O(m)
        if not matrix: return 0
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [0] * (cols + 1)
        maxsqlen = 0
        prev = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxsqlen * maxsqlen