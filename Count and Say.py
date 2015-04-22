#!/user/bin/python

class Solution:
    # @param n, an integer
    # @return a string
    def countAndSay(self, n):
        ans = ['' for i in range(n)]
        if n == 1:
            ans[0] += '1'
            return ans[0]
        for h in range (1, n):
            i = 0
            ans[0] += '1'
            l = ans[h - 1]
            while i < len(l):
                j = i + 1
                while j < len(l) and l[i] == l[j]:
                    j += 1
                    print (j)
                ans[h] += str(j - i) + l[i]
                i += j - i
        return ans[n - 1]
   
x = Solution()
print(x.countAndSay(4))
            
