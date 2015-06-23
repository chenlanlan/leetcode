#!/usr/bin/python

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        if m == 0:
            return 0
        move = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            move += 1
        return m << move

x = Solution()
print(x.rangeBitwiseAnd(5, 7))

