#!/usr/bin/python

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        d = [0 for i in range(n)]
        d[0] = 1
        if n > 1:
            if s[1] != '0':
                d[1] = d[0]
                if int(s[0: 2]) <= 26:
                    d[1] += 1
            else:
                if int(s[0: 2]) <= 26:
                    d[1] += 1
        for i in range(2, n):
            if s[i] != '0':
                d[i] += d[i - 1]
            if int(s[i - 1] + s[i]) <= 26 and int(s[i - 1]) != 0:
                d[i] += d[i - 2]
            if d[i - 1] == 0:
                return 0
        return d[n - 1]

test = Solution()
print(test.numDecodings('101'))
