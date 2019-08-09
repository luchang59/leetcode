class Solution:
    def numIslands(self, grid):
        
        # DFS Solution
        # if not grid: return 0
        
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # R, C = len(grid), len(grid[0])
        # res = 0
        
        # for i in range(R):
        #     for j in range(C):
        #         if grid[i][j] == '1':
        #             stack = [(i, j)]
        #             while stack:
        #                 row, col = stack.pop()
        #                 for d in directions:
        #                     nr, nc = row + d[0], col + d[1]
        #                     if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '1':
        #                         grid[nr][nc] = '0'
        #                         stack.append((nr, nc))
        #             res += 1
        
        # return res

        # Union Find
        if not grid: return 0
        R = len(grid); C = len(grid[0])
        self.count = sum(grid[i][j]=='1' for i in range(R) for j in range(C))
        parent = [i for i in range(R*C)]
        
        def find(x):
            if parent[x]!= x:
                return find(parent[x])
            return parent[x]
        
        def union(x,y):
            xroot, yroot = find(x),find(y)
            if xroot == yroot: return 
            parent[xroot] = yroot
            self.count -= 1
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '0':
                    continue
                index = i*C + j
                if j < C-1 and grid[i][j+1] == '1':
                    union(index, index+1)
                if i < R-1 and grid[i+1][j] == '1':
                    union(index, index+C)
        return self.count