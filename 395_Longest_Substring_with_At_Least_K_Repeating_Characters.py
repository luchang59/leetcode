import collections

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0

        dic = collections.defaultdict(int)
        for string in s:
            dic[string] += 1
        
        for c in dic.keys():
            if dic[c] < k:
                subs = s.split(c)
                res = 0
                for sub in subs:
                    res = max(res, self.longestSubstring(sub, k))
                return res