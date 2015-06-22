#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        stack = []
        i = 0
        temp = ''
        while i < len(s):
            if s[i] != ' ':
                temp += s[i]
            if (s[i] == ' ' or i == len(s) - 1) and temp != '':
                stack.append(temp)
                temp = ''
            i += 1
        stack.reverse()
        res = ' '.join(stack)
        
    return res

test = Solution()
print(test.reverseWords('a '))
                
            
