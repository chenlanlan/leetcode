#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    if nums[left] == target:
                        return left
                    elif nums[left] < target:
                        right = mid - 1
                    else:
                        left = mid + 1
            elif nums[mid] < nums[right]:
                if nums[mid] < target:
                    if nums[left] == target:
                        return left
                    elif nums[left] < target:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1           
        return -1

    def search2(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]:
                if nums[mid] < target or nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target or nums[right] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

test = Solution()
print(test.search2([4, 5, 6, 7, 8, 1, 2, 3], 6))
