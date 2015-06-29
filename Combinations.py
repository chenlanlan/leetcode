#!/usr/bin/python

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def __init__(self):
        self.result = []

    def combine(self, n, k):
        path = []
        self.dfs(n, k, 1, 0, path)
        return self.result

    def dfs(self, n, k, start, cur, path):
        if cur == k:
            self.result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            self.dfs(n, k, i + 1, cur + 1, path)
            path.pop()
            

test = Solution()
print(test.combine(3, 2))

