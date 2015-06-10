#!/usr/bin/python

class Solution:
    # @param {string} digits
    # @return {string[]}
    def numToLetters(self, num):
        d = {'1': [], '2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'],
             '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7':['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        return d[num]

    def letterCombine(self, digits, index, temp, res):
        if index > len(digits) - 1:
            res.append(temp)
            return
        letters = self.numToLetters(digits[index])
        for letter in letters:
            temp += letter
            self.letterCombine(digits, index + 1, temp, res)
            temp = temp[:-1]
        return
    
    def letterCombinations(self, digits):
        res = []
        if digits == '':
            return res
        self.letterCombine(digits, 0, '', res)
        return res

test = Solution()
print(test.letterCombinations('234'))




        
