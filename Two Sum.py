#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        dict = {}
        res = []
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]] + 1, i + 1]
            dict[nums[i]] = i


test = Solution()
print(test.twoSum([2, 7, 11, 15, 8], 10))
            
        
