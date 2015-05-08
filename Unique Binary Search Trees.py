#!/usr/bin/python


class Solution:
    # @param n, an integer
    # @return an integer
    def numTrees(self, n):
        C = [0 for h in range(n + 1)]
        C[0] = 1
        C[1] = 1
        i = 2
        while i <= n :
            j = 0
            while j < i :
                C[i] += C[j] * C[i - j - 1]
                j += 1
            i += 1        
        return C[n]

x = Solution()
print(x.numTrees(3))
        
