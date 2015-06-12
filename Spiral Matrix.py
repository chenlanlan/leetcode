#!/usr/bin/python

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def __init__ (self):
        self.ans = []
        
    def spiralOrder(self, matrix):
        cols = len(matrix[0])
        rows = len(matrix)
        if cols == 0 or rows == 0 :
            return self.ans
        self.spiral(matrix, 0, 0, rows, cols)
        return self.ans

    def spiral(self, matrix, x, y, rows, cols):
        if rows <= 0 or cols <= 0:
            return
        for i in range(cols):
            self.ans.append(matrix[x][y + i])
        for j in range(1, rows - 1):
            self.ans.append(matrix[x + j][y + cols - 1])
        if rows > 1:
            for i in range(cols - 1, -1, -1):
                self.ans.append(matrix[x + rows - 1][y + i])
        if cols > 1:
            for j in range(rows - 2, 0, -1):
                self.ans.append(matrix[x + j][y])
        return self.spiral(matrix, x + 1, y + 1, rows - 2, cols - 2)

test = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print('result: ', test.spiralOrder(matrix))
