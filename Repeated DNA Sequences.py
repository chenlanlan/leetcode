#!/usr/bin/python

import collections
class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        n = len(s)
        dict = {}
        res = []
        for i in range(n - 9):
            if i < n - 10:
                if s[i : i + 10] in dict and dict[s[i : i + 10]] == 1:
                    res.append(s[i : i + 10])
                    dict[s[i : i + 10]] += 1
                elif s[i : i + 10] not in dict:
                    dict[s[i : i + 10]] = 1
            elif s[i: ] in dict and dict[s[i : i + 10]] == 1:
                res.append(s[i : i + 10])
                dict[s[i : i + 10]] += 1
            else:
                dict[s[i : i + 10]] = 1
        return res
    
    def findRepeatedDnaSequences2(self, s):
        n = len(s)
        count = collections.Counter()
        res = []
        for i in range(n - 9):
            if i < n - 10:
                if count[s[i : i + 10]] == 1:
                    res.append(s[i : i + 10])
                    count.update({s[i : i + 10]: 1})
                elif count[s[i : i + 10]] == 0:
                    count.update({s[i : i + 10]: 1})
            elif count[s[i: ]] == 1: 
                res.append(s[i: ])
                count.update({s[i: ]: 1})
        return res

test = Solution()
print(test.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
print(test.findRepeatedDnaSequences2('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
                
                
