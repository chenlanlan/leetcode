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
                result.append(v[:])
                v.append(a)
                v.sort()
                result.append(v[:])
        return result
        
    def subsets(self, nums):
        result = []
        return self.sub(nums, 0, len(nums))

test = Solution()
print(test.subsets([1, 2, 3]))
