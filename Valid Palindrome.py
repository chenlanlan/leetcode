#!/user/bin/python

def isPalindrome(self, s):
    n = len(s)
    if n <= 0:
        return True
    s = s.lower()
    i = 0
    j = n - 1
    print(ord('0'),ord('9'))
    while i <= j:
        print(i,j,s[i], s[j])
        while not (ord(s[i])in range (97, 123) or ord(s[i])in range (48, 58)):
                i += 1
                if i == n:
                    return True
        while not (ord(s[j])in range (97, 123) or ord(s[j])in range (48, 58)):
            j -= 1
        if s[i] == s[j] :
            i += 1
            j -= 1
        else:
            return False        
    return True
    
        
self = 0
s = 'ab2a'
print(isPalindrome(self, s))
        
