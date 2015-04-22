#!/user/bin/python

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n == 1:
            return 1
        F = ['o' for i in range(n)]
        F[0] = 1
        F[1] = 2
        for i in range(2, n):
            F[i] = F[i - 1] + F[i - 2]
        return F[n - 1]
x = Solution()
print (x.climbStairs(5))
