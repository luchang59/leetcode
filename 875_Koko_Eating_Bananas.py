class Solution:
    def minEatSpeed(self, piles, H):

        # similar problems: 1011, 410, 774, 875

        # first step: set valid fuction, determine whether the possible result meet the requirement.
        def valid(possible):
            hours = 0                               # count the time needs
            for p in piles:
                if p <= possible: hours += 1        # if number of banans less than possible result, hours plus one
                else: hours += p // possible + 1    # if number of banans more than possible result, hours plus quotient add one
            return True if hours <= H else False    # if the totla hous less than requirement(H) return True, else False
        
        # use binary search to find the possible result
        start, end = 1, max(piles)                  # the minimum everytime koko can eat is 1 banana and the maximum is max(piles)
        while start < end:                          # here I didn't use start + 1 < end
            mid = (start + end) // 2
            if valid(mid): end = mid
            else: start = mid + 1                   # therefore, start = mid + 1 here
                                   
        return start