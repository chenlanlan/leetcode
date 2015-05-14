#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def dfs(self, i, nums, result):
        if i == len(nums):
            result.append(nums[:])
            return
        for j in range(i, len(nums)):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            self.dfs(i + 1, nums , result)
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            
        
    def permute(self, nums):
        result = []
        if len(nums) == 0:
            return result
        self.dfs(0, nums, result)
        return result

test = Solution()
print(test.permute([1, 2, 3, 4]))
        
