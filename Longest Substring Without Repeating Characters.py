#!/usr/bin/python

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        table = {}
        maxLen = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] in table:
                if maxLen < right - left:
                    maxLen = right - left
                while s[left] != s[right]:
                    del table[s[left]]
                    left += 1
                left += 1
            else:
                table[s[right]] = 1
            right += 1
        return max(maxLen, right - left)
        

test = Solution()
print(test.lengthOfLongestSubstring('dabvdffwagwvwljgowjr;o3nrovjepemrpjgwpgjerb'))
                
                
                
