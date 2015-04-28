#!/user/bin/python

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        L = []
        def HappyNumber(n, L):
            if n == 1:
                return True
            n_str = str(n)
            ans = 0
            for i in range(len(n_str)):
                ans += int(n_str[i]) * int(n_str[i])
            if ans in L:
                return False
            L.append(ans)
            return HappyNumber(ans, L)
        return HappyNumber(n, L)

x = Solution()
print(x.isHappy(11))
