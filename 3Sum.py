#!/usr/bin/python

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        temp = []
        for i in range(n):
            left = i + 1
            right = n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    temp = [nums[i], nums[left], nums[right]]
                    if not temp in result:
                        result.append(temp)
                    right -= 1
                    left += 1
                    temp = []
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return result

test = Solution()
print(test.threeSum([3, 0, -2, -1, 1, 2]))
            
