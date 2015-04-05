#!/user/bin/python

def atoi(self, str):
    num_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    def convert(s):
        if s == num_str[0]:
            num = 0
        elif s == num_str[1]:
            num = 1
        elif s == num_str[2]:
            num = 2
        elif s == num_str[3]:
            num = 3
        elif s == num_str[4]:
            num = 4
        elif s == num_str[5]:
            num = 5
        elif s == num_str[6]:
            num = 6
        elif s == num_str[7]:
            num = 7
        elif s == num_str[8]:
            num = 8
        elif s == num_str[9]:
            num = 9
        else:
            return -1
        return num
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
            print (num)
            if num >= 2147483648 and input_sign > 0:
                return 2147483647 * input_sign
            elif  num >= 2147483648 and input_sign < 0:
                return 2147483648 * input_sign
        else:
            sign = False
            return num * input_sign
        i += 1
    return num * input_sign
 

self = 0
str = '+32-11'
print(atoi(self, str))
