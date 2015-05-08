#!/usr/bin/python

class Solution:
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        if m > n or n <= 0 or m <= 0:
            return 0
        mid = (m + n) // 2
        return mid & self.rangeBitwiseAnd(m, mid - 1) & self.rangeBitwiseAnd(mid + 1, n)
    def rangeBitwiseAnd2(self, m, n):
        if m == 0:
            return 0
        move = 1
        while m != n:
            m = m >> 1
            n = n >> 1
            move = move << 1
        return m * move

x = Solution()
print(x.rangeBitwiseAnd(5, 7))
print(x.rangeBitwiseAnd2(2, 2147483647))

