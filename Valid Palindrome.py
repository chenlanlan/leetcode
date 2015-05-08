#!/usr/bin/python

class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        n = len(s)
        if n <= 0:
            return True
        s = s.lower()
        i = 0
        j = n - 1
        while i <= j:
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
    
        
x = Solution()
print(x.isPalindrome('ab2a'))
        
