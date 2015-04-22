#!/user/bin/python

class Solution:
    # @param s, a string
    # @return an integer
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

x = Solution()
print(x.lengthOfLastWord(' a   '))
