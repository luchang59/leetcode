import collections

class Solution:
    def topKFrequent(self, words, k):
        
        dic = collections.defaultdict(int)
        frq = collections.defaultdict(list)

        for word in words:
            dic[word] += 1
        
        for d in dic:
            frq[dic[d]].append(d)
            frq[dic[d]].sort()

        res = []

        for x in range(len(words), 0, -1):
            if x in frq:
                for i in frq[x]:
                    res.append(i)
        
        return res[:k]

        # heapq
        # count = collections.Count(words)
        # heap = [(-freq, word) for word, freq in count.items()]
        # heapq.heapify(heap)
        # return [heapq.heappop(heap)[1] for _ in range(k)]