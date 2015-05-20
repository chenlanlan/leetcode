#!/usr/bin/python

import collections
class Solution:
    # @param {string} s
    # @return {string[]}    
    def findRepeatedDnaSequences(self, s):
        n = len(s)
        sequenceLength = 10
        count = collections.Counter()
        res = []
        for i in range(n - 9):
            if count[s[i : i + sequenceLength]] == 1:
                res.append(s[i : i + sequenceLength])
                count.update({s[i : i + sequenceLength]: 1})
            else:
                count.update({s[i : i + sequenceLength]: 1})
        return res

test = Solution()
print(test.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
                
                
