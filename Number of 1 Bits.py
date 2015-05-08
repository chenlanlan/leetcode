#!/usr/bin/python

class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n > 0:
            n &= (n - 1)
            count += 1
        return count

test = Solution()
print(test.hammingWeight(7))
