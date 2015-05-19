#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return a list of lists of string       
    def minCut(self, s):
        dp = [0 for i in range(len(s) + 1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s) + 1):
            dp[i] = len(s) - i
        for i in range(len(s) - 1, - 1, - 1):
            for j in range(i, len(s)):
                if s[i] == s[j] and ( (j - i < 2) or p[i + 1][j - 1]):
                    p[i][j] = True
                    dp[i] = min(1 + dp[j + 1], dp[i])
        return dp[0] - 1

test = Solution()
print(test.minCut('ababababababababababababcbabababababababababababa'))

