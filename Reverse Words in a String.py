#!/user/bin/python

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        i = 0
        ans = []
        temp = ''
        res = ''
        while i < len(s):
            if s[i] != ' ':
                temp += s[i]
            if (s[i] == ' ' or i == len(s) - 1 )and temp != '':
                ans.append(temp)
                temp = ''
            i += 1
        print(ans)
        while ans != []:
            word = ans.pop()
            if ans != []:
                res += word + ' '
            else:
                res += word
        return res

test = Solution()
print(test.reverseWords('a '))
                
            
