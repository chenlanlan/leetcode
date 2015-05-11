#!/usr/bin/python

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        row = [1 for i in range(m)]
        grid = [row for j in range(n)]
        for i in range (1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[n - 1][m - 1]

test = Solution()
print(test.uniquePaths(4, 3))
