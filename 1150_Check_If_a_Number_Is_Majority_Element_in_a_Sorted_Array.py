import collections
class Solution:
    def isMajorityElement(self, nums, target):
        N = len(nums)
        dic = collections.defaultdict(int)
        
        for n in nums:
            dic[n] += 1
        
        if dic[target] > N // 2: return True
        return False