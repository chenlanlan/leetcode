#!/usr/bin/python

import collections
class Solution:
    # @param {string} s
    # @return {string[]}    
    def findRepeatedDnaSequences(self, s):
        d = {}
        res = []
        for i in range(len(s) - 9):
            if s[i: i + 10] in d:
                if s[i: i + 10] not in res:
                    res.append(s[i: i + 10])
            else:
                d[s[i: i + 10]] = 1
    return res

test = Solution()
print(test.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
                
                
