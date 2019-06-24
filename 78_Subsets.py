class Solution:
    def subsets(self, nums):

        res = []

        def backtrack(index, path):
            res.append(path)
            for i in range(index, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return res