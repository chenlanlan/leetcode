#!/usr/bin/python

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        ans = ''
        i = len(a) - 1
        j = len(b) - 1
        h = 0
        while i >= 0 and j >= 0: #判断共有的部分
            if int(a[i]) + int(b[j]) + h < 2:
                ans += str(int(a[i]) + int(b[j]) + h) 
                h = 0
            else:
                ans += str((int(a[i]) + int(b[j]) + h) % 2)
                h = 1
            i -= 1
            j -= 1
        k = h
        while i >= 0: #加上a多出的部分
            if int(a[i]) + k < 2:
                ans += str(int(a[i]) + k) 
                k = 0
            else:
                k = 1
                ans += '0'
            i -= 1
        while j >= 0: #加上b多出的部分
            if int(b[j]) + k < 2:
                ans += str(int(b[j]) + k) 
                k = 0
            else:
                k = 1
                ans += '0'
            j -= 1
        if k == 1:
            ans += str(k)
        ans = ans[::-1]
        return ans

class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        ans = ''
        i = len(a) - 1
        j = len(b) - 1
        h = 0
        if i > j: #两个字符串补成相同位数
            b = '0' * (i - j) + b
            length = i
        else:
            a = '0' * (j - i) + a
            length = j
        while length >= 0:
            if int(a[length]) + int(b[length]) + h < 2:
                ans += str(int(a[length]) + int(b[length]) + h) 
                h = 0
            else:
                ans += str((int(a[length]) + int(b[length]) + h) % 2)
                h = 1
            length -= 1
        if h == 1:
            ans += str(h)
        ans = ans[::-1]
        return ans
x = Solution()
print(x.addBinary('101', '11'))
