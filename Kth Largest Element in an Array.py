#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        nums.sort()
        if k > len(nums):
            return 0
        else:
            count = 0
            for i in range(len(nums) - 1, -1, -1):
                count += 1
                if count == k:
                    return nums[i]
        return 0

test = Solution()
print(test.findKthLargest([3,2,1,5,6,4], 2))
