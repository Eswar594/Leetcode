class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            fish = grid[r][c]
            grid[r][c] = 0  
            total_fish = fish

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                total_fish += dfs(nr, nc)
            return total_fish
        
        max_fish = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0: 
                    max_fish = max(max_fish, dfs(i, j)) 
        return max_fish

