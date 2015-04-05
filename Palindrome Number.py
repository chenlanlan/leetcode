#!/user/bin/python

def isPalindrome(self, x):
    x_s = str(x)
    length = len(x_s)
    for i in range (0, length // 2 + 1):
        if x_s[i] != x_s[length - 1 - i]:
            return False
    return True

self = 0
x = -121
print(isPalindrome(self, x))
        
