class Solution:
    def removeDuplicate(self, nums):
        if not nums: return 0

        i = 0
        for j in range(len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1