#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def swap(self, nums, h, k):
        i = h
        while nums[i] != nums[k] and i < k:
            i += 1
        if i == k:
            return True
        else:
            return False
        
    def dfs(self, i, nums, result):
        
        if i == len(nums):
            result.append(nums[:])
            return
        for j in range(i, len(nums)):
            if self.swap(nums, i, j) == False:
                continue
            nums[i], nums[j]  = nums[j], nums[i]
            self.dfs(i + 1, nums , result)
            nums[i], nums[j]  = nums[j], nums[i]
            
    def permuteUnique(self, nums):
        result = []
        if len(nums) == 0:
            return result
        self.dfs(0, nums, result)
        return result

test = Solution()
print(test.permuteUnique([1, 1, 2, 2]))
        
