from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for s, e in red_edges: red[s].append(e)
        for s, e in blue_edges: blue[s].append(e)

        seen = set()
        res = [float('inf')] * n
        queue = deque([(0, -1, 0), (0, 1, 0)])

        while queue:
            node, color, step = queue.popleft()
            res[node] = min(res[node], step)

            if color == 1:
                for nei in red[node]:
                    if (nei, color) not in seen:
                        queue.append((nei, color * -1, step + 1))
                        seen.add((nei, color))
            else:
                for nei in blue[node]:
                    if (nei, color) not in seen:
                        queue.append((nei, color * -1, step + 1))
                        seen.add((nei, color))

        return [x if x != float('inf') else -1 for x in res]