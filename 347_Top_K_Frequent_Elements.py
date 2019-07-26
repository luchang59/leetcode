import heapq, collections

class Solution:
    def topKFrequent(self, nums, k):

# ------ heap solution ------
#       count = collections.Counter(nums)
#       return heapq.nlargest(k, count.keys(), key=count.get)

        dic = collections.defaultdict(int)
        frq = collections.defaultdict(list)

        for n in nums:
            dic[n] += 1
        
        for d in dic:
            frq[dic[d]].append(d)

        res = []
        for x in range(len(nums), 0, -1):
            if x in frq:
                for j in frq[x]:
                    res.append(j)
        
        return res[:k]