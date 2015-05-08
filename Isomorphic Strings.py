#!/usr/bin/python

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        dict = {}
        for i in range(len(s)):
            if not s[i] in dict:
                for key in dict:
                    if t[i] == dict[key]:
                        return False
                dict[s[i]] = t[i]
            elif t[i] != dict[s[i]]:
                return False
        return True

x = Solution()
print(x.isIsomorphic('aba', 'cdc'))            
            
