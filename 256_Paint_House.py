class Solution:
    def minCost(self, costs):

        for row in range(1, len(costs)):
            for col in range(3):
                costs[row][col] += min(costs[row - 1][:col] + costs[row - 1][col + 1:])

        return min(costs[-1]) if costs else 0