class Solution:
    """
    actually, it is DP algorithm, we need to store the prevMax, which is the maximum of the value in front of last value.
    then we need to compare the prevMax + current value and the currMax, then update the currMax
    update the currMax(temp) 
    """
    def rob(self, nums) -> int:
        if not nums: return 0
        
        prevMax = 0
        currMax = 0
        
        for n in nums:
            temp = currMax
            currMax = max(prevMax + n, currMax)
            prevMax = temp

        return currMax