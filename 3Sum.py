#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    if not temp in result:
                        result.append(temp)
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        return result

test = Solution()
print(test.threeSum([3, 0, -2, -1, 1, 2]))
            
