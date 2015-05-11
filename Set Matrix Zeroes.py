#!/usr/bin/python
#use the first row and first column to record the rows and columns which should be set zeros

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        m = len(matrix[0])
        n = len(matrix)
        rowZero = False
        columnZero = False
        for i in range(m):
            if matrix[0][i] == 0:
                rowZero = True
                
        for j in range(n):
            if matrix[j][0] == 0:
                columnZero = True
                
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if rowZero:
            for i in range(m):
                matrix[0][i] = 0

        if columnZero:
            for j in range(n):
                matrix[j][0] = 0

        return matrix

test = Solution()
matrix = [
  [1,   3,  5,  7],
  [10, 0, 16, 20],
  [23, 30, 34, 50]
]
print(test.setZeroes(matrix))
                
