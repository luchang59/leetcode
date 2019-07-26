class Solution:
    def maxProduct(self, words):

        if not words: return 0

        dic, res = {}, 0
        for word in words:
            bit = 0
            for c in words:
                bit |= 1 << (ord(c) - ord('a'))
            dic[bit] = max(dic.get(bit, 0), len(word))
        
        for i in dic:
            for j in dic:
                if i & j == 0:
                    res = max(res, dic[i] * dic[j])
        return res