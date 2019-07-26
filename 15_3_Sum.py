class Solution:
    def threeSum(self, nums):
        
        # two pointers solution
        # O(n ^ 2)

        res = []
        nums.sort()
        N = len(nums)

        for i in range(N - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            left, right = i + 1, N - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0: left += 1
                elif total > 0: right -= 1
                else:
                    res.append(nums[i], nums[left], nums[right])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                left += 1
                right -= 1
        
        return res