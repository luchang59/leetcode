class Solution:
    def permute(self, nums):
        
        # Backtracking solution
        res = []
        def backtrack(first):
            if first == n:
                res.append(nums[:])
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        backtrack(0)
        return res

        # DFS solution 

        ans = []
        def dfs(num, path):
            if not num: res.append(path)
            for i in range(len(num)): 
                # i = 0: [1, 2, 3] -> [] + [2, 3]
                # i = 1: [1, 2, 3] -> [1] + [3]
                # i = 2: [1, 2, 3] -> [1, 2] + []
                subNum = num[:i] + num[i+1:]
                newPath = path + [num[i]]
                dfs(subNum, newPath)
        dfs(nums, [])
        return ans
        
