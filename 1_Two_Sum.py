from typing import List
import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i in range(len(nums)):
            if target - nums[i] not in dic:
                dic[nums[i]] = i
            else:
                return [i, dic[target - nums[i]]]
        
        # two points solution
        # O(NlogN), if just return the value, the space complacity will be O(1)

        dic = collections.defaultdict(list)
        for i, n in enumerate(nums):
            dic[n].append(i)
        
        nums.sort()
        left, right = 0, len(nums) - 1
        
        while left < right:
            total = nums[left] + nums[right]
            
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                if nums[left] == nums[right]:
                    return [dic[nums[left]][0], dic[nums[right]][1]]
                return [dic[nums[left]][0], dic[nums[right]][0]]
        