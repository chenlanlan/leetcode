#!/user/bin/python

def longestCommonPrefix(self, strs):
    n = len(strs)
    if n == 0 or strs[0] == ' ':
        return ''
    for i in range (1, n):
        n1 = len(strs[0])
        for j in range(0, n1):
            if len(strs[i]) < j + 1 or strs[i][j] != strs[0][j]:
                strs[0] = strs[0][0:j]
                break
    return strs[0]

self = 0
strs = ["flower","flow","flight"]
print(longestCommonPrefix(self, strs))
