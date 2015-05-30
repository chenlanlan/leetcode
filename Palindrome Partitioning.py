#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return a list of lists of string        
    def isPalindrome(self, s):
        return s ==s[::-1]

    def dfs(self, s, res):
        if len(s) == 0:
            Solution.res.append(res[:])
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[: i]):
                self.dfs(s[i: ], res + [s[: i]])
        
    def partition(self, s):
        Solution.res = []
        self.dfs(s, [])
        return Solution.res

test = Solution()
print(test.partition('aaab'))

