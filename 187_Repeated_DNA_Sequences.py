import collections

class Solution:
    def findRepeatedDnaSequence(self, s):
        
        dic = collections.defaultdict(int)

        for i in range(len(s) - 9):
            dic[s[i:i+10]] += 1
        
        res = []
        for key in dic:
            if dic[key] > 1:
                res.append(key)
        return res