#!/user/bin/python

def titleToNumber(self, s):
    length = len(s)
    number = 0
    for i in range (0, length):
       number = number + (ord(s[i]) - 64) * 26 ** (length - i -1)
    return number
self = 0
s = 'AQRS'
print (titleToNumber(self, s))


