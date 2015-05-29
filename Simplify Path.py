#!/usr/bin/python

class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        if path == None or len(path) == 0:
            return ''
        stack = []
        res = ''
        i = 0
        while i < len(path):
            index = i
            temp = ''
            while i < len(path) and path[i] != '/':
                temp += (path[i])
                i += 1
            if index != i:
                if temp == '..':
                    if len(stack) != 0:
                        stack.pop()
                elif temp != '.':
                    stack.append(temp)
            i += 1
        if len(stack) != 0:
            for i in range(len(stack)):
                res += '/'+ stack[i]
        if len(res) == 0:
            return '/'
        return res

test = Solution()
print(test.simplifyPath("/a/./b/../../c/"))
