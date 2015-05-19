#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def dfs(self, i, nums, result):
        if i == len(nums):
            result.append(nums[:])
            return
        for j in range(i, len(nums)):
            nums[i], nums[j]  = nums[j], nums[i]
            self.dfs(i + 1, nums , result)
            nums[i], nums[j]  = nums[j], nums[i]
            
        
    def permute(self, nums):
        result = []
        if len(nums) == 0:
            return result
        self.dfs(0, nums, result)
        return result

test = Solution()
print(test.permute([1, 2, 3, 4]))
        
