#!/usr/bin/python

class Solution:
    # @return an integer
    def atoi(self, str):
        num_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        def convert(s):
            if ord('0') <= ord(s) and ord(s) <= ord('9'):
                return ord(s) - 48
            else:
                return -1
        length = len(str)
        num = 0
        i = 0
        input_sign = 0
        sign = True
        if length == 0:
            return 0
        while i < length:
            if str[i] == ' ':
                if sign == False:
                    return input_sign * num
            elif str[i] == '-':
                sign = False
                if input_sign == 0:
                    input_sign = -1
                else:
                    return input_sign * num
            elif str[i] == '+':
                sign = False
                if input_sign == 0:
                    input_sign = 1
                else:
                    return input_sign * num
            elif convert(str[i]) >= 0 and convert(str[i]) <= 9:
                if input_sign == 0:
                    input_sign = 1
                sign = False
                num = num * 10 + convert(str[i])
                if num >= 2147483648 and input_sign > 0:
                    return 2147483647 * input_sign
                elif  num >= 2147483648 and input_sign < 0:
                    return 2147483648 * input_sign
            else:
                sign = False
                return num * input_sign
            i += 1
        return num * input_sign
 
x = Solution()
print(x.atoi('+32-11'))
