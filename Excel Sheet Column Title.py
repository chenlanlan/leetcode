#!/usr/bin/python

class Solution:
    # @return a string
    def convertToTitle(self, num):
        s = []
        b = 0
        while int(num) > 0:
            b = int(num) % 26
            if b ==0:
                s.append('Z')
                num = int(num) - 1
            else:
                s.append(chr(64 + b))
            num = int(num) // 26
        s.reverse()
        return "".join(s)

x = Solution()
print (x.convertToTitle(52))


