#!/usr/bin/python

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dict = {}
        res = []
        for i in range(len(strs)):
            s = strs[i]
            s = list(s)
            s.sort()
            st = ''
            for j in range(len(s)):
                st += s[j]
            if st in dict:
                if  strs[dict[st]] not in res:
                    res.append(strs[dict[st]])
                res.append(strs[i])               
            else:
                dict[st] = i
        return res

test = Solution()
print(test.anagrams(['bac', 'abc', 'cd', 'dc']))
