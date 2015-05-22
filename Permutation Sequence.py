#!/usr/bin/python

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}        
    def getPermutation(self, n, k):
        result = []
        ans = ''
        nums = [i + 1 for i in range(n)]
        if len(nums) == 0:
            return None
        factor = [1 for i in range(n)]
        for i in range(1, n):
            factor[i] = factor[i - 1] * i
        k -= 1
        for i in range(n - 1, 0, -1):
            code = k // factor[i]
            k = k % factor[i]
            result.append(code)
        result.append(0)
        for i in range(n):
            ans += str(nums[result[i]])
            del nums[result[i]]
        return ans

test = Solution()
print(test.getPermutation(4, 6))
    
