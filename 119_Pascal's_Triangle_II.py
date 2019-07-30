class Solution:
    def getRow(self, rowIndex):
        # Iteration Solution:
            # Time Complexity: O(N ^ 2)
            # Space Complexity: O(N)

        res = [1]
        if not rowIndex: return res
        
        n = 1
        while n <= rowIndex:
            new = [0] * (n + 1)
            new[0] = res[0]
            new[-1] = res[-1]
            for i in range(1, n):
                new[i] = res[i - 1] + res[i]
            res = new
            n += 1
        return res
