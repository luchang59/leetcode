class Solution:
    def prisonAfterNDays(self, cells, N):
        
        seen = {}

        while N:
            seen[tuple(cells)] = N

            dic = {i: c for i, c in enumerate(cells)}
            cells[0] = 0
            cells[-1] = 0
            for i in range(1, 7):
                if dic[i-1] == dic[i+1]:
                    cells[i] = 1
                else:
                    cells[i] = 0
            
            N -= 1

            if tuple(cells) in seen:
                N %= seen[tuple(cells)] - N
        
        return cells