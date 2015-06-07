#!/usr/bin/python

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        ans = ''
        i = len(a)
        j = len(b)
        length = i
        if i > j:
            b = '0' * (i - j) + b
        if j > i:
            a = '0' * (j - i) + a
            length = j
        add = 0
        for i in range(length - 1, -1 , -1):
            ans += str((int(a[i]) + int(b[i]) + add) % 2)
            add = (int(a[i]) + int(b[i]) + add) // 2
        if add != 0:
            ans += str(add)
        ans = ans[::-1]
        return ans
    
x = Solution()
print(x.addBinary('101', '11'))
