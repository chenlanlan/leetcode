#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        index = len(s) - 1
        ans = 0
        end = True
        while index >= 0:
            if s[index] == ' ':
                if end:
                    index -= 1
                else:
                    return ans
            else:
                ans += 1
                end = False
                index -= 1
        return ans

x = Solution()
print(x.lengthOfLastWord(' a   '))
