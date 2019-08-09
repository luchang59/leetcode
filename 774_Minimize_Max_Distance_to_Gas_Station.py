class Solution:
    def minmaxGasDist(self, stations, K):
        
        # similar 1011, 410, 774, 875

        def valid(D):
            station = 0
            for i in range(len(stations) - 1):
                dist = stations[i + 1] - stations[i]
                station += dist // D
            if station <= K: return True
            return False 

        start, end = 0, 10**8
        while start + 1e-6 < end:
            mid = (start + end) / 2.0
            if valid(mid):
                end = mid
            else:
                start = mid
        return start