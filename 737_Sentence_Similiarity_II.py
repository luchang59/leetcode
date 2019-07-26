class unionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if x != self.parents[x]:
            self.parents = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.parents[px] = py


class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):

        if len(words1) != len(words2): return False

        dic = {}
        i = 0
        uf = unionFind(len(pairs) * 2)
        
        for pair in pairs:
            for p in pair:
                if p not in dic:
                    dic[p] = i
                    i += 1
            uf.union(pair[0], pair[1])
        
        i = 0
        while i < len(words1):
            w1, w2 = words1[i], words2[i]
            if w1 not in dic or w2 not in dic:
                if w1 != w2: return False
                else:
                    i += 1
                    continue
            if uf.find(w1) != uf.find(w2): return False
            i += 1
        
        return True