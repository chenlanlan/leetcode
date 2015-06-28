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

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    
    def lowerBound(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target and (mid == 0 or nums[mid - 1] < target):
                return mid
            if nums[mid] < target:
                left = mid + 1
            #  not (mid != 0 and nums[mid - 1] >= target)
            else:
                right = mid - 1
        
    return len(nums)

def searchRange(self, nums, target):
    first = self.lowerBound(nums, target);
        if first == len(nums) or nums[first] != target:
            return [-1, -1];
    second = self.lowerBound(nums, target + 1);
        return [first, second - 1]

test = Solution()
print(test.searchRange([1], 1))
                
                
