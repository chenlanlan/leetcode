#!/usr/bin/python

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0': return '0'
        s = ''
        l1 = len(num1)
        l2 = len(num2)
        vec1 = [0 for i in range(l1)]
        vec2 = [0 for i in range(l2)]
        res = [0 for i in range(l1 + l2)]
        for i in range(l1):
            vec1[i] = ord(num1[i]) - ord('0')
        for i in range(l2):
            vec2[i] = ord(num2[i]) - ord('0')
        for i in range(l1):
            for j in range(l2):
                res[i + j + 1] += vec1[i] * vec2[j]
        i = l1 + l2 - 1
        while i >= 0:
            if res[i] > 0:
                res[i - 1] += res[i] // 10
                res[i] %= 10
            s = chr(res[i] + ord('0')) + s
            i -= 1
        if s[0] == '0':
            return s[1:]
        else:
            return s
    

test = Solution()
print(test.multiply('22', '72'))
        
