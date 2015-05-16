#!/usr/bin/python

class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        def interDivide(dividend, divisor):
            if dividend < divisor:
                return 0
            result = 1
            temp = divisor
            while temp <= dividend:
                left = dividend - temp
                temp <<= 1
                if temp > dividend:
                    break
                else:
                    result <<= 1
            return result + interDivide(left, divisor)
        if dividend >= 0 and divisor > 0 or dividend <= 0 and divisor < 0:
            positive = True
        else:
            positive = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        if positive:
            return min(2147483647, interDivide(dividend, divisor))
        else:
            return (- 1) * min(2147483648, interDivide(dividend, divisor))

test = Solution()
print(test.divide(87, 4))
        
