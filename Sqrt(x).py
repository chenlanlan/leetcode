#!/usr/bin/python

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        ans = x
        while abs(ans * ans - x) > 0.0001:
            ans = (ans + x / ans) / 2
            print(ans)
        return int(ans)

    def mySqrt2(self, x):
        if x <= 1:
            return x
        left = 1
        right = x / 2 + 1
        while left < right:
            mid = (left + right) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid
            print (left, right)
        return int(right)
        

test = Solution()
print(test.mySqrt2(7))
