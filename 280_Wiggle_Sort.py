class Solution:
    def wiggleSort(self, nums):
        less = 1

        for i in range(len(nums) - 1):
            if less == +1:
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            else:
                if nums[i] < nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            less *= -1