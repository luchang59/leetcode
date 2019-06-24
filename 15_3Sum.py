class Solution:
    def threeSum(self, nums):

        res = []
        nums.sort()
        length = len(nums)

        for i in range(length - 2):
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i - 1]: continue
            
            l, r = i + 1, length - 1
            while l < r:
                totalSum = nums[i] + nums[l] + nums[r]

                if totalSum < 0:
                    l += 1
                elif totalSum > 0:
                    r -= 1
                else:
                    res.append(nums[i], nums[l], nums[r])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res