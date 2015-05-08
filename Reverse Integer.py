#!/usr/bin/python

class Solution:
    # @return an integer
    def reverse(self, x):
        x_ori = x
        if x < 0:
            x_ori = x
            x = abs(x)
        x_str = str(x)
        xNew_str = x_str[::-1]
        if int(xNew_str) > 2147483647:
            return 0
        if x_ori >= 0:
            return int(xNew_str)
        else:
            return -int(xNew_str)

x = Solution()
print (x.reverse(234))
        


