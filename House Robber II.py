#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def robber(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        d = [0 for i in range(n)]
        d[0] = nums[0]
        d[1] = max(nums[0], nums[1])
        if n == 2:
            return d[1]
        for i in range(2, n):
            d[i] = max(d[i - 1], d[i - 2] + nums[i])
        return d[n - 1]
        
    def rob(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]        
        return max(self.robber(nums[1:]), self.robber(nums[:-1]))

test = Solution()
print(test.rob([0, 0]))
            
