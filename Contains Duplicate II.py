#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        n = len(nums)
        d = {}
        contain = False
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = i
            elif abs(i - d[nums[i]]) <= k:
                if contain == False:
                    contain = True
                else:
                    return False
        return contain

test = Solution()
print(test.containsNearbyDuplicate([1], 2))
                
            
