#!/usr/bin/python

class Solution:
    # @param {string} s
    # @return {boolean}
    def isMatch(self, a, b):
        if a == '(':
            return b ==')'
        elif a == '{' :
            return b == '}'
        elif a == '[':
            return b == ']'
        return False
        
    def isValid(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
                continue
            if len(stack)!= 0 and self.isMatch(stack[-1], s[i]):
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        

test = Solution()
print(test.isValid('()'))
