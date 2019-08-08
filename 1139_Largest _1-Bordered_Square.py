from typing import List 

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        
        R, C = len(grid), len(grid[0])
        hor = [g[:] for g in grid]
        ver = [g[:] for g in grid]
        res = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j]:
                    if i: ver[i][j] += ver[i - 1][j]
                    if j: hor[i][j] += hor[i][j - 1]
        
        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                radius = min(hor[i][j], ver[i][j])
                while radius > res:
                    if (ver[i][j - radius + 1] >= radius and 
                        hor[i - radius + 1][j] >= radius):
                        res = radius
                    radius -= 1
        
        return res * res