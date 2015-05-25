#!/usr/bin/python

class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        if len(s) == 0:
            return s
        maxLen = 0
        res = ''
        for i in range(2 * len(s) - 1):
            left = i // 2
            right = i // 2
            if i % 2 == 1:
                right += 1
            string = self.lengthOfPal(s, left, right)
            if maxLen < len(string):
                maxLen = len(string)
                res = string
        return res

    def lengthOfPal(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]
        

test = Solution()
print(test.longestPalindrome('habbbaaba'))
                
                
