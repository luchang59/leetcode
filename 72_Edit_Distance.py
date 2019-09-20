"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        N = len(word1)
        M = len(word2)

        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N + 1):
            dp[i][0] = i
        for j in range(M + 1):
            dp[0][j] = j
        
        for i in range(1, N + 1):
            for j in range(1, M + 1):
                left = dp[i][j-1] + 1
                up = dp[i-1][j] + 1
                up_left = dp[i-1][j-1] if word1[i-1] == word2[j-1] else dp[i-1][j-1] + 1
                dp[i][j] = min(left, up, up_left)
        
        return dp[-1][-1]