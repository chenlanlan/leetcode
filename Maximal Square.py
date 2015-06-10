#!/usr/bin/python

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if matrix == []:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        d = [[0] * col for i in range(row)]
        ans = 0
        for i in range(row):
            for j in range(col):
                d[i][j] = int(matrix[i][j])
                if i and j and d[i][j]:
                    d[i][j] = min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1
                ans = max(ans, d[i][j])
        return ans * ans
