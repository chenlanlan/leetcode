#!/user/bin/python

def romanToInt(self, s):
    def convert(sp):
        if sp == 'I':
            return 1
        if sp == 'V':
            return 5
        if sp == 'X':
            return 10
        if sp == 'L':
            return 50
        if sp == 'C':
            return 100
        if sp == 'D':
            return 500
        if sp == 'M':
            return 1000
    length = len(s)
    result = 0
    for i in range (0, length):
        if i > 0 and convert(s[i]) > convert(s[i - 1]):
            result += convert(s[i]) - 2 * convert(s[i - 1])
        else:
            result += convert(s[i])
    return result

self = 0
s = 'MMMCMXCIX'
print(romanToInt(self, s))
        
