#!/usr/bin/python

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        copy = [matrix[i][:] for i in range(n)]
        for j in range(n - 1, -1, -1):
            for i in range(n):
                matrix[i][j] = copy[n - j - 1][i]
        return matrix

    def rotate2(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - i][j]
                matrix[n - 1 - i][j] = temp
        for i in range(n):
            for j in range(i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        return matrix

test = Solution()
matrix = [[1, 2, 3, 4], [1, 2, 3, 4],[1, 2, 3, 4],[1, 2, 3, 4]]
print(test.rotate2(matrix))
