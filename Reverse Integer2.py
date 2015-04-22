#!/user/bin/python

class Solution:
    # @return an integer
    def reverse2(self, x):
        x_ori = x
        if x < 0:
            x_ori = x
            x = abs(x)
        ans = 0
        while x != 0:
            ans = ans * 10 + (x % 10)
            x = x // 10
        if ans > 2147483647:
            return 0
        if x_ori >= 0:
            return ans
        else:
            return -ans
x = Solution()
print (x.reverse2reverse2(-123))
