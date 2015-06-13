#!/usr/bin/python

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        matrix = [[1] * m for i in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[n - 1][m - 1]

test = Solution()
print(test.uniquePaths(4, 3))
