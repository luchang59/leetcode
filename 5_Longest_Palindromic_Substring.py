class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP solution
        res = ''
        maxLength = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
            maxLength = 1
            res = s[i]
        
        for i in range(n):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                maxLength = 2
                res = s[i:i+2]
        
        for j in range(n):
            for i in range(j - 1):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j - i + 1 > maxLength:
                        maxLength = j - i + 1
                        res = s[i:j + 1]
        return res 