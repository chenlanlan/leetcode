#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        first = True
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if first:
                    result = sum
                    first = False
                elif abs(sum - target) < abs(result - target):
                    result = sum
                if result == target:
                    return result
                if sum > target:
                    right -= 1
                else:
                    left += 1
        return result

test = Solution()
print(test.threeSumClosest([-1, 1, -4, 2], 1))
