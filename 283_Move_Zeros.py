class Solution:
    def moveZeros(self, nums):

        i, j = 0, 0 

        while i < len(nums):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            i += 1