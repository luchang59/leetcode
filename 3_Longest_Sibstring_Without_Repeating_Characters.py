import collections

class Solution:
    def lengthOfLongestSubstring(self, s):

        res = 0
        if not s: return res

        counter = collections.defaultdict(int)
        count = 0
        begin, end = 0, 0

        while end < len(s):
            char = s[end]
            counter[char] += 1
            if counter[char] > 1:
                count += 1
            end += 1

            while count > 0:
                tempChar = s[begin]
                if counter[tempChar] > 1:
                    count -= 1
                counter[tempChar] -= 1
                begin += 1
            
            res = max(res, end - begin)
        
        return res