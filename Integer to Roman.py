#!/user/bin/python

class Solution:
    # @return a string
    def intToRoman(self, num):
        result = ''
        s_number = str(num)
        length = len(s_number)
        j = 1
        def convert(n):
            if n == 1:
                return 'IVIX'
            if n == 2:
                return 'XLXC'
            if n == 3:
                return 'CDCM'
            if n == 4:
                return 'M'
        for i in range (length - 1, -1, -1):
            if int(s_number[i]) < 4:
                result = (int(s_number[i]) % 5) * convert(j)[0] + result
            elif int(s_number[i]) == 4:
                result = convert(j)[0:2] + result
            elif int(s_number[i]) < 9:
                result = convert(j)[1] + (int(s_number[i]) % 5) * convert(j)[0] + result
            else:
                result = convert(j)[2:] + result
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
        for i in range(0, 13):
            count = num // kBase[i]
            num = num % kBase[i]
            while count > 0:
                roman += kLetter[i]
                count -= 1
        return roman


    
    
