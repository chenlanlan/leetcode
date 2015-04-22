#!/user/bin/python

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if j == len(needle) - 1 and haystack[i] == needle[j]:
                return i - j
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
        return -1

x = Solution()
print(x.strStr('mississipppi', 'issip'))
