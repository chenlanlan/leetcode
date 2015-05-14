#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def Jump(self, nums):
        step = 0
        curMax = 0
        curRch = 0
        for i in range(len(nums)):
            if curRch < i:
                step += 1
                curRch = curMax
            curMax = max(curMax, nums[i] + i)
        return step

test = Solution()
print(test.canJump([2, 3, 1, 1, 4]))
