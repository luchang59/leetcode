class Solution:
    def rob(self, nums) -> int:
        
        if not nums: return 0
        if len(nums) <= 3: return max(nums)
        
        # 198 House Robber I
        def helper(nums):
            currMax = 0
            prevMax = 0
            
            for n in nums:
                temp = currMax
                currMax = max(prevMax + n, currMax)
                prevMax = temp
            
            return currMax
        
        return max(helper(nums[:-1]), helper(nums[1:]))