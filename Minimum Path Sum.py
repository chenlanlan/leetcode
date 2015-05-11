#!usr/bin/python

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        ans = grid[:]
        for i in range(1, n):
            ans[i][0] = ans[i - 1][0] + ans[i][0]
        for j in range(1, m):
            ans[0][j] = ans [0][j - 1] + ans[0][j]
        for i in range(1, n):
            for j in range(1, m):
                ans[i][j] = ans[i][j] + min(ans[i - 1][j], ans[i][j - 1])
        return ans[n - 1][m - 1]
        

test = Solution()
grid = [[1, 2, 3, 5], [6, 2, 9, 8], [3, 7, 5, 4]]
print(test.minPathSum(grid))
