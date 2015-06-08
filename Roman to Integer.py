#!/usr/bin/python

class Solution:
    # @return an integer
    def convert(self, sp):
        if sp == 'I': return 1
        if sp == 'V': return 5
        if sp == 'X': return 10
        if sp == 'L': return 50
        if sp == 'C': return 100
        if sp == 'D': return 500
        if sp == 'M': return 1000
    def romanToInt(self, s):
        result = 0
        for i in range(len(s)):
            if i > 0 and self.convert(s[i]) > self.convert(s[i - 1]):
                result += self.convert(s[i]) - 2 * self.convert(s[i - 1])
            else:
                result += self.convert(s[i])
        return result

x = Solution()
print(x.romanToInt('MMMCMXCIX'))
        
