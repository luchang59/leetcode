class Solution:
    def maxProfit(self, prices):
        
        # dp solution:
        # if not prices: return 0
        
        # N = len(prices)
        # gain = [0]
        # for i in range(1, N):
        #     gain.append(prices[i] - prices[i - 1])
        
        # dp = [0] * N
        # for i in range(1, N):
        #     dp[i] = max(gain[i], dp[i-1] + gain[i])
        
        # return max(dp)

        # brute force:
        mini = float('inf')
        res = 0
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            else:
                res = max(res, prices[i] - mini)
        return res