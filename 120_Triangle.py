class Solution:
    def minimumTotal(self, triangle):

        if not triangle or not triangle[0]: return 0

        dp = [[0 for i in range(len(row))] for row in triangle]
        dp[0][0] = triangle[0][0]

        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][0] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[-1])