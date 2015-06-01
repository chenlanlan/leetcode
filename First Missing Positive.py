#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        n = len(nums)
        if n == 0:
            return 1
        for i in range(n):
            while nums[i] != i + 1:
                if nums[i] >= n or nums[i] <= 0 or nums[i] == nums[nums[i] - 1]:
                    break
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

test = Solution()
print(test.firstMissingPositive([4, 1, 3, 3]))
