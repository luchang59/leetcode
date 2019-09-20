import collections

class Solution:
    def numBusesToDestination(self, routes, S: int, T: int) -> int:
    
        if S == T: return 0

        graph = collections.defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].add(bus)

        queue = collections.deque([(S, 0)])
        seen = set([S])

        while queue:
            stop, buses = queue.popleft()
            if stop == T: return buses
            for bus in graph[stop]:
                for nxt in routes[bus]:
                    if nxt not in seen:
                        queue.append((nxt, buses + 1))
                        seen.add(nxt)
                routes[bus] = []
        
        return -1
