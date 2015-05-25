#!/usr/bin/python

class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ''
        for i in range(numRows):
            j = i
            flag = True
            while j < len(s):
                result += s[j]
                if i == 0 or i == numRows - 1:
                    j += 2 * (numRows - 1)
                else:
                    if flag:
                        j += 2 * (numRows - 1 - i)
                        flag = False
                    else:
                        j += 2 * i
                        flag = True
        return result

test = Solution()
print(test.convert('12345675890', 3))
            
