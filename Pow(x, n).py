#!/usr/bin/python

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0/self.myPow(x, -n)
        return x * self.myPow(x, n - 1)

    def myPow2(self, x, n):
        if n == 0:
            return 1.0
        if n < 0:
            return 1.0 / self.myPow2(x, -n)
        half = self.myPow2(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

test = Solution()
print(test.myPow2(2, 4))
