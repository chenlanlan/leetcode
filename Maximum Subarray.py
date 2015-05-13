#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
        sum = 0
        maxSum = nums[0]
        for i in range(0, len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[i]
            maxSum = max(sum, maxSum)
        return maxSum

test = Solution()
print(test.maxSubArray([-2, 1, -2, 4, -1, 2, 1, -5, 4]))
