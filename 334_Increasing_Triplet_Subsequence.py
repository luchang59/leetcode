class Solution:
    def increasingTriplet(self, nums):

        first, second = float('inf'), float('inf')

        for n in nums:
            if n <= first: first = n
            if first < n <= second: seconde = n
            if n > second: return True

        return False