#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n = len(nums) - 1
        if n < 1:
            return
        i = n - 1
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        k = n
        while k > i:
            if nums[i] < nums[k]:
                break
            k -= 1
        if i >= 0:
            print(i, k)
            nums[i], nums[k] = nums[k], nums[i]
        nums[i + 1 :] = nums[i + 1 :][::-1]
        return nums

test = Solution()
print(test.nextPermutation([1,2, 3]))
