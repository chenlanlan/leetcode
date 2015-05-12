#!/usr/bin/python

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n == 0:
            return []
        row = [1 for i in range(n)]
        ans = [row[:] for i in range(n)]
        def generate(matrix, x, y, num, rows, cols):
            if rows <= 0 or cols <= 0:
                return
            for i in range(0, cols):
                ans[x][y + i] = num
                num += 1
            for j in range(1, rows - 1):
                ans[x + j][y + cols - 1] = num
                num += 1
            if rows > 1:
                for i in range(cols - 1, -1, -1):
                    ans[x + rows - 1][y + i] = num
                    num += 1
            if cols > 1:
                for j in range(rows - 2, 0, -1):
                    ans[x + j][y] = num
                    num += 1
            return generate(ans, x + 1, y + 1, num, rows - 2, cols - 2)
        generate(ans, 0, 0, 1, n, n)
        return ans

test = Solution()
print(test.generateMatrix(1))
