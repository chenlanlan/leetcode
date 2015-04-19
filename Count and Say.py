#!/user/bin/python


def countAndSay(self, n):
    ans = ['' for i in range(n)]
    if n == 1:
        ans[0] += '1'
        return ans[0]
    for h in range (1, n):
        i = 0
        ans[0] += '1'
        while i <len(ans[h - 1]):
            j = i + 1
            while j < len(ans[h - 1]) and ans[h - 1][i] == ans[h - 1][j]:
                j += 1
                print (j)
            ans[h] += str(j - i) + ans[h - 1][i]
            i += j - i
    return ans[n - 1]
   
self = 0
n = 4
print(countAndSay(self, n))
            
