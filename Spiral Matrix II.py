#!/usr/bin/python

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        ans = []
        if n == 0:
            return ans
        ans = [[0] * n for i in range(n)]
        self.generate(ans, 0, 0, 1, n)
        return ans

    def generate(self, ans, x, y, num, n):
        if n <= 0:
            return
        for i in range(n):
            ans[x][y + i] = num
            num += 1
        for j in range(1, n - 1):
            ans[x + j][y + n - 1] = num
            num += 1
        if n > 1:
            for i in range(n - 1, -1, -1):
                ans[x + n - 1][y + i] = num
                num += 1
            for j in range(n - 2, 0, -1):
                ans[x + j][y] = num
                num += 1
        return self.generate(ans, x + 1, y + 1, num, n - 2)

test = Solution()
print(test.generateMatrix(1))
