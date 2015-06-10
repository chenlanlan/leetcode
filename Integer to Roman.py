#!/usr/bin/python

class Solution:
    # @return a string
    def convert(self, n):
        if n == 1: return 'IVIX'
        if n == 2: return 'XLXC'
        if n == 3: return 'CDCM'
        if n == 4: return 'M'
        
    def intToRoman(self, num):
        result = ''
        s_num = str(num)
        length = len(s_num)
        j = 1
        for i in range(length -1, -1, -1):
            if int(s_num[i]) < 4:
                result = (int(s_num[i]) % 5) * self.convert(j)[0] + result
            elif int(s_num[i]) == 4:
                result = self.convert(j)[0: 2] + result
            elif int(s_num[i]) < 9:
                result = self.convert(j)[1] + (int(s_num[i]) % 5) * self.convert(j)[0] + result
            else:
                result = self.convert(j)[2:] + result
            j += 1
        return result

x = Solution()
print (x.intToRoman(3999))

class Solution:
    # @return a string      
    def intToRoman2(self, num):
        kBase = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        kLetter = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman = ''
        for i in range(13):
            count = num // kBase[i]
            num = num % kBase[i]
            while count > 0:
                roman += kLetter[i]
                count -= 1
        return roman


    
    
