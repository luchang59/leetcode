import collections
class Solution:
    def findAnagrams(self, s, t):

        # time complexity O(n)
        result = []
        if len(t) > len(s): return result
        
        counter = collections.Counter(t)         # map, for one char, it appears how many times

        count = len(counter)                    # how many distinct char appears in t.
        begin, end = 0, 0                       # sliding window.

        while end < len(s):
            char = s[end]
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0: count -= 1
            end += 1
            while count == 0:
                tempChar = s[begin]
                if tempChar in counter:
                    counter[tempChar] += 1
                    if counter[tempChar] > 0: count += 1
                if end - begin == len(t):
                    result.append(begin)
                begin += 1
        return result 