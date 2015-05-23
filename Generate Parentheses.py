#!/usr/bin/python

class Solution:
    # @param {integer} n
    # @return {string[]}
    def __init__(self):
        self.res = []
        
    def create(self, countleft, countright, s):
        if countleft == 0 and countright == 0:
            self.res.append(s)
            return
        if countleft > 0:
            self.create(countleft - 1, countright, s + '(')
        if countright > countleft:
            self.create(countleft, countright - 1, s + ')')
        
        
    def generateParenthesis(self, n):
        if n == 0 :
            return self.res
        self.create(n, n, '')
        return self.res

test = Solution()
print(test.generateParenthesis(3))
