#!/usr/bin/python

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        row = [0 for i in range(m)]
        ans = [row[:] for j in range(n)]
        if obstacleGrid[0][0] == 1:
            ans[0][0] = 0
            return 0
        else:
            ans[0][0] = 1
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                ans[i][0] = 0
            else:
                ans[i][0] = ans[i - 1][0]
        for j in range(1, m):
            if obstacleGrid[0][j] == 1:
                ans[0][j] = 0
            else:
                ans[0][j] = ans[0][j - 1]
        for i in range (1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    ans[i][j] = 0
                else:
                    ans[i][j] = ans[i - 1][j] + ans[i][j - 1]
                #print(ans)
        return ans[n - 1][m - 1]

test = Solution()
obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
b = [[0, 1], [0, 0]]
print(test.uniquePathsWithObstacles(b))
