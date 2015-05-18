#!/usr/bin/python

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

test = Solution()
print(test.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
                
                
