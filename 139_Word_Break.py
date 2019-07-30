import collections

class Solution:
    def wordBreak(self, s, wordDict):


        # BFS Solution, time complexity O(n^2), space O(n) length of queue is len(s)
        queue = collections.deque([0])
        seen = [0] * len(s)      #

        while queue:
            start = queue.popleft()
            if start == len(s): return True
            if start not in seen:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        queue.append(end)
                seen.add(start)
        return False


        # Dynamic Programming, time complexity O(n^2), space complexity O(n) length of array is len(s) + 1

        N = len(s)
        dp = [False] * (N + 1)
        dp[0] = True

        for start in range(N):
            for end in range(start + 1, N + 1):
                if dp[start] and s[start:end] in wordDict:
                    dp[end] = True
        
        return dp[-1]