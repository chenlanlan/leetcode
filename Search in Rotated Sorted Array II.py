#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[right]:
                if nums[mid] < target or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] < nums[right]:
                if nums[mid] > target or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1
        return False

test = Solution()
print(test.search([3, 1, 1], 3))
