class Solution:
    def gasStation(self, gas, cost):

        N = len(gas)
        total, curr, start = 0, 0, 0

        for i in range(N):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0
        
        return start if total >= 0 else -1
