"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?
Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20

Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
"""

class Solution:
    def largestSumOfAverages(self, A, K: int) -> float:

        """
        k = 1:
        for the nums from i to N, the sum of average will be:
        [24/5, 15/4, 14/3, 12/2, 9/1]
        
        k = 2:
        for 1 to end:
        I know we can split it to [1:j] + [j:] ([j:] = dp[j])
        so, I just need to find the best j, also means max(dp[i])
        for this example, it maybe [1:3] + [3:]

        do it again, until we did it k - 1 times.
        """

        N = len(A)

        firstNumSum = [0] * (N + 1)
        for i in range(N):
            firstNumSum[i+1] = firstNumSum[i] + A[i]
        
        def average(i, j):
            return (firstNumSum[j] - firstNumSum[i]) / (j - i)

        dp = [average(i, N) for i in range(N)]
        for _ in range(K - 1):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        
        return dp[0]