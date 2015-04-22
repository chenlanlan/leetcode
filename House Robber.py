#!/user/bin/python

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        n = len(num)
        if n == 0:
            return 0
        elif n == 1:
            return num[0]    
        d = [0 for i in range(n)]
        d[0] = num[0]
        d[1] = max(num[0], num[1])
        for i in range(2, n):
            d[i] = max((d[i - 2] + num[i]), d[i - 1])
        return d[n - 1]

x = Solution()
print(x.rob([2,1]))
