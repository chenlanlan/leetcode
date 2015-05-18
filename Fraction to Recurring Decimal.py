#!/usr/bin/python

class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        if denominator == 0:
            return ''
        ans = ''
        if numerator > 0 and denominator < 0 or numerator < 0 and denominator > 0:
            ans += '-'
        num = abs(numerator)
        den = abs(denominator)
        res = int(num // den)
        ans += str(res)
        rem = (num % den) * 10
        if rem == 0:
            return ans
        dict = {}
        ans += '.'
        i = 0
        i += len(ans)
        while rem != 0:
            if rem in dict:
                ans = ans[0: dict[rem]] + '(' + ans[dict[rem]:] + ')'
                return ans
            elif rem not in dict:
                dict[rem] = i
            res = int(rem // den)
            ans += str(res)
            rem = (rem % den) * 10
            i += 1
        return ans

test = Solution()
print(test.fractionToDecimal(-7, 12))
    
