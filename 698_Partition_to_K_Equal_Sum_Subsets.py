class Solution:
    def canPartionKSubsets(self, nums, k):

        target, remainder = divmod(sum(nums), k)
        if remainder or target < max(nums): return False

        seen = [False] * len(nums)

        def dfs(k, curSum, idx):
            if k == 0: return True
            if curSum > target: return False
            if curSum == target: return dfs(k-1, 0, 0)
            
            for i in range(idx, len(nums)):
                if not seen[i]:
                    seen[i] = True
                    dfs(k, curSum + nums[i], i+1)
                    seen[i] = False
            return False
        
        return dfs(k, 0, 0)
