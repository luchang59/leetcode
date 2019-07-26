class solution:
    def permuteUnique(self, nums):

        nums.sort()
        res = []

        def backtrack(lst, path):
            if not lst:
                res.append(path)
                return 
            for i in range(len(lst)):
                if i > 0 and lst[i] == lst[i - 1]: continue
                backtrack(lst[:i] + lst[i+1:], path + [lst[i]])
        
        backtrack(nums, [])
        return res