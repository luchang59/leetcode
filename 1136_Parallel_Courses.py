import collections
from typing import List

class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        pre = {i: set() for i in range(1, N + 1)}
        nxt = collections.defaultdict(set)

        for u, v in relations:
            pre[v].add(u)
            nxt[u].add(v)
    
        queue = collections.deque([v for v in range(1, N + 1) if not pre[v]])
        N -= len(queue)
        res = 0
        
        while queue:
            res += 1
            for _ in range(len(queue)):
                v = queue.popleft()
                for u in pre[v]:
                    nxt[u].remove(v)
                    if len(nxt[u]) == 0:
                        queue.append(u)
                        N -= 1
        
        return res if N == 0 else -1