#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def sub(self, nums, idx, n):
        result = []
        if idx == n:
            temp = []
            result.append(temp)
        else:
            vec = self.sub(nums, idx + 1, n)
            a = nums[idx]
            for i in range(len(vec)):
                v = vec[i]
                if v not in result:
                    result.append(v[:])
                v.append(a)
                v.sort()
                if v not in result:
                    result.append(v[:])
        return result
        
    def subsetsWithDup(self, nums):
        result = []
        return self.sub(nums, 0, len(nums))      
            
test = Solution()
print(test.subsetsWithDup([1, 2, 2]))
