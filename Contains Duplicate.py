#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        table = {}
        for i in range(len(nums)):
            if nums[i] not in table:
                table[nums[i]] = 1
            else:
                return True
        return False

test = Solution()
print(test.containsDuplicate([1, 2, 4, 6, 7, 3, 5, 4]))
