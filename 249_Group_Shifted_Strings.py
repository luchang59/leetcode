import collections

class Solution:
    def groupStrings(self, strings):

        res = collections.defaultdict(list)

        for s in strings:
            tmp = []
            for i in range(1, len(s)):
                tmp.append((ord(s[i]) - ord(s[i - 1])) % 26)
            res[tuple(tmp)].append(s)

        return list(res.values())