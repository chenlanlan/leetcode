#!/user/bin/python

def minimumTotal(self, triangle):
    sum = triangle
    ans = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(0, i + 1):
            if j == 0:
                sum[i][j] = sum[i - 1][j] + triangle[i][j]
                ans = sum[i][j]
            elif j == i:
                sum[i][j] = sum[i - 1][j - 1] + triangle[i][j]
            else:
                sum[i][j] = min(sum[i - 1][j - 1], sum[i - 1][j]) + triangle[i][j]
            if sum[i][j] < ans:
                ans = sum[i][j]
    return ans

self = 0
triangle =[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(minimumTotal(self, triangle))
