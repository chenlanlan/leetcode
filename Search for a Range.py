#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        ans = []
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == 0 or nums[mid] != nums[mid - 1]):
                ans.append(mid)
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if ans == []:
            return [-1, -1]
        left, right = ans[0], len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid] != nums[mid + 1]):
                ans.append(mid)
                return ans
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

test = Solution()
print(test.searchRange([1], 1))
                
                
