#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        zeroCount = 0
        oneCount = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            elif nums[i] == 1:
                oneCount += 1
        for i in range(0, zeroCount):
            nums[i] = 0
        for i in range(zeroCount, zeroCount + oneCount):
            nums[i] = 1
        for i in range(zeroCount + oneCount, len(nums)):
            nums[i] = 2

    def sortColors2(self, nums):
        zeroPointer = -1
        onePointer = -1
        twoPointer = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                twoPointer += 1
                nums[twoPointer] = 2
                onePointer += 1
                nums[onePointer] = 1
                zeroPointer += 1
                nums[zeroPointer] = 0
            elif nums[i] == 1:
                twoPointer += 1
                nums[twoPointer] = 2
                onePointer += 1
                nums[onePointer] = 1
            elif nums[i] == 2:
                twoPointer += 1
                nums[twoPointer] = 2
        return nums

test = Solution()
print(test.sortColors2([2, 1, 0, 2, 0]))
                
