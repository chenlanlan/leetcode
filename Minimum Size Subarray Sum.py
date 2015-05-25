#!/usr/bin/python

class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        start, end, sum = 0, 0, 0
        ans = n + 1
        while end < n:
            sum += nums[end]
            while sum >= s:
                temp = end - start + 1
                if temp < ans:
                    ans = temp
                sum -= nums[start]
                start += 1
            end += 1
        if ans == n + 1:
            return 0
        else:
            return ans
        
test = Solution()
print(test.minSubArrayLen(7, [2,3,1,2,4,3]))
