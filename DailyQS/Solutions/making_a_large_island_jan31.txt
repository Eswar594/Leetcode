class Solution:
    def largestIsland(self, grid):
        n, idx, dirs = len(grid), 2, [(0, 1), (1, 0), (0, -1), (-1, 0)]
        areaMap = {}

        def dfs(i, j, id):
            if not (0 <= i < n and 0 <= j < n and grid[i][j] == 1): return 0
            grid[i][j] = id
            return 1 + sum(dfs(i + dx, j + dy, id) for dx, dy in dirs)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1: areaMap[idx] = dfs(i, j, idx); idx += 1

        maxArea = max(areaMap.values(), default=0)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = {grid[i+dx][j+dy] for dx, dy in dirs if 0 <= i+dx < n and 0 <= j+dy < n and grid[i+dx][j+dy] > 1}
                    maxArea = max(maxArea, 1 + sum(areaMap[k] for k in seen))

        return maxArea
