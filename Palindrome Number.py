#!/usr/bin/python

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        x_s = str(x)
        length = len(x_s)
        for i in range (length // 2 + 1):
            if x_s[i] != x_s[length - 1 - i]:
                return False
        return True

x = Solution()
print(x.isPalindrome(-121))
        
