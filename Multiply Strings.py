#!/usr/bin/python

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1_int = int(num1)
        num2_int = int(num2)
        ans_int = num1_int * num2_int
        return str(ans_int)

test = Solution()
print(test.multiply('12', '3'))
        
