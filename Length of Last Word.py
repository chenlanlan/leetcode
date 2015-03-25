#!/user/bin/python

def lengthOfLastWord(self, s):
    length = len(s)
    while length > 0:
        for j in range(length - 1, -1, -1):
            if s[length - 1] == ' ':
                length = length - 1
        for i in range(length - 1, -1, -1):
            if s[i] == ' ':
                return length - i -1
            elif i == 0:
                return length
    return 0

self= 0
s = ' a   '
print(lengthOfLastWord(self, s))
