class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        
        res = float('inf')
        nums.sort()
        length = len(nums)
        
        for i in range(length - 2):
            # if nums[i] > target: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            l, r = i + 1, length - 1
            while l < r:
                totalSum = nums[i] + nums[l] + nums[r]
                if totalSum == target: return totalSum
                if abs(totalSum - target) < abs(res - target):
                    res = totalSum
                if totalSum > target:
                    r -= 1
                elif totalSum < target:
                    l += 1
            
        return res