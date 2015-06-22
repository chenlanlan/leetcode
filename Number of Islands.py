class Solution:
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1': continue
                ans += 1
                self.dfs(grid, i, j, m, n)
        return ans
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n: return
        if grid[i][j] == '1':
            grid[i][j] = '2'
            self.dfs(grid, i - 1, j, m, n)
            self.dfs(grid, i + 1, j, m, n)
            self.dfs(grid, i, j - 1, m, n)
            self.dfs(grid, i, j + 1, m, n)
