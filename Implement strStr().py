#!/user/bin/python

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

self = 0
haystack = 'mississipppi'
needle = 'issip'
print(strStr(self, haystack, needle))
