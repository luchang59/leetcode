import collections

class unionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]: self.parents[py] = px
        elif self.rank[px] < self.rank[py]: self.parents[px] = py
        elif self.rank[px] == self.rank[py]:
            self.parents[px] = py
            self.rank[px] += 1

        
class Solution:
    def accountsMerge(self, accounts):
        
        if not accounts: return []
        
        dicName = {}
        dicID = {}
        i = 0
        
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                dicName[email] = name
                if email not in dicID:
                    dicID[email] = i
                    i += 1
                    
        uf = unionFind(i)
        for acc in accounts:
            for email in acc[1:]:
                uf.union(dicID[acc[1]], dicID[email])
                
        res = collections.defaultdict(list)
        for email in dicName:
            res[uf.find(dicID[email])].append(email)
        
        output = []
        
        for r in res:
            tmp = []
            tmp.append(dicName[res[r][0]])
            tmp.extend(sorted(res[r]))
            output.append(tmp)
        
        return output