#!/usr/bin/python

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0 or strs[0] == ' ':
            return ''
        for i in range (1, n):
            n1 = len(strs[0])
            for j in range(0, n1):
                if len(strs[i]) < j + 1 or strs[i][j] != strs[0][j]:
                    strs[0] = strs[0][0:j]
                    break
        return strs[0]

x = Solution()
print(x.longestCommonPrefix(["flower","flow","flight"]))
