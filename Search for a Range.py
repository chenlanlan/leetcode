#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        range = [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left > n - 1 or nums[left] != target:
            return range
        else:
            range[0] = left
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        range[1] = right
        return range

test = Solution()
print(test.searchRange([1], 1))
                
                
